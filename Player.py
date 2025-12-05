from Castle import *
from Hero import *



players_list = {}



class Player:
    def __init__(self, color):
        self.color = color
        players_list[self.color] = self


    def check_stats(self):
        castle_list[self.color].check_stats()



    def create_hero(self):
        if hero_list[self.color].hp == 0:
            hero_list[self.color].hp = Hero('').hp
            print('Герой создан')
        else:
            print('У вас уже есть герой!')





        


# red_player = Player('red')
# print(players_list)
# red_player.check_stats()






