import math
from Castle import Castle, released_army
from Monster import Monster
from NPC import *
class Hero:
    def __init__(self,color):
        self.color = color
        self.hp = 6000
        self.dmg =100
        self.army = {'peasant': 0, 'knight': 0, 'catapult': 0}
        self.army_dmg = 0
        self.army_hp = 0


    def check_stats(self):
        print(f'Здоровье вашего героя:{self.hp}')
        print(f'Урон вашего героя:{self.dmg}')
        print(f'Армия вашего героя:{self.army}')
        print(f'Урон армии героя:{self.army_dmg}')
        print(f'Здоровье армии героя:{self.army_hp}')
        print(f'Общий урон:{self.dmg + self.army_dmg}')


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
    

    def attack_npc(self,type):
        self.type = type
        if self.hp > 0:
            npc_list[self.type].hp -= (self.army_dmg + self.dmg)
            self.army_hp -= npc_list[self.type].dmg
            self.army['peasant'] -= (math.floor(npc_list[self.type].dmg / Monster('peasant').hp))
            if self.army['peasant'] < 0:
                self.army['knight'] += (math.floor((self.army['peasant'] * Monster('peasant').hp) / Monster('knight').hp))
                self.army['peasant'] = 0
            if self.army['knight'] < 0:
                self.army['catapult'] += (math.floor((self.army['knight'] * Monster('knight').hp) / Monster('catapult').hp))
                self.army['knight'] = 0 
            if self.army['catapult'] < 0:
                self.army['catapult'] = 0          
            if self.army_hp <= 0:
                self.hp += self.army_hp
                self.army_hp = 0
            if self.hp <= 0 and npc_list[self.type].hp > 0:
                self.hp = 0
                print('Вы проиграли!')
                print(f'У npc осталось {npc_list[self.type].hp} hp')
            elif npc_list[self.type].hp <= 0 and self.hp > 0:
                npc_list[self.type].hp = NPC(self.type).hp
                print('Вы выиграли!')
                self.check_stats()
            elif npc_list[self.type].hp <= 0 and self.hp <= 0:
                print('Все погибли!')
                self.hp = 0
                npc_list[self.type].hp = NPC(self.type).hp
            else:
                print('Бой закончился ничьёй!')
                self.check_stats()
                print(f'У npc осталось {npc_list[self.type].hp} hp') 
               
        else:
            print('У вас нет героя!')


        
my_castle = Castle('green')
my_castle.create_monster('peasant', 5)
my_castle.create_monster('knight', 4)
my_castle.create_monster('catapult',2)
my_hero = Hero('green')
my_castle.release_army('peasant',4)
my_castle.release_army('knight', 3)
my_castle.release_army('catapult',1)
my_hero.take_army()
my_hero.check_stats()
npc_stats()
my_hero.attack_npc('goblin')
my_hero.attack_npc('goblin')
npc_stats()