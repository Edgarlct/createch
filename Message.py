import utime


class Message:
    def __init__(self, screen):
        self.screen = screen
    def displayMessage(self, message):
        print(message)
        self.screen.showMessage(message)
    def displayinDefinitelyMessage(self, message):
        while True:
            self.screen.showMessage(message)
            utime.sleep(1)