#!/bin/bash
#SBATCH --time=24:00:00      # 20 minutes of wall time
#SBATCH -N 1                 # 1 Node
#SBATCH -n 12                 
#SBATCH -mem=8gb  
eval "$(/home/esk81/.usr/local/miniconda/bin/conda shell.bash hook)"           
conda activate breseq
cd data/day10

for i in {2..12}

do
    output_dir=/home/esk81/unbiased_seascapes/data/day10/X"$i"
    mkdir output_dir
    filename=X"$i"p10_R1.gz 
    breseq -p -r reference.gbk -r phagemid.gbk -r shv-1.gbk filename -j 12 -l 120 -o output_dir
done