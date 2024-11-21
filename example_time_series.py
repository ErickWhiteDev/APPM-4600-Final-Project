import datetime

import numpy as np
from matplotlib import pyplot as plt
from spacepy import pycdf

from set_vis_params import set_vis_params

data_file = pycdf.CDF("data/rbsp-a_magnetometer_uvw_emfisis-L2_20140227_v1.6.1_trimmed")

magnitude = data_file["Magnitude"][:]
time = data_file["Epoch"][:]

set_vis_params()

time_series, ax = plt.subplots()

ax.plot(time, magnitude)

ax.set_xlabel('Time [h]')
ax.set_xticks(np.linspace(datetime.datetime(2014, 2, 27, 16, 0, 0, 0), datetime.datetime(2014, 2, 27, 22, 0, 0, 0), 7), np.arange(16, 23, 1))
ax.set_ylabel('Magnetic Field Strength [nT]')

ax.set_xlim([datetime.datetime(2014, 2, 27, 16, 0, 0, 0), datetime.datetime(2014, 2, 27, 22, 0, 0, 0)])
ax.set_ylim(0, 1000)

plt.show()
