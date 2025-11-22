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
            self.choice = input(f"Кого вы хотите купить?:{warriors_list}:\n")
            self.kol = int(input('Скоко?:'))
            






class Player:    
    def __init__(self, color):
        self.color = color
        
