import random   # A remplacer par la lecture réel de valeur plus tard

class PhotodiodeSensor:
    def __init__(self, channel=0):
        self.channel = channel

    def read(self):
        # simule une lecture analogique
        return random.uniform(0.0,3.3)

