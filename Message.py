import utime


class Message:
    def __init__(self, screen):
        self.screen = screen
    def displayMessage(self, message):
        self.screen.showMessage(message)

    def showUnreadMessage(self):
        self.screen.showUnreadMessage()

    def receivedMessage(self, message):
        print(message)
    def displayinDefinitelyMessage(self, message):
        while True:
            self.screen.showMessage(message)
            utime.sleep(1)