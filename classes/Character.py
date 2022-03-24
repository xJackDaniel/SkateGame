class Character:
    def __init__(self, id, price, image, name):
        self.id = id
        self.price = price
        self.image = image
        self.name = name

    def get_id(self):
        return self.id

    def get_price(self):
        return self.price

    def get_iamge_url(self):
        return self.get_iamge

    def get_name(self):
        return self.name

    def is_own(self):
        pass