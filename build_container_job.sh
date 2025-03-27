#!/bin/bash
#SBATCH --time=00:50:00
#SBATCH --account=def-ycoady

APPTAINER_NO_MOUNT=tmp apptainer build ollama-phi4.sif ollama-phi4.def
