import numpy as np
from scipy.signal import ShortTimeFFT
from scipy.signal.windows import *
from matplotlib import pyplot as plt
from spacepy import pycdf

from set_vis_params import set_vis_params

data_file = pycdf.CDF("data/rbsp-a_magnetometer_uvw_emfisis-L2_20140227_v1.6.1_trimmed")

magnitude = data_file["Magnitude"][:]

N = len(magnitude)

n = int(4096)

win = hamming(2 * n)
hop = n
fs = 64
mfft = 2 * n

STFT = ShortTimeFFT(win, hop, fs, mfft=mfft, scale_to='magnitude')

S = STFT.spectrogram(magnitude)
S_dB = 10 * np.log10(np.fmax(S, 1E-5))

set_vis_params()

spectrogram = plt.figure()
ax = spectrogram.add_subplot(1, 1, 1)

ax.imshow(S_dB, origin='lower', aspect='auto', cmap='Greys_r', extent=STFT.extent(N))

ax.set_xlabel('Time [h]')
ax.set_xticks(np.arange(0, 7 * 3600, 3600), np.arange(16, 23, 1))
ax.set_ylabel('Frequency [Hz]')

ax.set_ylim(0.1, 10)

ax.set_yscale('log')

plt.show()
