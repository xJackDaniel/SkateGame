class Button:
    def __init__(self, style, screen, text, id):
        self.style = style
        self.screen = screen
        self.text = text
        self.id = id


    def get_style(self):
        return self.style

    def get_screen(self):
        return self.screen

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id
