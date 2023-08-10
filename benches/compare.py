#!/usr/bin/python3

import numpy as np
import sys

def collect(fname):
    benches = {}
    with open(fname, "r") as f:
        for l in f.readlines():
            split = l.split(":")
            name = split[0]
            samples = split[1].strip(" \n").split(" ")
            samples = np.array([float(s) for s in samples])
            benches[name] = samples
    return benches

baseline = collect(sys.argv[1])
target = collect(sys.argv[2])

print(f"{sys.argv[2]}/{sys.argv[1]}")
for b in baseline:
    avgbaseline = np.mean(baseline[b][1:])
    avgtarget = np.mean(target[b][1:])
    print(f"{b}: {avgtarget/avgbaseline}")
