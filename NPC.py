import random




def npc_stats():
    print(f'''  
               ======================================================================================
               |   Стая волков    |   Болотный гоблин   |   Пещерный гигант   |    Горный дракон    |
               |====================================================================================|
               |                  |                     |                     |                     |
               |hp = {volves.hp}          |  hp = {goblin.hp}          |  hp = {giant.hp}          |   hp = {dragon.hp}        |
               |                  |                     |                     |                     |
               |dmg = {volves.dmg}         |  dmg = {goblin.dmg}         |  dmg = {giant.dmg}         |   dmg = {dragon.dmg}       |
               |=====================================================================================
          
          
          ''')
    


def generate_difficulty(func):
    def f(difficulty):
        volves.hp = random.randint(200, 300) * func(difficulty)
        volves.dmg = random.randint(175, 275) * func(difficulty)
        goblin.hp = random.randint(1300, 1700) * func(difficulty)
        goblin.dmg = random.randint(1800, 2200) * func(difficulty)
        giant.hp = random.randint(6000, 7000) * func(difficulty)
        giant.dmg = random.randint(5700, 6300) * func(difficulty)
        dragon.hp = random.randint(45000, 55000) * func(difficulty)
        dragon.dmg = random.randint(13000, 17000) * func(difficulty)
        npc_stats()
    return f


class NPC:
    def __init__(self,type, hp = 0, dmg = 0):
        self.type = type
        self.hp = hp
        self.dmg = dmg


@generate_difficulty
def generate_npc(difficulty):
    return difficulty

        




volves = NPC("volves")
goblin = NPC("goblin")
giant = NPC("giant")
dragon = NPC("dragon")

generate_npc(5)

