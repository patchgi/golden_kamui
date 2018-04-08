#!/bin/bash

for i in `seq 0 99`
do
    c="python app.py $i"
    eval $c
done
exit 0
