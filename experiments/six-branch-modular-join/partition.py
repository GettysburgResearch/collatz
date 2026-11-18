"""Run, checkpoint, or combine exact modular-join bucket partitions."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from search import DIGITS, P, Q, UNIT, decode


def contributions(depth):
    modulus = Q**depth
    return [[(-digit*Q**i*pow(P, -i-1, modulus)) % modulus for digit in DIGITS]
            for i in range(depth)]


def scaled(rows, scale, modulus):
    return [[value*scale//modulus for value in row] for row in rows]


def chunk_tables(rows):
    # Small contiguous tables avoid redoing 28 arbitrary-precision additions per pair.
    tables = []
    for start in range(0, len(rows), 5):
        values = [0]
        for row in rows[start:start+5]:
            values = [prefix+value for prefix in values for value in row]
        tables.append((len(values), values))
    return tables[::-1]


def lookup(code, tables):
    total = 0
    for size, table in tables:
        code, digit = divmod(code, size)
        total += table[digit]
    if code:
        raise ValueError("word index out of bounds")
    return total


def digest(data):
    return hashlib.sha256(data).hexdigest()


class Job:
    def __init__(self, directory, depth, bits, base, bound, parts, wide=None):
        self.directory = directory
        self.depth, self.bits, self.base, self.parts = depth, bits, base, parts
        self.bound = bound if wide is None else wide
        self.extra = 1 if wide is None else 2
        self.half = (depth+1)//2
        self.modulus = Q**depth
        self.extended = self.modulus*Q**self.extra
        exact = contributions(depth+self.extra)
        prefix_rows = [[v % self.modulus for v in row] for row in exact[:depth]]
        keys = scaled(prefix_rows, UNIT, self.modulus)
        self.left = chunk_tables(exact[:self.half])
        self.right = chunk_tables(exact[self.half:depth])
        self.left_keys = chunk_tables(keys[:self.half])
        self.right_keys = chunk_tables(keys[self.half:])
        # Every suffix contribution is a multiple of the entire prefix modulus.
        suffixes = {0: ()}
        for row in exact[depth:]:
            if any(v % self.modulus for v in row):
                raise ValueError("suffix not divisible by prefix modulus")
            suffixes = {(key-value//self.modulus) % (Q**self.extra): word+(digit,)
                        for key, word in suffixes.items() for digit, value in enumerate(row)}
        if len(suffixes) != 6**self.extra:
            raise ValueError("suffix collision")
        self.suffixes = suffixes
        lines = [f"{depth} {self.half} {bits} {base} {bound}"]
        if wide is not None:
            tags = scaled(exact, 1<<32, self.extended)
            self.left_tags = chunk_tables(tags[:self.half])
            self.right_tags = chunk_tables(tags[self.half:depth])
            self.allowed = {(e-a-b) % (1<<32) for e in range(-depth-2, 2)
                            for a in tags[depth] for b in tags[depth+1]}
            keys = keys+tags
        lines.extend(" ".join(map(str, row)) for row in keys)
        self.input = "\n".join(lines)+"\n"
        self.identity = dict(depth=depth if wide is None else depth+2, bits=bits, base=base,
                             bound=self.bound, parts=parts, input_sha256=digest(self.input.encode()))
        if wide is not None:
            self.identity["prefix_depth"] = depth

    def prepare(self):
        self.directory.mkdir(parents=True, exist_ok=True)
        manifest, inputs = self.directory/"job.json", self.directory/"input.txt"
        if manifest.exists():
            if json.loads(manifest.read_text()) != self.identity or inputs.read_text() != self.input:
                raise ValueError(f"job identity or input mismatch in {self.directory}")
        else:
            if any(self.directory.glob("*.part")) or any(self.directory.glob("*.verified")):
                raise ValueError("refusing to adopt partitions without matching job manifest")
            inputs.write_text(self.input)
            manifest.write_text(json.dumps(self.identity, sort_keys=True)+"\n")

    def summary(self, index):
        path = self.directory/f"{index}.part"
        cached = self.directory/f"{index}.verified"
        if cached.exists():
            row = json.loads(cached.read_text())
            self.validate_summary(row, index)
            if path.exists() and digest(path.read_bytes()) != row[5]:
                raise ValueError(f"raw partition differs from its verified commitment in {path}")
            return row
        if not path.exists():
            return None
        raw = path.read_bytes()
        records = raw.splitlines()
        buckets = 1<<self.bits
        low, high = buckets*index//self.parts, buckets*(index+1)//self.parts
        if (len(records)<2 or records[0] != f"range {low} {high}".encode()
                or records[-1] != f"complete {len(records)-2}".encode()):
            raise ValueError(f"range or completion mismatch in {path}")
        best = [None, None]
        extensions = 0
        for line in records[1:-1]:
            a, b = map(int, line.split())
            right_key = lookup(b, self.right_keys) % UNIT
            if not low <= right_key >> (64-self.bits) < high:
                raise ValueError(f"wrong ownership in {path}")
            delta = (lookup(a, self.left_keys)+right_key) % UNIT
            if self.bound < delta < UNIT-self.depth:
                raise ValueError(f"outside modular filter in {path}")
            if self.extra == 2:
                tag = (lookup(a,self.left_tags)+lookup(b,self.right_tags)) % (1<<32)
                if tag not in self.allowed:
                    raise ValueError(f"outside suffix tag filter in {path}")
            top, root = divmod((lookup(a,self.left)+lookup(b,self.right)) % self.extended,
                               self.modulus)
            if root == 0:
                raise ValueError("illegal zero root")
            if root*UNIT > self.bound*self.modulus:
                continue
            if self.extra == 1 and (best[0] is None or root < int(best[0][0])):
                best[0] = [str(root), a, b, []]
            suffix = self.suffixes.get(top)
            if suffix is not None:
                extensions += 1
                if best[1] is None or root < int(best[1][0]):
                    best[1] = [str(root), a, b, list(suffix)]
        result = [index, len(records)-2, extensions, best[0], best[1], digest(raw)]
        self.validate_summary(result, index)
        tmp = cached.with_suffix(".verifying")
        tmp.write_text(json.dumps(result,separators=(",",":"))+"\n")
        tmp.replace(cached)
        return result

    def validate_summary(self, row, index):
        if (len(row)!=6 or row[0]!=index or not 0<=row[2]<=row[1]
                or len(bytes.fromhex(row[5]))!=32 or (row[2]>0)!=(row[4] is not None)
                or (self.extra==2 and row[3] is not None)):
            raise ValueError(f"invalid summary for part {index}")
        for slot in (3,4):
            if row[slot] is None:
                continue
            root, left, right, suffix = row[slot]
            bucket=(lookup(right,self.right_keys)%UNIT) >> (64-self.bits)
            if not ((1<<self.bits)*index//self.parts <= bucket
                    < (1<<self.bits)*(index+1)//self.parts):
                raise ValueError("witness does not belong to its part")
            if len(suffix) != (0 if slot==3 else self.extra):
                raise ValueError("wrong witness depth")
            word = decode(left,self.half)+decode(right,self.depth-self.half)+suffix
            if not 0<int(root)*UNIT<=self.bound*self.modulus:
                raise ValueError("witness beyond cap")
            self.endpoint(int(root),word)

    @staticmethod
    def endpoint(source, word):
        for digit in word:
            if not 0<=digit<6:
                raise ValueError("unknown branch digit")
            source, rem = divmod(P*source+DIGITS[digit],Q)
            if rem:
                raise ValueError("physical witness replay failed")
        return source

    def checkpoint(self, archive):
        rows = []
        for i in range(self.parts):
            row = self.summary(i)
            if row is not None:
                rows.append(row)
        header=dict(job=self.identity, complete=len(rows)==self.parts,
                    completed_parts=len(rows), expected_parts=self.parts)
        if archive:
            archive.parent.mkdir(parents=True,exist_ok=True)
            tmp=archive.with_suffix(".tmp")
            with tmp.open("w") as out:
                out.write(json.dumps(header,sort_keys=True)+"\n")
                for row in rows:
                    out.write(json.dumps(row,separators=(",",":"))+"\n")
            tmp.replace(archive)
        return header, rows

    def restore(self, path):
        lines = path.read_text().splitlines()
        header=json.loads(lines[0])
        if (header["job"] != self.identity or len(lines)-1!=header["completed_parts"]
                or header["expected_parts"]!=self.parts
                or header["complete"]!=(len(lines)-1==self.parts)):
            raise ValueError("checkpoint identity or coverage mismatch")
        previous=-1
        for line in lines[1:]:
            row=json.loads(line)
            index=row[0]
            if not previous<index<self.parts:
                raise ValueError("checkpoint part ordering or coverage mismatch")
            self.validate_summary(row,index)
            dest=self.directory/f"{index}.verified"
            if dest.exists() and json.loads(dest.read_text())!=row:
                raise ValueError("conflicting part commitments")
            if (self.directory/f"{index}.part").exists() and not dest.exists():
                if self.summary(index)!=row:
                    raise ValueError("checkpoint conflicts with raw part")
            else:
                tmp=dest.with_suffix(".restoring")
                tmp.write_text(line+"\n")
                tmp.replace(dest)
            previous=index

    def results(self, rows):
        if len(rows)!=self.parts or any(row[0]!=i for i,row in enumerate(rows)):
            raise ValueError("incomplete bucket cover; no full minimum can be certified")
        aggregate=hashlib.sha256(b"".join(bytes.fromhex(r[5]) for r in rows)).hexdigest()
        for slot in ([3,4] if self.extra==1 else [4]):
            covered=[r[slot] for r in rows if r[slot] is not None]
            if not covered:
                raise ValueError("no witness under cap; no minimum certified")
            root,a,b,suffix=min(covered,key=lambda w:int(w[0]))
            word=decode(a,self.half)+decode(b,self.depth-self.half)+suffix
            yield dict(depth=len(word),root=root,word="".join(map(str,word)),
                       endpoint=str(self.endpoint(int(root),word)),prefix_depth=self.depth,
                       prefix_upper_key=self.bound,filter_candidates=sum(r[1] for r in rows),
                       extensions_in_cap=sum(r[2] for r in rows),bucket_bits=self.bits,
                       base_length=self.base,partitions=self.parts,input_sha256=self.identity["input_sha256"],
                       ordered_partition_sha256=aggregate)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=["run","checkpoint","finish","restore"])
    parser.add_argument("directory",type=Path)
    parser.add_argument("--binary",type=Path)
    parser.add_argument("--archive",type=Path)
    parser.add_argument("--depth",type=int,default=28)
    parser.add_argument("--bits",type=int,default=20)
    parser.add_argument("--base",type=int,default=9)
    parser.add_argument("--bound",type=int,default=8192)
    parser.add_argument("--parts",type=int,default=4096)
    parser.add_argument("--wide",type=int)
    parser.add_argument("--suffix-directory",type=Path)
    args=parser.parse_args()
    if (not 2<=args.depth<=38 or not 1<=args.bits<=30 or not 1<=args.parts<=1<<args.bits
            or not 0<args.bound<=(args.wide or args.bound)<(UNIT>>args.bits)//4):
        parser.error("invalid depth, bits, part count or cap")
    if (args.wide is None)!=(args.suffix_directory is None):
        parser.error("--wide and --suffix-directory must be supplied together")
    prefix=Job(args.directory,args.depth,args.bits,args.base,args.bound,args.parts)
    prefix.prepare()
    job=prefix
    if args.wide is not None:
        job=Job(args.suffix_directory,args.depth,args.bits,args.base,args.bound,args.parts,args.wide)
        job.prepare()
    if args.mode=="restore":
        if not args.archive:
            parser.error("restore requires --archive")
        job.restore(args.archive)
    elif args.mode=="run":
        if not args.binary:
            parser.error("run requires --binary")
        command=[str(args.binary.resolve()),str(prefix.directory),str(args.parts)]
        if args.wide is not None:
            command.extend([str(job.directory),str(args.wide)])
        subprocess.run(command,input=job.input,text=True,check=True)
    else:
        head,records=job.checkpoint(args.archive)
        if args.mode=="finish":
            for receipt in job.results(records):
                print(json.dumps(receipt))
        else:
            print(json.dumps(head,sort_keys=True))
