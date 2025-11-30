npc_list = {}




def npc_stats():
    print(f'''  
               ======================================================================================
               |   Стая волков    |   Болотный гоблин   |   Пещерный гигант   |    Горный дракон    |
               |====================================================================================|
               |                  |                     |                     |                     |
               |hp = {volves.hp}  |  hp = {goblin.hp}   |  hp = {giant.hp}    |   hp = {dragon.hp}  |
               |                  |                     |                     |                     |
               |dmg = {volves.dmg}|  dmg = {goblin.dmg} |  dmg = {giant.dmg}  |   dmg = {dragon.dmg}|
               |=====================================================================================
          
          
          ''')
    



class NPC:
    def __init__(self,type):
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



volves = NPC('volves')
goblin = NPC("goblin")
giant = NPC("giant")
dragon = NPC("dragon")



npc_list['volves'] = volves
npc_list['goblin'] = goblin
npc_list['giant'] = giant
npc_list['dragon'] = dragon