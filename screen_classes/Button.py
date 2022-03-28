class Button:
    def __init__(self, style, screen, text, id):
        self.style = style
        self.screen = screen
        self.text = text
        self.id = id


    def get_style(self):
        """Returns the button's style"""
        return self.style

    def get_screen(self):
        """Returns the screen to which the button moves"""
        return self.screen

    def get_text(self):
        """Returns the text on the button"""
        return self.text

    def get_id(self):
        """Returns the button's id"""
        return self.id
