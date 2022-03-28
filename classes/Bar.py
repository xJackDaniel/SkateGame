class Bar:
    def __init__(self, type, height, width, jump):
        self.type = type
        self.height = height
        self.width = width
        self.jump = jump

    def get_type(self):
        """Returns the bar's type"""
        return self.type

    def get_height(self):
        """Returns the bar's height"""
        return self.height

    def get_width(self):
        """Returns the bar's width"""
        return self.width

    def get_jump(self):
        """Returns True/False if the player needs to jump over the bar"""
        return self.jump
