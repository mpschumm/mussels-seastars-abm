#!/usr/bin/env bash
# Extract useful part from export-world output files

for f in World-*.csv
do
    base="${f%.*}"
    awk '/"TURTLES"/ {p=1; next} /"PATCHES"/ {exit} /^$/ {next} p==1 {print}' $f \
        > ${base}-extract.csv
done
# Combine into one file
# pattern="World-*-extract.csv"
# files=( $pattern )
# echo $(head -n 1 "${files[0]}")',"filename"' > world-extracts-combined.csv
# awk -v OFS=',' '{print $0,("\"" FILENAME "\"")}' World-*-extract.csv | tail -n +2 >> world-extracts-combined.csv
