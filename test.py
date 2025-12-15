from Hero import *


print(f''' 
         =====================================================================
         |Герой                           |   Армия                          |
         =====================================================================
         |Здоровье вашего героя:{self.hp}|Армия вашего героя:{self.army}     |
         |Урон вашего героя:{self.dmg}   |Урон армии героя:{self.army_dmg}   |
         |                               |Здоровье армии героя:{self.army_hp}|
         ===================================================================== 
         |                 Общий урон:{self.dmg + self.army_dmg}             |
         =====================================================================

              ''')





print(f'Здоровье вашего героя:{self.hp}')
        print(f'Урон вашего героя:{self.dmg}')
        print(f'Армия вашего героя:{self.army}')
        print(f'Урон армии героя:{self.army_dmg}')
        print(f'Здоровье армии героя:{self.army_hp}')
        print(f'Общий урон:{self.dmg + self.army_dmg}')


  print(f'Здоровье вашего замка:{self.hp}')
        print(f'Ваша армия:{self.army}')
        print(f'Урон вашей армии:{self.dmg}')
        print(f'Здоровье вашей армии:{self.army_hp}')




        if self.type == "volves":
            self.hp = 250
            self.dmg = 225
            self.price = 375
        elif self.type == "goblin":
            self.hp = 1500
            self.dmg = 2000
            self.price = 1000
        elif self.type == "giant":
            self.hp = 6000
            self.dmg = 6000
            self.price = 2500
        elif self.type == "dragon":
            self.hp = 45000
            self.dmg = 15000
            self.price = 8000