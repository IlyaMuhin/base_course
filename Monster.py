class Monster:
    def __init__(self, type):
        self.type = type
        if self.type == 'peasant':
            self.hp = 50
            self.dmg = 25
            self.price = 25
        elif self.type == 'knight':
            self.hp = 75
            self.dmg = 30
            self.price = 40
        elif self.type == 'catapult':
            self.hp = 600
            self.dmg = 400
            self.price = 2500

