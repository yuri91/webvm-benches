#!/bin/bash

set -e

MY_DIR=`dirname "$(readlink -f "$0")"`

outfile=$1
nsamples=$2

rm -f ${outfile}
for f in ${MY_DIR}/benches32/*.native; do
	echo -n "$(basename -- ${f}): " | tee -a ${outfile}
	for (( i=0; i<$nsamples; i++ ))
	do
		/bin/time -f "%e" ${f} > /dev/null 2> /tmp/dump
		cat /tmp/dump | tr '\n' ' ' | tee -a ${outfile}
	done
	echo | tee -a ${outfile}
done
