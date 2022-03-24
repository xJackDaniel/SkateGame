class Player:
    def __init__(self, hearts, skin, best_score, current_score):
        self.hearts = hearts
        self.skin = skin
        self.best_score = best_score
        self.current_score = current_score

    def get_hearts(self):
        return self.hearts

    def get_skin(self):
        return self.skin

    def get_best_score(self):
        return self.best_score

    def get_currect_score(self):
        return  self.currect_score

    def add_score(self):
        self.score += 1

    def set_best_score(self):
        pass