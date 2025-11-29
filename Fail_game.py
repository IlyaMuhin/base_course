color_list = {1:'Красный',2:'Желтый',3:'Зеленый',4:'Синий'}
warriors_list = {1:"Human", 2:"Knight", 3:"Catapult"}
d_hum = 0
s_hum = 0
class Warrior:
    def __init__(self,type, index):
        self.type = type
        self.index = index
        if self.type == "Human":
            self.hp = 50
            self.dmg = 25
            self.price = 25
        elif self.type == "Knight":
            self.hp = 75
            self.dmg = 30
            self.price = 40
        elif self.type == "Catapult":
            self.hp = 600
            self.dmg = 400
            self.price = 2500



class NPC:
    def __init__(self, type):
        self.type = type
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
    
volves = NPC('volf')
goblin = NPC('goblin')
giant = NPC('giant')
dragon = NPC('dragon')

        



class Castle:
    def __init__(self,index):
        self.index = index
        self.hp = 100000
        self.money = 100000
        self.army = {}
        self.human_kol = 0
        self.knight_kol = 0
        self.catapult_kol = 0
        self.army_dmg = 0
        self.army_hp = 0
        
    def buy_army(self):
        while True:
            print(f'Ваши деньги:{self.money}')
            self.choice = int(input(f"Кого вы хотите купить?:{warriors_list}:\n"))
            if self.choice == 0:
                break
            if self.choice == 1:
                self.kol = int(input('Скоко?:'))
                if self.kol == 0:
                    break
                if self.money >= Warrior('Human', 1).price * self.kol:
                    for i in range(self.kol):
                        self.army[f'human{i}'] = Warrior('Human', i)
                        self.money -= Warrior('Human', 1).price
                    self.human_kol += self.kol
                    for i in range(self.human_kol):
                        self.army_dmg += self.army[f'human{i}'].dmg 
                    for i in range(self.human_kol):
                        self.army_hp += self.army[f'human{i}'].hp 
                    print(f'Осталось денег:{self.money}') 
                else:
                    print('Недостаточно денег!')
                    break                  
            elif self.choice == 2:
                self.kol = int(input('Скоко?:'))
                if self.kol == 0:
                    break
                if self.money >= Warrior('Knight', 1).price * self.kol:
                    for i in range(self.kol):
                        self.army[f'knight{i}'] = Warrior('Knight', i)
                        self.money -= Warrior('Knight', 1).price
                    self.knight_kol += self.kol
                    for i in range(self.knight_kol):
                        self.army_dmg += self.army[f'knight{i}'].dmg 
                    for i in range(self.knight_kol):
                        self.army_hp += self.army[f'knight{i}'].hp 
                    print(f'Осталось денег:{self.money}')
                else:
                    print('Недостаточно денег!')
                    break
            elif self.choice == 3:
                self.kol = int(input('Скоко?:'))
                if self.kol == 0:
                    break
                if self.money >= Warrior('Knight', 1).price * self.kol:
                    for i in range(self.kol):
                        self.army[f'catapult{i}'] = Warrior('Catapult', i)
                        self.money -= Warrior('Catapult', 1).price
                    self.catapult_kol += self.kol
                    for i in range(self.catapult_kol):
                        self.army_dmg += self.army[f'catapult{i}'].dmg 
                    for i in range(self.catapult_kol):
                        self.army_hp += self.army[f'catapult{i}'].hp 
                    print(f'Осталось денег:{self.money}')
                else:
                    print('Недостаточно денег!')

    def buy_upgrades(self):
        print('''                  ======================================
                  |         Выберите улучшение:        |
                  ======================================
                  |      Армия замка       |   Замок   |
                  ======================================
                  | 1:hp + 25 | 2:dmg + 75 |3:hp + 1500|
                  |Цена:100💰 | Цена:150💰 |Цена:5000💰|
                  ======================================           ''')
        self.choice = int(input())
        if self.choice == 1:
            if self.money >= 100:
                self.army_hp += 25
            else:
                print('Недостаточно денег!')
        elif self.choice == 2:
            if self.money >= 150:
                self.army_dmg +=75
            else:
                print('Недостаточно денег!')
        elif self.choice == 3:
            if self.money >= 5000:
                self.hp += 1500
            else:
                print('Недостаточно денег!')
    
    def buy_hero_upgrades(self):
        print('''                  =========================
                  |   Выбери улучшение    |
                  =========================
                  |1:hp + 100|2:dmg + 200 |           
                  |Цена:100💰| Цена:200💰 |
                  =========================''')
        self.choice = int(input())
        if self.choice == 1:
            if self.money >= 100:
                if self.index == 1:
                    red_hero.hp += 100
                elif self.index == 2:
                    yellow_hero.hp += 100
                elif self.index == 3:
                    green_hero.hp += 100
                elif self.index == 4:
                    blue_hero.hp += 100
            else:
                print('Недостаточно денег!')
        elif self.choice == 2:
            if self.money >= 200:
                if self.index == 1:
                    red_hero.dmg += 200
                elif self.index == 2:
                    yellow_hero.dmg += 200
                elif self.index == 3:
                    green_hero.dmg += 200
                elif self.index == 4:
                    blue_hero.dmg += 200
            else:
                print('Недостаточно денег!')   
            
            
                

            

red_castle = Castle(1)
yellow_castle = Castle(2)
green_castle = Castle(3)
blue_castle = Castle(4)           






class Hero:
    def __init__(self, index):
        self.index = index
        self.hp = 1000
        self.dmg = 1000
        self.army = {}
        self.human_kol = 0
        self.knight_kol = 0
        self.catapult_kol = 0
        self.army_dmg = 0
        self.army_hp = 0
    
    def create_hero(self):
        self.hp = 1000
        self.dmg = 1000
        self.army = {}
        self.human_kol = 0
        self.knight_kol = 0
        self.catapult_kol = 0
        self.army_dmg = 0
        self.army_hp = 0
    
    def take_army(self):
        if self.index == 1:
            self.choice = int(input('Сколько людей(Human) вы хотите забрать?: '))
            if self.choice <= red_castle.human_kol:
                for i in range(self.choice):
                    self.army[f'human{i+self.human_kol}'] = Warrior('Human', i+self.human_kol)
                    del red_castle.army[f'human{i+self.human_kol}']
                    red_castle.human_kol -= 1
                self.human_kol += self.choice
                self.army_dmg += Warrior('Human',1).dmg
                self.army_hp +=  Warrior('Human',1).hp
                    
            else:
                print('В вашей армии нет столько воинов!')
            self.choice = int(input('Сколько рыцарей вы хотите забрать?: '))
            if self.choice <= red_castle.knight_kol:
                for i in range(self.choice):
                    self.army[f'knight{i+self.knight_kol}'] = Warrior('Knight', i+self.knight_kol)
                    del red_castle.army[f'knight{i+self.knight_kol}']
                    red_castle.knight_kol -= 1
                self.knight_kol += self.choice
                self.army_dmg += Warrior('Knight',1).dmg
                self.army_hp +=  Warrior('Knight',1).hp
                    
            else:
                print('В вашей армии нет столько воинов!')
            self.choice = int(input('Сколько катапульт вы хотите забрать?: '))
            if self.choice <= red_castle.catapult_kol:
                for i in range(self.choice):
                    self.army[f'catapult{i+self.catapult_kol}'] = Warrior('Catapult', i+self.catapult_kol)
                    del red_castle.army[f'knight{i+self.catapult_kol}']
                    red_castle.catapult_kol -= 1
                self.catapult_kol += self.choice
                self.army_dmg += Warrior('Catapult',1).dmg
                self.army_hp +=  Warrior('Catapult',1).hp
                    
            else:
                print('В вашей армии нет столько воинов!')
        if self.index == 2:
            self.choice = int(input('Сколько людей(Human) вы хотите забрать?: '))
            if self.choice <= yellow_castle.human_kol:
                for i in range(self.choice):
                    self.army[f'human{i+self.human_kol}'] = Warrior('Human', i+self.human_kol)
                    del yellow_castle.army[f'human{i+self.human_kol}']
                    yellow_castle.human_kol -= 1
                self.human_kol += self.choice
                self.army_dmg += Warrior('Human',1).dmg
                self.army_hp +=  Warrior('Human',1).hp
            else:
                print('В вашей армии нет столько воинов!')
            self.choice = int(input('Сколько рыцарей вы хотите забрать?: '))
            if self.choice <= yellow_castle.knight_kol:
                for i in range(self.choice):
                    self.army[f'knight{i+self.knight_kol}'] = Warrior('Knight', i+self.knight_kol)
                    del yellow_castle.army[f'knight{i+self.knight_kol}']
                    yellow_castle.knight_kol -= 1
                self.knight_kol += self.choice
                self.army_dmg += Warrior('Knight',1).dmg
                self.army_hp +=  Warrior('Knight',1).hp
            else:
                print('В вашей армии нет столько воинов!')
            self.choice = int(input('Сколько катапульт вы хотите забрать?: '))
            if self.choice <= yellow_castle.catapult_kol:
                for i in range(self.choice):
                    self.army[f'catapult{i+self.catapult_kol}'] = Warrior('Catapult', i+self.catapult_kol)
                    del yellow_castle.army[f'knight{i+self.catapult_kol}']
                    yellow_castle.catapult_kol -= 1
                self.catapult_kol += self.choice
                self.army_dmg += Warrior('Catapult',1).dmg
                self.army_hp +=  Warrior('Catapult',1).hp
            else:
                print('В вашей армии нет столько воинов!')
        if self.index == 3:
            self.choice = int(input('Сколько людей(Human) вы хотите забрать?: '))
            if self.choice <= green_castle.human_kol:
                for i in range(self.choice):
                    self.army[f'human{i+self.human_kol}'] = Warrior('Human', i+self.human_kol)
                    del green_castle.army[f'human{i+self.human_kol}']
                    green_castle.human_kol -= 1
                self.human_kol += self.choice
                self.army_dmg += Warrior('Human',1).dmg
                self.army_hp +=  Warrior('Human',1).hp
            else:
                print('В вашей армии нет столько воинов!')
            self.choice = int(input('Сколько рыцарей вы хотите забрать?: '))
            if self.choice <= green_castle.knight_kol:
                for i in range(self.choice):
                    self.army[f'knight{i+self.knight_kol}'] = Warrior('Knight', i+self.knight_kol)
                    del green_castle.army[f'knight{i+self.knight_kol}']
                    green_castle.knight_kol -= 1
                self.knight_kol += self.choice
                self.army_dmg += Warrior('Knight',1).dmg
                self.army_hp +=  Warrior('Knight',1).hp
            else:
                print('В вашей армии нет столько воинов!')
            self.choice = int(input('Сколько катапульт вы хотите забрать?: '))
            if self.choice <= green_castle.catapult_kol:
                for i in range(self.choice):
                    self.army[f'catapult{i+self.catapult_kol}'] = Warrior('Catapult', i+self.catapult_kol)
                    del green_castle.army[f'knight{i+self.catapult_kol}']
                    green_castle.catapult_kol -= 1
                self.catapult_kol += self.choice
                self.army_dmg += Warrior('Catapult',1).dmg
                self.army_hp +=  Warrior('Catapult',1).hp
            else:
                print('В вашей армии нет столько воинов!')
        if self.index == 4:
            self.choice = int(input('Сколько людей(Human) вы хотите забрать?: '))
            if self.choice <= blue_castle.human_kol:
                for i in range(self.choice):
                    self.army[f'human{i+self.human_kol}'] = Warrior('Human', i+self.human_kol)
                    del blue_castle.army[f'human{i+self.human_kol}']
                    blue_castle.human_kol -= 1
                self.human_kol += self.choice
                self.army_dmg += Warrior('Human',1).dmg
                self.army_hp +=  Warrior('Human',1).hp
            else:
                print('В вашей армии нет столько воинов!')
            self.choice = int(input('Сколько рыцарей вы хотите забрать?: '))
            if self.choice <= blue_castle.knight_kol:
                for i in range(self.choice):
                    self.army[f'knight{i+self.knight_kol}'] = Warrior('Knight', i+self.knight_kol)
                    del blue_castle.army[f'knight{i+self.knight_kol}']
                    blue_castle.knight_kol -= 1
                self.knight_kol += self.choice
                self.army_dmg += Warrior('Knight',1).dmg
                self.army_hp +=  Warrior('Knight',1).hp
            else:
                print('В вашей армии нет столько воинов!')
            self.choice = int(input('Сколько катапульт вы хотите забрать?: '))
            if self.choice <= blue_castle.catapult_kol:
                for i in range(self.choice):
                    self.army[f'catapult{i+self.catapult_kol}'] = Warrior('Catapult', i+self.catapult_kol)
                    del blue_castle.army[f'knight{i+self.catapult_kol}']
                    blue_castle.catapult_kol -= 1
                self.catapult_kol += self.choice
                self.army_dmg += Warrior('Catapult',1).dmg
                self.army_hp +=  Warrior('Catapult',1).hp
            else:
                print('В вашей армии нет столько воинов!')
    
    def attack(self):
        print(''' 
                  =====================================
                  |          Кого атаковать?          |          
                  =====================================
                  |1:NPC|2:Замок игрока|3:Героя игрока|
                  ===================================== 
                                                         ''')
        self.choice1 = int(input())
        if self.choice == 1:
            print(''' 
                     ====================================================================
                     |                          Выберите NPC                            |          
                     ====================================================================                            
                     |1:Стая волков |2:Болотный гоблин|3:Пещерный гигант|4:Горный дракон| 
                     |hp = 250      |hp = 1500        |hp = 6000        |hp = 45000     |
                     |dmg = 225     |dmg = 2000       |dmg = 6000       |dmg = 15000    |
                     |reward = 375💰|reward = 1000💰  |reward = 2500💰  |reward = 8000💰|                                      
                     ====================================================================
                                                                                                 ''')
            self.choice2 = int(input())
            # if self.choice2 == 1:
            #     volves.hp - 

            

red_hero = Hero(1)
yellow_hero = Hero(2)
green_hero = Hero(3)
blue_hero = Hero(4)






class Player:    
    def __init__(self,color):
        self.color = color
    def buy_army(self):
        if self.color == 1:
            red_castle.buy_army()
        elif self.color == 2:
            yellow_castle.buy_army()
        elif self.color == 3:
            green_castle.buy_army()
        elif self.color == 4:
            blue_castle.buy_army()
    def create_hero(self):
        if self.color == 1:
            if red_hero.hp == 0:
                red_hero.create_hero()
            else:
                print('У вас уже есть герой!')
        if self.color == 2:
            if yellow_hero.hp == 0:
                yellow_hero.create_hero()
            else:
                print('У вас уже есть герой!')
        if self.color == 3:
            if green_hero.hp == 0:
                green_hero.create_hero()
            else:
                print('У вас уже есть герой!')
        if self.color == 4:
            if blue_hero.hp == 0:
                blue_hero.create_hero()
            else:
                print('У вас уже есть герой!')
    
    def buy_upgrades(self):
        while True:
            print('''                      =========================
                      |   Выбери улучшение    |
                      =========================
                      |1:Для замка|2:Для героя|
                      =========================''')
            self.choice = int(input())
            if self.choice == 1:
                if self.color == 1:
                    red_castle.buy_upgrades()
                if self.color == 2:
                    yellow_castle.buy_upgrades()
                if self.color == 3:
                    green_castle.buy_upgrades()
                if self.color == 4:
                    blue_castle.buy_upgrades()
            elif self.choice == 2:
                if self.color == 1:
                    red_castle.buy_hero_upgrades()
                if self.color == 2:
                    yellow_castle.buy_hero_upgrades()
                if self.color == 3:
                    green_castle.buy_hero_upgrades()
                if self.color == 4:
                    blue_castle.buy_hero_upgrades()
            else:
                break

red_player = Player(1)
yellow_player = Player(2)
green_player = Player(3)
blue_player = Player(4)




red_player.buy_army()
# print(red_castle.human_kol,red_castle.knight_kol,red_castle.catapult_kol)
# print(red_hero.human_kol,red_hero.knight_kol,red_hero.catapult_kol)
# print(red_castle.army)
# print(red_hero.hp)
# print(red_hero.dmg)
# # print(red_castle.hp)
# # # red_hero.take_army()
# print(red_hero.army)
# print(red_hero.army_hp)
# print(red_hero.army_dmg)
# # # print(red_castle.army)
# # # print(red_castle.human_kol,red_castle.knight_kol,red_castle.catapult_kol)
# # print(red_castle.army_dmg)
# # print(red_castle.army_hp)
# # red_player.buy_upgrades()
# # print(red_castle.army_dmg)
# # print(red_castle.army_hp)
# # # red_player.buy_army()
# # print(red_hero.hp)
# # print(red_hero.dmg)
# # print(red_castle.hp)
# # red_player.buy_army()
# red_hero.take_army()
# print(red_hero.army)
# print(red_hero.army_hp)
# print(red_hero.army_dmg)
# print(red_castle.human_kol,red_castle.knight_kol,red_castle.catapult_kol)
# print(red_hero.human_kol,red_hero.knight_kol,red_hero.catapult_kol)
# print(red_castle.army)
# red_hero.take_army()
# print(red_castle.human_kol,red_castle.knight_kol,red_castle.catapult_kol)
# print(red_hero.human_kol,red_hero.knight_kol,red_hero.catapult_kol)
# print(red_castle.army)
# red_hero.take_army()
# print(red_castle.human_kol,red_castle.knight_kol,red_castle.catapult_kol)
# print(red_hero.human_kol,red_hero.knight_kol,red_hero.catapult_kol)
# print(red_castle.army)
        
