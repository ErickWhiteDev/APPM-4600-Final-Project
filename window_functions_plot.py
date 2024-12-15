#! /usr/bin/env python3

from scipy.fft import fft, fftfreq, fftshift
from scipy.signal.windows import blackman, hamming, hann, gaussian
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# setup figure
fig = plt.figure()
gs0 = gridspec.GridSpec(1, 2, figure=fig)
gs00 = gridspec.GridSpecFromSubplotSpec(4, 1, subplot_spec=gs0[1])

ax0 = fig.add_subplot(gs0[0])

N = 1024
x = np.linspace(0, 1, N)

windows = [hamming(N), blackman(N), hann(N), gaussian(N, N/6)]
names = ["Hamming", "Blackman", "Hann", "Gaussian"]
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

axes_right = []
for i in range(len(windows)):
    ax0.plot(x, windows[i], label=names[i] + " Window", color=colors[i])
    # pad window
    window = np.concatenate((np.zeros((10*N)), windows[i], np.zeros((10*N))))

    f = fftshift(fft(window))
    # normalize fft to max
    f /= np.max(f)
    f_x = np.linspace(0,f.size,f.size) - f.size/2
    if i > 0:
        ax_fft = fig.add_subplot(gs00[i], sharex=axes_right[i-1])
    else:
        ax_fft = fig.add_subplot(gs00[i])
    
    if i < len(windows)-1:
        plt.setp(ax_fft.get_xticklabels(), visible=False)
    else:
        ax_fft.set_xlabel("bins\n\n(b)")

    ax_fft.semilogy(f_x, np.abs(f), label=names[i] + " Window", color=colors[i])
    ax_fft.set_xlim(-500, 500)
    ax_fft.set_ylim(1e-6, 5)
    ax_fft.grid()
    ax_fft.legend()

    axes_right.append(ax_fft)



ax0.grid()
ax0.legend()
ax0.set_xlabel("n/N\n\n(a)")
ax0.set_ylabel("g(n)")
plt.show()
