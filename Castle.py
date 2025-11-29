import Monster.py
class Castle:

    def __init__(self,color):
        self.color = color
        self.hp = 100000
        self.dmg = 0
        self.money = 0
        self.army = {'peasant': 0, 'knight': 0, 'catapult': 0}
    
    def create_monster(self,type,kol):
        self.type = type
        self.kol = kol
        self.army[type] += kol

        


my_castle = Castle('green')
my_castle.create_monster('peasant', 5)