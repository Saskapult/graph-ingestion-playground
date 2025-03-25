#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser

#SBATCH --nodes=1
#SBATCH --gpus=p100:1
#SBATCH --ntasks-per-node=24
#SBATCH --exclusive
#SBATCH --mem=2G
#SBATCH --time=0-03:00
#SBATCH --account=def-someuser

# This job 

INPUT="fema_nims_doctrine-2017.pdf"

OUTDIR="graphs/$(date +"%FT%T")"

mkdir "$OUTDIR"
echo "Generated from $INPUT" > "$OUTDIR/info"

uv run main.py "$INPUT" -o "$OUTDIR"
