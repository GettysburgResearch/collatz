#!/usr/bin/env python3
"""Check a compact physical inverse credit with standard-library integers.

Store W(3i+2); reconstruct W(3i+1)=q+W(6i+2). No synthesis code is imported.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


class Certificate:
    def __init__(self, metadata, values):
        require(metadata["format"] in ("class-two-u8-v1", "fixed-policy-bits-v1"), "unknown encoding")
        self.p, self.q, self.depth = (metadata[k] for k in ("p", "q", "digits"))
        require(all(type(x) is int for x in (self.p, self.q, self.depth)), "integer parameters required")
        require(self.p > self.q > 0 and self.depth >= 2, "parameter range")
        self.n = 3**(self.depth-1)
        self.modulus = 3*self.n
        require(len(values) == self.n, "wrong byte count")
        self.values = values
        self.max_credit = max(values)+self.q
        require(min(values) == 0, "normalization failure")

    def potential(self, residue):
        r = residue % self.modulus
        require(r % 3 != 0, "potential requires a ternary unit")
        if r % 3 == 2:
            return self.values[(r-2)//3]
        return self.q+self.values[(2*((r-1)//3)) % self.n]

    def check(self, policy=None):
        """All reduced rows, including all three possible next ternary digits."""
        v, n, p, q = self.values, self.n, self.p, self.q
        h = n//3
        mx = bytes(max(v[j], v[j+h], v[j+2*h]) for j in range(h))
        minimum_slack = 1 << 30
        for j in range(h):
            i = 3*j
            e0 = 2*q+v[(4*i+2) % n]
            o0 = 2*q-p+mx[(4*j) % h]
            e1 = 2*q+v[(4*i+6) % n]
            e2 = 2*q+v[(4*i+10) % n]
            o2 = q-p+mx[(2*j+1) % h]
            if policy is None:
                c0,c2 = min(e0,o0),min(e2,o2)
            else:
                b0,b2 = 2*j,2*j+1
                c0 = o0 if (policy[b0//8] >> (b0%8)) & 1 else e0
                c2 = o2 if (policy[b2//8] >> (b2%8)) & 1 else e2
            s0 = v[i]-c0
            s1 = v[i+1]-e1
            s2 = v[i+2]-c2
            require(min(s0,s1,s2) >= 0, f"credit failure near class-two index {i}")
            minimum_slack = min(minimum_slack,s0,s1,s2)
        return {"reduced_rows":n,"unit_rows":2*n,"max_credit":self.max_credit,
                "minimum_slack":minimum_slack,"terminal_refund_max":q,
                "a_priori_gap_cap":self.max_credit//q+1}

    def choose_gap(self, positive_unit):
        require(positive_unit > 0 and positive_unit % 3 != 0, "positive unit required")
        r = positive_unit % self.modulus
        original = r
        for gap in range(1,self.max_credit//self.q+2):
            value = self.potential(r)
            if r % 9 in (2,8):
                child = (2*r-1)//3
                high = max(self.potential(child+k*(2*self.modulus//3)) for k in range(3))
                if self.q-self.p+high <= value:
                    final_child = ((1 << gap)*positive_unit-1)//3
                    require(self.q*gap+self.potential(final_child) <= self.p+self.potential(original), "collapsed gap failure")
                    return gap
            require(self.q+self.potential(2*r) <= value, "no certified physical action")
            r = (2*r) % self.modulus
        raise ValueError("even-run bound violated")

    def compile_and_replay(self, t, tail):
        require(t >= 1 and 0 < tail < 3**t and tail % 3 != 0, "invalid cone")
        initial_credit = self.potential(tail)
        constant = tail
        actions = []
        for _ in range(t-1):
            action = self.choose_gap(constant)
            numerator = (1 << action)*constant-1
            require(numerator % 3 == 0, "compiler divisibility")
            constant = numerator//3
            require(constant > 0 and constant % 3 != 0, "compiler unit")
            actions.append(action)
        final_action = 1 if constant % 3 == 2 else 2
        require(self.q*final_action-self.potential(constant) <= self.q, "terminal refund")
        constant = ((1 << final_action)*constant-1)//3
        actions.append(final_action)
        total = sum(actions)
        require(0 < constant < 1 << total, "suffix bound")
        require(self.q*total <= self.p*t+initial_credit+self.q-self.p, "compiler budget")
        coefficient,intercept = 1 << total,constant
        for action in reversed(actions):
            require(coefficient % 2 == 0 and intercept % 2 == 1, "odd affine event")
            coefficient = 3*coefficient//2
            intercept = (3*intercept+1)//2
            for _ in range(action-1):
                require(coefficient % 2 == 0 and intercept % 2 == 0, "even affine event")
                coefficient //= 2
                intercept //= 2
        require(coefficient == 3**t and intercept == tail, "affine endpoint mismatch")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("metadata",type=Path)
    parser.add_argument("--values",type=Path,help="Reuse already reconstructed raw credit bytes; the digest is still checked")
    parser.add_argument("--threads",type=int,default=4)
    parser.add_argument("--no-openmp",action="store_true",help="Compile the reconstruction in portable single-thread mode")
    args = parser.parse_args()
    metadata = json.loads(args.metadata.read_text())
    policy = None
    if metadata["format"] == "fixed-policy-bits-v1":
        policy = gzip.decompress((args.metadata.parent/metadata["policy_file"]).read_bytes())
        count = 2*3**(metadata["digits"]-2)
        require(metadata["policy_bits"] == count, "policy count metadata")
        require(len(policy) == (count+7)//8, "policy byte count")
        require(count % 8 == 0 or policy[-1] >> (count % 8) == 0, "nonzero policy padding")
        require(hashlib.sha256(policy).hexdigest() == metadata["policy_sha256"], "policy digest mismatch")
        if args.values:
            values = args.values.read_bytes()
        else:
            with tempfile.TemporaryDirectory(prefix="collatz-policy-") as temporary:
                tmp = Path(temporary)
                executable = tmp/"reconstruct_policy"
                command = ["c++","-O3","-std=c++17"]
                if not args.no_openmp:
                    command.append("-fopenmp")
                command += [str(args.metadata.parent/"reconstruct_policy.cpp"),"-o",str(executable)]
                subprocess.run(command,check=True)
                (tmp/"policy.bits").write_bytes(policy)
                subprocess.run([str(executable),str(metadata["digits"]),str(metadata["p"]),str(metadata["q"]),
                                str(metadata["max_iterations"]),str(tmp/"policy.bits"),str(tmp/"values.u8"),str(args.threads)],check=True)
                values = (tmp/"values.u8").read_bytes()
    else:
        path = args.metadata.parent/metadata["values_file"]
        values = gzip.decompress(path.read_bytes())
    require(hashlib.sha256(values).hexdigest() == metadata["values_sha256"], "table digest mismatch")
    cert = Certificate(metadata,values)
    result = cert.check(policy)
    require(result["max_credit"] == metadata["max_credit"], "credit metadata mismatch")
    replays = 0
    for t in range(1,7):
        for tail in range(1,3**t):
            if tail % 3:
                cert.compile_and_replay(t,tail)
                replays += 1
    for t in (40,100,1000):
        for tail in (1,2,3**t-1,3**t-2):
            cert.compile_and_replay(t,tail)
            replays += 1
    try:
        Certificate(metadata,bytes(len(values))).check()
    except ValueError:
        pass
    else:
        raise ValueError("zero-credit negative control unexpectedly passed")
    try:
        Certificate(metadata,values[:-1])
    except ValueError:
        pass
    else:
        raise ValueError("truncated-table negative control unexpectedly passed")
    result.update({"p":cert.p,"q":cert.q,"digits":cert.depth,
                   "values_sha256":metadata["values_sha256"],"affine_replays":replays,
                   "negative_controls":["zero_credit_rejected","truncation_rejected"],"status":"PASS"})
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
