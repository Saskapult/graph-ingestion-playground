#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser

# This job 

INPUT="fema_nims_doctrine-2017.pdf"

OUTDIR="graphs/$(date +"%FT%T")"

mkdir "$OUTDIR"
echo "Generated from $INPUT" > "$OUTDIR/info"

uv run main.py "$INPUT" -o "$OUTDIR"
