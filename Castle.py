from Monster import Monster

released_army = {'peasant': 0, 'knight': 0, 'catapult': 0}

castle_list = {}



class Castle:

    def __init__(self,color):
        self.color = color
        self.hp = 100000
        self.dmg = 0
        self.money = 0
        self.army = {'peasant': 0, 'knight': 0, 'catapult': 0}
        self.army_hp = 0
        castle_list[self.color] = self



    def create_monster(self,type,kol):
        self.type = type
        self.kol = kol
        self.army[self.type] += self.kol
        self.dmg += Monster(self.type).dmg * self.kol
        self.army_hp += Monster(self.type).hp * self.kol


    def check_stats(self):
        print(f'''
              =======================================================
              |          Замок
              =======================================================
              |Здоровье вашего замка:{self.hp}
              =======================================================
              |    Армия замка
              =======================================================
              |Ваша армия:{self.army}            
              |Урон вашей армии:{self.dmg}
              |Здоровье вашей армии:{self.army_hp}
              =======================================================






                              ''')

    def release_army(self,type1,kol1):
        self.type1 = type1
        self.kol1 = kol1
        if self.army[self.type1] >= self.kol1:
            released_army[self.type1] += self.kol1
            self.army[self.type1] -= self.kol1
            self.army_hp -= Monster(self.type1).hp * self.kol1
            self.dmg -= Monster(self.type1).dmg * self.kol1
        else:
            print('У вас недостаточно воинов!')

# red_castle = Castle('red')       


