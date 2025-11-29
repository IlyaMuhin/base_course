from Monster import Monster


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
        self.army[self.type] += self.kol
        self.dmg += Monster(self.type).dmg * self.kol


    def check_stats(self):
        print(f'Ваша армия:{self.army}')
        print(f'Урон вашей армии:{self.dmg}')
        


my_castle = Castle('green')
my_castle.create_monster('peasant', 5)
my_castle.create_monster('knight', 4)
my_castle.create_monster('catapult',2)
my_castle.check_stats()