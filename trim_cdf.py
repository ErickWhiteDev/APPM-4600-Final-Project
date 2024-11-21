import os

from spacepy import pycdf

if os.path.exists("data/rbsp-a_magnetometer_uvw_emfisis-L2_20140227_v1.6.1_trimmed.cdf"):
    os.remove("data/rbsp-a_magnetometer_uvw_emfisis-L2_20140227_v1.6.1_trimmed.cdf")

untrimmed_data = pycdf.CDF("data/rbsp-a_magnetometer_uvw_emfisis-L2_20140227_v1.6.1.cdf")

time = untrimmed_data["Epoch"][:]
magnitude = untrimmed_data["Magnitude"][:]

filter = [time[i].hour >= 16 and time[i].hour <= 21 for i in range(len(time))]

time_filtered = time[filter]
magnitude_filtered = magnitude[filter]

trimmed_data = pycdf.CDF("data/rbsp-a_magnetometer_uvw_emfisis-L2_20140227_v1.6.1_trimmed.cdf", "")

trimmed_data["Epoch"] = time_filtered
trimmed_data["Magnitude"] = magnitude_filtered

untrimmed_data.close()
trimmed_data.close()
