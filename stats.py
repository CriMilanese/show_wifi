import os
import sys
import matplotlib.pyplot as plt
import re
import numpy as np
from subprocess import check_output, Popen
from wifi import *
import mplcursors as mc

def channel_sort(self):
	return self.signal;

def harvest_wifi_data():
	sh = check_output('nmcli dev wifi', shell=True)
	file = sh.decode("utf-8")

	with open('nmcli_log.txt', 'w') as handle:
		handle.write(file)

	#find values
	patt_chan = re.findall('Infra\s+[0-9]+', file)
	patt_names = re.findall(':[A-Z0-9][A-Z0-9]\s+[A-Za-z0-9\._-]+', file)
	patt_signal = re.findall('bit/s.+[0-9][0-9][0-9]*', file)
	patt_qual = re.findall('[\d][\d][\d]*\sMb', file)
	wifi_list = [sys.getsizeof(Wifi)] * len(patt_signal);

	#polish
	channels = [a[-2:] for a in patt_chan]
	names = [x[5:8] for x in patt_names]
	signal = [(x[-2:]) for x in patt_signal]
	rate = [patt[0:3] for patt in patt_qual]


	for i in range(len(patt_chan)):
		if int(channels[i])<50:
			wifi_list[len(patt_chan)-i-1] = Wifi(signal[i], names[i], rate[i], channels[i])

	# sort them by channel
	wifi_list.sort(key=channel_sort)
	fig = plt.gcf()
	plt.scatter([i.channel for i in wifi_list], [i.signal for i in wifi_list], c=[i.rate for i in wifi_list], cmap='RdBu')

	plt.get_current_fig_manager().set_window_title('WiFi signals around you')
	clb = plt.colorbar()
	clb.set_label('rate [Mb/s]', rotation=270)
	for wifi in wifi_list:
		plt.annotate(wifi.name, (wifi.channel, wifi.signal), (3,3), textcoords='offset pixels')

  # give extra info on hover
	mc.cursor(hover=True)
	plt.ylabel('sig_strength [dB]')
	plt.xlabel('channel')
	plt.show()

harvest_wifi_data()
