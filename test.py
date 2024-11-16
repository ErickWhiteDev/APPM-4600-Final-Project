import numpy as np
from scipy.signal import ShortTimeFFT
from scipy.signal.windows import *

from matplotlib import pyplot as plt
from matplotlib import dates as mdates

from spacepy import pycdf

data_file = pycdf.CDF("data/rbsp-a_magnetometer_uvw_emfisis-L2_20140227_v1.6.1")

magnitude = data_file["Magnitude"][:]
# time = data_file["Epoch"][0:100]

win = hamming(512)
hop = 256
fs = 64
mfft = 512

STFT = ShortTimeFFT(win, hop, fs, mfft=mfft, scale_to='magnitude')

S = STFT.stft(magnitude)

# spectrogram = plt.figure()
# ax = spectrogram.add_subplot(1, 1, 1)

# ax.imshow(abs(S), origin='lower', aspect='auto', cmap='viridis')

spectrogram, ax = plt.subplots()

Pxx, freqs, bins, im = ax.specgram(magnitude - np.mean(magnitude), NFFT=2056, Fs=fs, cmap='Grays')

bins_hours = bins / 3600

ax.set_xlabel('Time (hours)')
ax.set_xticks(np.arange(0, 86400, 3600), np.arange(0, np.max(bins_hours), 1))

ax.set_xlim(16 * 3600, 22 * 3600)
ax.set_ylim(0.1, 10)

ax.set_yscale('log')

plt.show()
