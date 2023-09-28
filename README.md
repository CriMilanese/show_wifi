### WHY
To verify and test existing wireless networks in the area and show an infographic
of their status, including channel, rate and quality. The users might find interesting
to assess that wireless signals from routers closer to their own aren't as close in
channel, hence frequency, to avoid interference of any sort.

### WHAT
A tool written for **python3** with the help and therefore the dependency of `numpy` and `matplotlib`. Furthermore, the script relies on the shell command `nmcli`, to be easily found for all platforms, that allows quite [some tricks](https://www.techrepublic.com/article/how-to-use-the-nmcli-command-to-gather-network-device-information-on-linux/).

### HOW 
just run `python3 stats.py`

### update Oct23
Some error occurs that were not there at last testing, plot throws an error for incomparable values.

Solved - the script was messed, it seems I was attempting to update the values in real-time
to get a better approximation because at the time of reading, a single value could be an outlier in the spectrum of signal's amplitudes that could have reached my antenna.
