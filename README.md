# Hodgso24_Research_Documentation

**This repo is for documenting the different data making and analysis notebooks and scripts I used while part of Brian O'Shea's research group at MSU.**

The majority of files will be jupyter notebooks, which is where I did most of my work. For redunancy sake I'll include a few of my scripts that I would submit to the slurm workload manager. Most of my notebooks are designed to be able to be copied and pasted directly into a .py file, which would be run by a .sb file. If not, they're stated in the top of the notebook, or just notebooks for playing with plotting things. I will also include a txt file or two, in case you want to recreate some of my code.


### Contents:

|**File Name**|**File Description**|**File Type**|
|---------|--------|-------|
| Slices_and_projections | Details how to make slices and projections in yt, brief on how to make movies | ipynb |
| Phase_Plots | Details how to make phase plots in yt | ipynb |
| Stellar_Density | Details how to make stellar density plots, including plots of new stars | ipynb |
| Star_Formation_Rate | Details how to plot SFR over time, how to smooth it out | ipynb |
| Cumulative_Star_Plot | Details how to make a plot of all stars formed throughout the sim| ipynb |
| Script_For_Disk_Data | Details making slices and projections and phase plots for just the disk of the galaxy | ipynb |
| Disk_and_CGM_Mass | Details how to make txt files with info on the mass in the disk and CGM | ipynb |
| Plotting_Mass | Takes the mass txt files made from the previous file and plots them | ipynb |
| Plotting_Metallicity_and_Temp | Details how to make txt files for mass-weighted averages of metallicity and temperature, and then plots them | ipynb |
| Multipanel_Plots | Details multiple methods for making multi panel plots of slices | ipynb |
| Multipanel_Comparassions | How to make a movie of multi panel plots| ipynb |
| Script_for_KS_Law | Details how to make txt files containting SFR density and gas surface density, as well as the parameters for a power law fit. Plots them to test the Kennicutt-Schmidt Law | ipynb |
| H2_Density | Details how to make a yt derived field for testing the density of H2 and stellar mass formed. Testing the H2 star formation algorithm used in two sims | ipynb |
| WIP_Projection_Progressions | Work in progress trying to make static in time projections that progress through the sim box. Not finished, not tested | ipynb |
| Example_python_script | An example of a script I would make with python, and would be run as a batch job | py |
| Example_batch_job | An example of a batch job file I would submit to slurm with ``sbatch Example_batch_job.sb`` | sb |
| Stars_Formed_Example | An example txt files with the number of stars formed in a simulation. Can be used with some of the plotting scripts | txt |
| CGM_Mass_Example | An example of a txt file with the mass of the CGM. Can be used in some of the plotting scripts | txt |


### General Tips:
- This assumes that you know how to use the basics of numpy, matplotlib, and yt
- The order listed in the contents is the reccomended order of reading (if you're new to this)
- Make sure to make your axes/limits the same for all sims you're looking at so they're easier to compare to each other
- I've left the sim names/paths in my scripts, so make sure to change that before running any of them to fit your specific sim

### Future Work:

I included one WIP file to do with projection progression, however there's a few other things that would be useful for any future work. I think it could be interesting to try a similar thing with slices, moving through the box to get a wholistic view through the slices. I dabled very breifly with volume rendering, but going into more detail with it would be interesting. I think it would also be worth while to try and recreate some plots similar to the ones used in the Kopenhafer, O'shea, Voit 2023 paper, especially the ones related to the change in mass. That particularly would give a good idea on whether or not gas is accreting onto the disk. It could also be interesting to keep track of the median t<sub>cool</sub> / t<sub>ff</sub> ratio, like they did in the paper. That would help be able to tell if gas is accreting via precipitation. I only ever made a multi panel movie of radial velocity for two of the sims, so it could be useful to do it for the other fields and for the other simulations.
