import math
from Player import *
from Castle import *
from Monster import Monster
from NPC import *


hero_list = {}



class Hero:
    def __init__(self,color = ""):
        self.color = color
        self.hp = 6000
        self.dmg =100
        self.army = {'peasant': 0, 'knight': 0, 'catapult': 0}
        self.army_dmg = 0
        self.army_hp = 0
        hero_list[self.color] = self

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
            self.army_dmg = Monster('peasant').dmg * self.army['peasant']
            self.army_dmg += Monster('knight').dmg * self.army['knight'] 
            self.army_dmg += Monster('catapult').dmg * self.army['catapult']          
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
            elif npc_list[self.type].hp <= 0 and self.hp <= 0:
                print('Все погибли!')
                self.hp = 0
                npc_list[self.type].hp = NPC(self.type).hp
            else:
                print('Бой закончился ничьёй!')
                print(f'У npc осталось {npc_list[self.type].hp} hp') 
               
        else:
            print('У вас нет героя!')
    



    def attack_player(self, player_color):
        self.player_color = player_color
        if self.hp > 0:
            castle_list[self.player_color].army_hp -= (self.dmg + self.army_dmg)
            if castle_list[self.player_color].army_hp < 0:
                castle_list[self.player_color].hp += castle_list[self.player_color].army_hp
                castle_list[self.player_color].army_hp = 0
            
            self.army_hp -= castle_list[self.player_color].dmg

            self.army['peasant'] -= (math.floor(castle_list[self.player_color].dmg / Monster('peasant').hp))
            if self.army['peasant'] < 0:
                self.army['knight'] += (math.floor((self.army['peasant'] * Monster('peasant').hp) / Monster('knight').hp))
                self.army['peasant'] = 0
            if self.army['knight'] < 0:
                self.army['catapult'] += (math.floor((self.army['knight'] * Monster('knight').hp) / Monster('catapult').hp))
                self.army['knight'] = 0 
            if self.army['catapult'] < 0:
                self.army['catapult'] = 0


            castle_list[self.player_color].army['peasant'] -= (math.floor((self.dmg + self.army_dmg) / Monster('peasant').hp))
            if castle_list[self.player_color].army['peasant'] < 0:
                castle_list[self.player_color].army['knight'] += (math.floor((castle_list[self.player_color].army['peasant'] * Monster('peasant').hp) / Monster('knight').hp))
                castle_list[self.player_color].army['peasant'] = 0
            if castle_list[self.player_color].army['knight'] < 0:
                castle_list[self.player_color].army['catapult'] += (math.floor((castle_list[self.player_color].army['knight'] * Monster('knight').hp) / Monster('catapult').hp))
                castle_list[self.player_color].army['knight'] = 0 
            if castle_list[self.player_color].army['catapult'] < 0:
                castle_list[self.player_color].army['catapult'] = 0

            
            self.army_dmg = Monster('peasant').dmg * self.army['peasant']
            self.army_dmg += Monster('knight').dmg * self.army['knight'] 
            self.army_dmg += Monster('catapult').dmg * self.army['catapult'] 


            castle_list[self.player_color].dmg = Monster('peasant').dmg * castle_list[self.player_color].army['peasant']
            castle_list[self.player_color].dmg += Monster('knight').dmg * castle_list[self.player_color].army['knight'] 
            castle_list[self.player_color].dmg += Monster('catapult').dmg * castle_list[self.player_color].army['catapult'] 



            if self.army_hp <= 0:
                self.hp += self.army_hp
                self.army_hp = 0
            if self.hp <= 0 and castle_list[self.player_color].hp > 0:
                self.hp = 0
                print('Вы проиграли!')
                print(f'У замка игрока осталось {castle_list[self.player_color].hp} hp')
            elif castle_list[self.player_color].hp <= 0 and self.hp > 0:
                castle_list[self.player_color].hp = 0
                print('Вы выиграли!')
                print(f'Игрок цвета {self.player_color} выбывает!')
                hero_list[self.player_color].hp = -1
                del players_list[self.player_color]
            elif castle_list[self.player_color].hp <= 0 and self.hp <= 0:
                print('Все погибли!')
                self.hp = 0
                castle_list[self.player_color].hp = 0
            else:
                print('Вам не удалось разрушить замок')
                print(f'У замка игрока осталось {castle_list[self.player_color].hp} hp')
        else:
            print('У вас нет героя!')

        
# my_castle = Castle('green')
# my_castle.create_monster('peasant', 5)
# my_castle.create_monster('knight', 4)
# my_castle.create_monster('catapult',2)
# my_hero = Hero('green')
# my_castle.release_army('peasant',4)
# my_castle.release_army('knight', 3)
# my_castle.release_army('catapult',1)
# my_hero.take_army()
# my_hero.check_stats()
# npc_stats()
# my_hero.attack_npc('goblin')
# my_hero.attack_npc('goblin')
# npc_stats()

# a = Player('red')
# b = Player('green')
# a_castle = Castle('red')
# b_castle = Castle('green')
# b_hero = Hero('green')
# a_hero = Hero('red')
# b_castle.create_monster('catapult', 20)
# a_castle.create_monster('catapult', 1000)
# a_castle.release_army('catapult', 1000)
# a_hero.take_army()
# print(b_castle.army)
# # a_hero.check_stats()
# # b_castle.check_stats()
# # print(castle_list)
# a_hero.attack_player('green')
# print(b_castle.army)
# b.check_stats()
# # a.check_stats()
# # a_hero.check_stats()
# # b_castle.check_stats()
# a_hero.attack_player('green')