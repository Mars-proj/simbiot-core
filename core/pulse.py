import time

class Pulse:
    def __init__(self):
        self.alive = True

    def start(self):
        while self.alive:
            time.sleep(1)
