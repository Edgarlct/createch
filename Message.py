class Message:
    def __init__(self, screen):
        self.screen = screen
    def displayMessage(self, message):
        print(message)
        self.screen.showMessage(message)