class Character:
    def __init__(self, id, price, image, name):
        self.id = id
        self.price = price
        self.image = image
        self.name = name

    def get_id(self):
        """Returns the id of the character"""
        return self.id

    def get_price(self):
        """Returns the price for the character"""
        return self.price

    def get_iamge_url(self):
        """Returns the image_url of the character"""
        return self.image

    def get_name(self):
        """Returns the name of the character"""
        return self.name

    def is_own(self):
        """Return True/False if the player owns this character."""
        pass