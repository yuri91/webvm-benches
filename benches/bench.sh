#!/bin/bash

cd benches32

for f in ./*.native; do
	echo -n "${f}: "
	/bin/time -f "%e" ${f} > /dev/null 2> /tmp/dump
	cat /tmp/dump | tr '\n' ' '
	/bin/time -f "%e" ${f} > /dev/null 2> /tmp/dump
	cat /tmp/dump | tr '\n' ' '
	/bin/time -f "%e" ${f} > /dev/null 2> /tmp/dump
	cat /tmp/dump | tr '\n' ' '
	/bin/time -f "%e" ${f} > /dev/null 2> /tmp/dump
	cat /tmp/dump | tr '\n' ' '
	/bin/time -f "%e" ${f} > /dev/null 2> /tmp/dump
	cat /tmp/dump | tr '\n' ' '
	echo
done
