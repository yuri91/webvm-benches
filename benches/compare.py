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

data1 = collect(sys.argv[1])
data2 = collect(sys.argv[2])

avgavg = 0
print(f"{sys.argv[2]}/{sys.argv[1]}")
for b in data1:
    avg1 = np.mean(data1[b][1:])
    avg2 = np.mean(data2[b][1:])
    avgavg += avg2/avg1
    print(f"{b}: {avg2/avg1}")

print(f"\ntotal average: {avgavg/len(data1)}")
