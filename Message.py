import utime


class Message:
    def __init__(self, screen):
        self.screen = screen
    def displayMessage(self, message):
        self.screen.showMessage(message)

    def showUnreadMessage(self, button):
        self.screen.showUnreadMessage(button)

    def receivedMessage(self, message):
        print(message)
    def displayinDefinitelyMessage(self, message):
        while True:
            self.screen.showMessage(message)
            utime.sleep(1)