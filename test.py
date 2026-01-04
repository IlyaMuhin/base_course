import math
import time
from Player import *
from Castle import *
from Monster import Monster
from NPC import *


def attack_npc(self,type):
        print(f'{self.color}:')
        self.type = type
        if self.hp > 0:
            while self.hp != 0 or self.type.hp != 0:
                print(f'''{self.hp} vs {self.type.hp}
                          {self.dmg} vs {self.type.dmg}


                                     ''')
                self.type.hp -= (self.army_dmg + self.dmg)
                self.army_hp -= self.type.dmg
                self.army['peasant'] -= (math.floor(self.type.dmg / Monster('peasant').hp))
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
                time.sleep(0.5)
                
            if self.hp <= 0 and self.type.hp > 0:
                self.hp = 0
                print('Вы проиграли!')
                print(f'У npc осталось {self.type.hp} hp')
            elif self.type.hp <= 0 and self.hp > 0:
                self.type.hp = NPC(self.type).hp
                print(f'Вы выиграли!')
            elif self.type.hp <= 0 and self.hp <= 0:
                print('Все погибли!')
                self.hp = 0
                self.type.hp = NPC(self.type).hp
 
                
        else:
            print(f'У вас нет героя!')

attack_npc('volves')