import numpy as np
from scipy.fft import rfft, rfftfreq
from scipy.signal import ShortTimeFFT
from scipy.signal.windows import *
from matplotlib import pyplot as plt

from set_vis_params import set_vis_params

T, N = 0.01, 1000
t = np.arange(N) * T
x = np.sin(5 * np.pi * t ** 2)

win = gaussian(51, std=10, sym=True)

FFT = rfft(x)
XFFT = rfftfreq(N, T)

STFT = ShortTimeFFT(win, hop=5, fs=1/T, mfft=500, scale_to='magnitude')

S = STFT.spectrogram(x)

set_vis_params()
plt.rcParams['font.size'] = 24

STFT_fig, STFT_ax = plt.subplots()

STFT_im = STFT_ax.imshow(S, origin='lower', aspect='auto', cmap='Greys_r', extent=STFT.extent(N))

STFT_fig.colorbar(STFT_im, label='FFT Magnitude')

STFT_ax.set_xlabel('Time [s]')
STFT_ax.set_ylabel('Frequency [Hz]')

STFT_ax.set_title('Spectrogram of $f(t) = \\sin(5\\pi t^2)$')

FFT_fig, FFT_ax = plt.subplots()

FFT_ax.plot(XFFT, np.abs(FFT))

FFT_ax.set_xlabel('Frequency [Hz]')
FFT_ax.set_ylabel('FFT Magnitude')

FFT_ax.set_title('FFT of $f(t) = \\sin(5\\pi t^2)$')

plt.show()
