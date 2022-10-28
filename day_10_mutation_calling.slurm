#!/bin/bash
#SBATCH --time=24:00:00      # 20 minutes of wall time
#SBATCH -N 1                 # 1 Node
#SBATCH -n 12                 
#SBATCH -mem=8gb             
module load breseq
cd data/day10
breseq -p -r reference.fasta X12p10_S4_R1.fastq.gz  X12p10_S4_R2.fastq.gz -j 12