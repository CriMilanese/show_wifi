class Wifi:
    def __init__(self, sig_str, n, qual, chann):
        self.signal = int(sig_str)
        self.name = n
        self.rate = int(qual)
        self.channel = int(chann)

    def print_wifi(self):
        print('\n')
        print('name: ', self.name)
        print('signal: ', self.signal)
        print('quality: ', self.rate)
        print('channel: ', self.channel)
