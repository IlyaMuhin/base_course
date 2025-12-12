from Castle import *
import Hero



players_list = {}



class Player:
    def __init__(self, color):
        self.color = color
        players_list[self.color] = self


    def check_stats(self):
        print(f'{self.color}:')
        castle_list[self.color].check_stats()



    def create_hero(self):
        print(f'{self.color}:')
        if Hero.hero_list[self.color].hp == 0:
            Hero.hero_list[self.color].hp = Hero.Hero('').hp
            print('Герой создан')
        else:
            print('У вас уже есть герой!')





        


# red_player = Player('red')
# print(players_list)
# red_player.check_stats()






