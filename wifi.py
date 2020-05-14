class Wifi:
    def __init__(self, sig_str, n, qual, chann):
        self.strength = sig_str
        self.name = n
        self.quality = qual
        self.channel = chann

    def print_wifi(self):
        print('\n')
        print('name: ', self.name)
        print('strength: ', self.strength)
        print('quality: ', self.quality)
        print('channel: ', self.channel)
