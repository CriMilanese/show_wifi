import os
import matplotlib.pyplot as plt
import re
import numpy as np
import subprocess
from wifi import *

sh = subprocess.check_output('sudo iwlist wlp2s0 scan | grep -e \'SSID\' -e \'Frequency\' -e \'Quality\'', shell=True)

file = sh.decode("utf-8")
wifi_list = []

#find values
patt_signal = re.findall('level=-[0-9][0-9]', file)
patt_names = re.findall('ESSID:\".*\"', file)
patt_qual = re.findall('[\d][\d]/[\d][\d]', file)
patt_chan = re.findall(' [0-9]+\)', file)

#polish
channels = [int(a[1:-1]) for a in patt_chan]
names = [x[7:10] for x in patt_names if x[7]!='"']
signal = [int(x[-3:]) for x in patt_signal]
quality = [int(patt[:2])/int(patt[3:]) for patt in patt_qual]

for i in range(len(names)):
	if channels[i]<30:
		tmp = Wifi(signal[i], names[i], quality[i], channels[i])
		wifi_list.append(tmp)

plt.scatter([i.strength for i in wifi_list], [i.channel for i in wifi_list], c=[i.quality for i in wifi_list], cmap='RdBu')
clb = plt.colorbar()
clb.set_label('quality', rotation=270)
for wifi in wifi_list:
	plt.annotate(wifi.name, (wifi.strength, wifi.channel), (3,3), textcoords='offset pixels')
	wifi.print_wifi()

plt.xlabel('sig_strength [dB]')
plt.ylabel('channel')
plt.show()
