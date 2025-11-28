color_list = {1:'Красный',2:'Желтый',3:'Зеленый',4:'Синий'}
warriors_list = {1:"Human", 2:"Knight", 3:"Catapult"}
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




class Castle:
    def __init__(self,index):
        self.index = index
        self.hp = 100000
        self.money = 100000
        self.army = []
        
    def buy_army(self):
        while True:
            print(f'Ваши деньги:{self.money}')
            self.choice = int(input(f"Кого вы хотите купить?:{warriors_list}:\n"))
            if self.choice == 0:
                break
            self.kol = int(input('Скоко?:'))
            if self.kol == 0:
                break
            if self.money >= Warrior(warriors_list[self.choice], 1).price * self.kol:
                for i in range(self.kol):
                    self.army.append(Warrior(warriors_list[self.choice], i+1))
                    self.money -= Warrior(warriors_list[self.choice], 1).price
                print(f'Осталось денег:{self.money}')
            else:
                print('Недостаточно денег!')
                break
red_castle = Castle(1)
yellow_castle = Castle(2)
green_castle = Castle(3)
blue_castle = Castle(4)           






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
red_player = Player(1)
yellow_player = Player(2)
green_player = Player(3)
blue_player = Player(4)
red_player.buy_army()
        
