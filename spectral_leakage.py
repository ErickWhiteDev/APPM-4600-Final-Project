# from scipy.fft import fft, fftfreq

# import numpy as np

# # Number of sample points

# N = 600

# # sample spacing

# T = 1.0 / 600.0

# x = np.linspace(0.0, N*T, N, endpoint=False)

# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)


# yf = fft(y)

# from scipy.signal.windows import blackman, gaussian, hamming

# w = blackman(N)
# # w2 = hamming(N)
# # w3 = gaussian(N, .1)

# ywf = fft(y*w)
# # yw2f = fft(y*w2)
# # yw3f = fft(y*w3)

# xf = fftfreq(N, T)[:N//2]


# import matplotlib.pyplot as plt

# plt.semilogy(xf[1:N//2], 2.0/N * np.abs(yf[1:N//2]), 'tab:red')
# plt.semilogy(xf[1:N//2], 2.0/N * np.abs(ywf[1:N//2]), 'tab:blue')
# # plt.semilogy(xf[1:N//2], 2.0/N * np.abs(yw2f[1:N//2]), 'tab:orange')
# # plt.semilogy(xf[1:N//2], 2.0/N * np.abs(yw3f[1:N//2]), 'tab:purple')


# plt.legend(['FFT', 'FFT w. window'])

# plt.grid()

# plt.show()


from scipy.fft import fft, fftfreq

import numpy as np

# Number of sample points

N = 600

# sample spacing

T = 1.0 / 800.0

x = np.linspace(0.0, N*T, N, endpoint=False)

y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(200.0 * 2.0*np.pi*x)

yf = fft(y)

from scipy.signal.windows import blackman, hamming

w = blackman(N)
ywf = fft(y*w)

w2 = hamming(N)
yw2f = fft(y*w2)

xf = fftfreq(N, T)[:N//2]



import matplotlib.pyplot as plt

plt.semilogy(xf[1:N//2], 2.0/N * np.abs(yf[1:N//2]), 'tab:red')

plt.semilogy(xf[1:N//2], 2.0/N * np.abs(ywf[1:N//2]), 'tab:blue')

plt.semilogy(xf[1:N//2], 2.0/N * np.abs(yw2f[1:N//2]), 'tab:green')

plt.legend(['No Window', 'Blackman Window', 'Hamming Window'])

plt.xlabel("Frequency")
plt.ylabel("Amplitude")

plt.grid()

plt.show()