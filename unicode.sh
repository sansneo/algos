#!/bin/sh

# Generating random sample file name
sample="sample-$(openssl rand -hex 16).txt"
echo "aa" > $sample && stat -c %s $sample ; rm $sample
echo "👾a" > $sample && stat -c %s $sample ; rm $sample
