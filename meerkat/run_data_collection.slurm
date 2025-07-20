#!/bin/bash
#SBATCH --job-name=meerkat_download
#SBATCH --output=slurm-%j.out
#SBATCH --error=slurm-%j.err
#SBATCH --time=72:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=4G

# Optional: load environment or activate virtualenv
# module load python/3.10
# source ~/envs/meerket/bin/activate

echo "Starting MeerKAT download job on $(hostname)"
date

python3 grab_meerkat.py

echo "Job completed"
date

