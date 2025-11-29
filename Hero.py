from Castle import Castle, released_army
from Monster import Monster
class Hero:
    def __init__(self,color):
        self.color = color
        self.hp = 1000
        self.dmg = 1000
        self.army = {'peasant': 0, 'knight': 0, 'catapult': 0}
        self.army_dmg = 0
        self.army_hp = 0


    def check_stats(self):
        print(f'Армия вашего героя:{self.army}')
        print(f'Урон армии героя:{self.dmg}')
        print(f'Здоровье армии героя:{self.army_hp}')


    def take_army(self):        
        self.army['peasant'] += released_army['peasant']
        self.army_dmg += Monster('peasant').dmg * released_army['peasant']
        self.army_hp += Monster('peasant').hp * released_army['peasant']
        released_army['peasant'] = 0

        self.army['knight'] += released_army['knight']
        self.army_dmg += Monster('knight').dmg * released_army['knight']
        self.army_hp += Monster('knight').hp * released_army['knight']
        released_army['knight'] = 0

        self.army['catapult'] += released_army['catapult']
        self.army_dmg += Monster('catapult').dmg * released_army['catapult']
        self.army_hp += Monster('catapult').hp * released_army['catapult']
        released_army['catapult'] = 0


        
my_castle = Castle('green')
my_castle.create_monster('peasant', 5)
my_castle.create_monster('knight', 4)
my_castle.create_monster('catapult',2)
my_castle.check_stats()
my_hero = Hero('green')
my_castle.release_army('peasant',5)
my_castle.release_army('knight', 4)
my_castle.release_army('catapult',2)
print(released_army)
my_hero.take_army()
my_castle.check_stats()
my_hero.check_stats()