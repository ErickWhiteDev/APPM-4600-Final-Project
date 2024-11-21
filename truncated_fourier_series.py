#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import time
from scipy.fft import fft, ifft, fftshift, ifftshift

mpl.rcParams.update({'font.size': 16})
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['axes.linewidth'] = 2

mpl.rcParams['xtick.major.size'] = 8
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['xtick.minor.size'] = 2
mpl.rcParams['xtick.minor.width'] = 1

mpl.rcParams['ytick.major.size'] = 8
mpl.rcParams['ytick.major.width'] = 2
mpl.rcParams['ytick.minor.size'] = 2
mpl.rcParams['ytick.minor.width'] = 1

mpl.rcParams['xtick.major.pad']='8'
mpl.rcParams['ytick.major.pad']='8'

# load data
data = np.loadtxt("boulder_temp.txt")
data = data[:,3]
day = np.arange(data.size)

# plot data
fig, ax = plt.subplots(2, 2)


# take fft
df = fft(data)
dfshift = df

i = 0
j = 0
for N in [732, 250, 50, 6]:
    dfshift[N:-1] = 0
    

    # reconstruct with varying number of terms
    rd = ifft(dfshift)

    ax[j][i].plot(day, data, label='Data')
    ax[j][i].plot(day, np.abs(rd), label = ('N=' + str(int(N/2))))
    ax[j][i].legend()
    ax[j][i].grid()
    i += 1
    if i >= 2:
        j = 1
        i = 0

fig.supxlabel("Day (from 1 January 2024)")
fig.supylabel("Temperature (F)")

plt.show()