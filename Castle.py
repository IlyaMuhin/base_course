from Monster import Monster

released_army = {'peasant': 0, 'knight': 0, 'catapult': 0}

class Castle:

    def __init__(self,color):
        self.color = color
        self.hp = 100000
        self.dmg = 0
        self.money = 0
        self.army = {'peasant': 0, 'knight': 0, 'catapult': 0}
        self.army_hp = 0
    
    def create_monster(self,type,kol):
        self.type = type
        self.kol = kol
        self.army[self.type] += self.kol
        self.dmg += Monster(self.type).dmg * self.kol
        self.army_hp += Monster(self.type).hp * self.kol


    def check_stats(self):
        print(f'Ваша армия:{self.army}')
        print(f'Урон вашей армии:{self.dmg}')
        print(f'Здоровье вашей армии:{self.army_hp}')

    def release_army(self,type,kol):
        self.type = type
        self.kol = kol
        if self.army[self.type] >= self.kol:
            released_army[self.type] += self.kol
            self.army[self.type] -= self.kol


        


