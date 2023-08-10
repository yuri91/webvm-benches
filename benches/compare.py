#!/usr/bin/python3

import numpy as np
import sys

def collect(fname):
    benches = {}
    with open(fname, "r") as f:
        for l in f.readlines():
            split = l.split(":")
            name = split[0]
            samples = split[1][1:].split(" ")
            samples = np.array([float(s) for s in samples])
            benches[name] = samples
    return benches

native = collect(sys.argv[1])
cheerpx = collect(sys.argv[2])

print(f"{sys.argv[2]}/{sys.argv[1]}")
for b in native:
    avgn = np.mean(native[b])
    avgc = np.mean(cheerpx[b])
    print(f"{b}: {avgc/avgn}")
