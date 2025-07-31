import re

def convert_pbs_to_slurm(pbs_script):
    slurm_lines = []
    for line in pbs_script.splitlines():
        # Convert PBS directives
        if line.startswith("#PBS"):
            line = line.replace("#PBS", "#SBATCH")
            line = re.sub(r"-l walltime=([0-9:]+)", r"--time=\1", line)
            line = re.sub(r"-l nodes=(\d+):ppn=(\d+)", r"--nodes=\1\n#SBATCH --ntasks-per-node=\2", line)
            line = re.sub(r"-N\s+(\S+)", r"--job-name=\1", line)
            line = re.sub(r"-q\s+(\S+)", r"--partition=\1", line)
            line = re.sub(r"-o\s+(\S+)", r"--output=\1", line)
            line = re.sub(r"-e\s+(\S+)", r"--error=\1", line)
        # PBS variable replacements
        line = line.replace("$PBS_O_WORKDIR", "$SLURM_SUBMIT_DIR")
        line = line.replace("cd $PBS_O_WORKDIR", "cd $SLURM_SUBMIT_DIR")
        slurm_lines.append(line)
    return "\n".join(slurm_lines)

