# misc-scripts
Random scripts for astronomy, research, data management, and productivity

## MeerKAT
Collection of python, slurm and example csv file for automating the download of large MeerKAT observing runs from SARAO archive. Assumes download links for measurement sets have already been created and are copied into the text file along with scheduling block number (SBID), observing date and target name (if necessary). The python script will download all data at once so it assumes that the full observing run has been completed, but new observations can safely be added to the end of the script without re-downloading earlier runs. 

A subdirectory will be created for each unique scheduling block using the information in the csv. If you edit headers, please also edit the python accordingly. If you want to group directories by frequency (e.g., L-band, UHF) then this can also be easily added within csv headers and the python script. 

The slurm script is set to a 72 hour run by default on a single node, and will check for partial downloads. Status will be returned as a log file showing which observation is being downloaded. Incomplete downloads can be resumed. 

The slurm script is NOT designed for interactive mode and so there is no tqdm status bar, but this can be added to the python script if you really want it for some reason.

## Astropy
Code snippets for demixing, sky coverage and prediction for SKA-LOW and other telescopes

## Cross-Matching
General code for basic cross-matching, deduplication, and catalogue manipulation -- starting with basic CSV filtering and moving up to specific cases (TBD). Ultimately aiming to become suitable for a range of telescopes, frequencies and fields wherever necessary. 

## HPC

Random things that seemed useful at the time.
