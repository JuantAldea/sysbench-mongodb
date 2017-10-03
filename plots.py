#!/usr/bin/python

import glob
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pprint import pprint as pp
import re
header = []
files = {}

input_files = glob.glob(sys.argv[1] + "/*/*/*"+ sys.argv[2] + "*tsv")
pp(input_files)

with open(input_files[0]) as f:
	header = f.readline().split()

dtype1 = np.dtype([(name,float) for name in header])

for p in input_files:
	print("reading " + p)
	f = open(p)
	dtype1 = np.dtype([(name, float) for name in f.readline().split()])	
	f.close()
	files[p] = np.loadtxt(p, dtype=dtype1, skiprows=1)

handles = []
axis_labels = []

n_plots = 3 if input_files[0].find("Load") != -1 else 2

f, axarr = plt.subplots(n_plots, sharex=True)
for f in files:
	frame = files[f]
	pp(frame)
	handle = 0
	
	if f.find("Load") != -1:
		handle1, = axarr[0].plot(frame['elap_secs'], frame['tot_inserts'], label = f)
		handle1, = axarr[1].plot(frame['elap_secs'], frame['int_ips'], label = f)
		handle1, = axarr[2].plot(frame['elap_secs'], frame['cum_ips'], label = f)
		axarr[0].set_title('total inserts per second')
		axarr[1].set_title('interval inserts per second')
		axarr[2].set_title('average inserts per second')
		handles.append(handle1)
	else:
		handle1, = axarr[0].plot(frame['elap_secs'], frame['cum_tps'], label = f)
		handle1, = axarr[1].plot(frame['elap_secs'], frame['int_tps'], label = f)
		axarr[0].set_title('total transactions per second')
		axarr[1].set_title('interval transacions per second')
		handles.append(handle1)

plt.legend(handles=handles)
plt.show()
