from helpers import screen


class Player:
    def __init__(self, hearts, skin, best_score, current_score, x, y):
        self.hearts = hearts
        self.skin = skin
        self.best_score = best_score
        self.current_score = current_score
        self.x = x
        self.y = y

    def get_hearts(self):
        return self.hearts

    def get_skin(self):
        return self.skin

    def get_best_score(self):
        return self.best_score

    def get_current_score(self):
        return self.currect_score

    def add_score(self):
        pass

    def set_best_score(self):
        pass