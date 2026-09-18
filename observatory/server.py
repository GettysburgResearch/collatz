"""Loopback-only Observatory server. Run: python observatory/server.py.

Not an Internet-facing production service. No arbitrary file serving, eval,
remote dependencies, plugin uploads, or shell endpoints.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import secrets
import threading
import time
from urllib.parse import urlsplit
import webbrowser

try:
    from .core import Budget, Cancelled, TimedOut, LIMITS, MAPS
    from .engine import VERSION, execute, normalize_request, capabilities
except ImportError:
    from core import Budget, Cancelled, TimedOut, LIMITS, MAPS
    from engine import VERSION, execute, normalize_request, capabilities

ROOT = Path(__file__).resolve().parent
MAX_BODY = 32768
ASSETS = {"/": ("lab.html", "text/html"), "/classic": ("index.html", "text/html"), "/app.mjs": ("app.mjs", "text/javascript"),
          "/view.mjs": ("view.mjs", "text/javascript"), "/style.css": ("style.css", "text/css")}
for filename in ("lab.mjs", "workspace.mjs", "panels.mjs", "client.mjs", "lab.css"):
    ASSETS["/" + filename] = (filename, "text/css" if filename.endswith(".css") else "text/javascript")


class Jobs:
    def __init__(self):
        self.lock = threading.RLock()
        self.pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="observatory")
        self.items: dict[str, dict] = {}

    def submit(self, request: dict) -> dict:
        config = normalize_request(request)
        with self.lock:
            if sum(j["status"] in ("running", "cancelling") for j in self.items.values()) >= 2:
                raise RuntimeError("Two jobs are already running. Cancel one or wait for completion.")
            finished = [key for key, j in self.items.items() if j["status"] not in ("running", "cancelling")]
            while len(self.items) >= 8 and finished:
                del self.items[finished.pop(0)]
            key = secrets.token_hex(12)
            self.items[key] = {"id": key, "status": "running", "request": config,
                               "progress": {}, "event": threading.Event(), "started": time.monotonic()}
            self.pool.submit(self._run, key, config)
            return self.get(key)

    def _run(self, key: str, config: dict) -> None:
        with self.lock:
            event = self.items[key]["event"]
        def progress(value):
            with self.lock:
                self.items[key]["progress"] = value
        try:
            data = execute(config, Budget(event, progress))
            # A cooperative cancel wins even when requested immediately after computation.
            if event.is_set() and not data["result"].get("interruption"):
                raise Cancelled("Cancelled by the caller.")
            if len(json.dumps(data, ensure_ascii=True)) > 16000000:
                raise ValueError("Result exceeds the 16 MB retention cap; use smaller horizons or bit limits.")
            update = {"status": data["result"].get("interruption") or "done", "data": data}
        except Cancelled as exc:
            update = {"status": "cancelled", "error": str(exc)}
        except TimedOut as exc:
            update = {"status": "timed_out", "error": str(exc)}
        except Exception as exc:
            update = {"status": "error", "error": f"{type(exc).__name__}: {exc}"}
        with self.lock:
            if update["status"] == "done" and event.is_set():
                update = {"status": "cancelled", "error": "Cancelled by the caller."}
            self.items[key].update(update)
            self.items[key]["elapsed_ms"] = round(1000 * (time.monotonic() - self.items[key]["started"]))

    def get(self, key: str) -> dict:
        with self.lock:
            if key not in self.items:
                raise KeyError("Job not found or expired from the eight-job in-memory cache.")
            return {k: v for k, v in self.items[key].items() if k not in ("event", "started")}

    def cancel(self, key: str) -> dict:
        with self.lock:
            if key not in self.items:
                raise KeyError("Unknown job.")
            if self.items[key]["status"] in ("running", "cancelling"):
                self.items[key]["status"] = "cancelling"
                self.items[key]["event"].set()
            return self.get(key)

    def close(self) -> None:
        with self.lock:
            for job in self.items.values():
                job["event"].set()
        self.pool.shutdown(wait=True, cancel_futures=True)


class Handler(BaseHTTPRequestHandler):
    server_version = "CollatzObservatory/0.3-preview"

    def setup(self):
        super().setup()
        self.connection.settimeout(5)

    def log_message(self, *_):
        pass  # Do not print request bodies, tokens, or hostile control characters.

    def send(self, status: int, data, content_type="application/json"):
        body = json.dumps(data, ensure_ascii=True).encode() if content_type == "application/json" else data
        self.send_response(status)
        self.send_header("Content-Type", content_type + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def guard(self, write=False) -> bool:
        port = self.server.server_port
        hosts = {f"127.0.0.1:{port}", f"localhost:{port}"}
        origin = self.headers.get("Origin")
        if self.headers.get("Host", "").lower() not in hosts or (origin and origin not in {"http://" + h for h in hosts}):
            self.send(403, {"error": "Loopback Host and same-origin requests only."})
            return False
        if write and not secrets.compare_digest(self.headers.get("X-Observatory-Token", ""), self.server.token):
            self.send(403, {"error": "Missing session token; retrieve it from /api/health."})
            return False
        return True

    def do_GET(self):
        if not self.guard():
            return
        path = urlsplit(self.path).path
        if path == "/api/health":
            self.send(200, {"version": VERSION, "token": self.server.token, "limits": LIMITS, "mode": "loopback-only"})
        elif path == "/api/capabilities":
            self.send(200, capabilities())
        elif path.startswith("/api/jobs/"):
            try:
                self.send(200, self.server.jobs.get(path.removeprefix("/api/jobs/")))
            except KeyError as exc:
                self.send(404, {"error": str(exc)})
        elif path in ASSETS:
            filename, mime = ASSETS[path]
            self.send(200, (ROOT / "web" / filename).read_bytes(), mime)
        else:
            self.send(404, {"error": "Not found."})

    def do_POST(self):
        if not self.guard(write=True):
            return
        if self.path != "/api/jobs":
            self.send(404, {"error": "Not found."})
            return
        try:
            if self.headers.get("Transfer-Encoding"):
                raise ValueError("Transfer-Encoding is not supported.")
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= MAX_BODY:
                self.send(413, {"error": f"Body must be 1–{MAX_BODY} bytes."})
                return
            if self.headers.get_content_type() != "application/json":
                self.send(415, {"error": "Use application/json."})
                return
            request = json.loads(self.rfile.read(size))
            self.send(202, self.server.jobs.submit(request))
        except (ValueError, UnicodeDecodeError, RecursionError) as exc:
            self.send(400, {"error": str(exc)})
        except RuntimeError as exc:
            self.send(429, {"error": str(exc)})

    def do_DELETE(self):
        if not self.guard(write=True):
            return
        if not self.path.startswith("/api/jobs/"):
            self.send(404, {"error": "Not found."})
            return
        try:
            self.send(200, self.server.jobs.cancel(self.path.removeprefix("/api/jobs/")))
        except KeyError as exc:
            self.send(404, {"error": str(exc)})

    def do_OPTIONS(self):
        self.send(403, {"error": "Cross-origin access is not supported."})


def make_server(port=8765):
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.token = secrets.token_urlsafe(32)
    server.jobs = Jobs()
    return server


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--open", action="store_true", help="Open the local URL in a browser")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("--port must be in 1..65535")
    try:
        server = make_server(args.port)
    except OSError as exc:
        parser.exit(1, f"Could not bind local port {args.port}: {exc}. Try --port 8766.\n")
    url = f"http://127.0.0.1:{args.port}"
    print(f"Collatz Observatory {VERSION}: {url}\nLocal-only finite experiments. Ctrl+C to stop.", flush=True)
    if args.open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.jobs.close()
        server.server_close()


if __name__ == "__main__":
    main()
