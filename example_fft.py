import numpy as np
from scipy.fft import rfft, rfftfreq
from matplotlib import pyplot as plt
from spacepy import pycdf

from set_vis_params import set_vis_params

data_file = pycdf.CDF("data/rbsp-a_magnetometer_uvw_emfisis-L2_20140227_v1.6.1_trimmed")

magnitude = data_file["Magnitude"][:]

N = magnitude.size
fs = 64

f = rfft(magnitude)
xf = rfftfreq(N, 1 / fs)

set_vis_params()

fft_plot, ax = plt.subplots()

ax.semilogy(xf, np.abs(f))

ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Magnetic Field Intensity [nT]')

ax.set_xlim(0, fs / 2)

plt.show()
