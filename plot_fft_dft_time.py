import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import time
from scipy.fft import fft, fftfreq

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

def driver():
    pts = np.arange(5, 26)
    pts = 2**pts

    fit = np.array([1.74747037, -15.09890991])

    dft_times = np.zeros(len(pts))
    fft_times = np.zeros(len(pts))
    for i in range(pts.size):
        n = pts[i]
        f = np.random.rand(n)

        if n < 16384:
            dft_start = time.time()
            dft_time = DFT(f)
            dft_end = time.time()
            dft_times[i] = dft_end - dft_start
        else:
            dft_times[i] = np.exp(np.polyval(fit, np.log(n)))

        fft_start = time.time()
        fft_time = fft(f)
        fft_end = time.time()

        fft_times[i] = fft_end - fft_start
    
    ax = plt.gca()
    plt.scatter(pts[:10], dft_times[:10], color='tab:blue', label="DFT (measured)")
    plt.scatter(pts[10:], dft_times[10:], color='tab:blue', fc='none', label="DFT (extrapolated)")
    plt.scatter(pts, fft_times, color='tab:orange', label="FFT")
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.xlabel("Sample points")
    plt.ylabel("Time (s)")

    plt.legend()
    plt.grid()
    plt.title("Time Comparison of direct DFT vs FFT")
    plt.show()

def DFT(f):

    N = len(f)
    n = np.arange(N)
    k = []
    for i in n:
        k.append([i])
        
    k = np.array(k)
    
    exponential = np.exp(-2j * np.pi * k * n / N)
    
    res = np.dot(exponential, f)
    return res

driver()