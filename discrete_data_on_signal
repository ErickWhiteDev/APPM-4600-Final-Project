import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams.update({'font.size': 14})
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


sampling_rate = 50   
duration = 2         
frequency = 5        

t_continuous = np.linspace(0, duration, 1000)  
t_discrete = np.linspace(0, duration, sampling_rate)

signal_continuous = 2*np.sin(2 * np.pi * t_continuous) + 3*np.sin(6 * np.pi * t_continuous) + np.sin(11 * np.pi * t_continuous)
signal_discrete = 2*np.sin(2 * np.pi * t_discrete) + 3*np.sin(6 * np.pi * t_discrete) + np.sin(11 * np.pi * t_discrete)



plt.plot(t_continuous, signal_continuous, color='tab:blue')


plt.scatter(t_discrete, signal_discrete, color='r', zorder=5)

# Annotate the discrete sample points
# for i, txt in enumerate(t_discrete):
#     plt.annotate(f'{txt:.2f}s', (t_discrete[i], signal_discrete[i]), 
#                  textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)


plt.title('Discrete Sampling of Continuous Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()