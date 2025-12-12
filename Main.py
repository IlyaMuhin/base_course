from Castle import Castle, castle_list, released_army
from Hero import Hero, hero_list
from Player import Player, players_list
from Monster import Monster
from NPC import NPC, npc_list, npc_stats, volves, giant, goblin, dragon

a = Player('red')
a_castle = Castle('red')
a_hero = Hero('red')
a.check_stats()
a_castle.create_monster('peasant', 20000)
a_castle.create_monster('knight', 5000)
a_castle.create_monster('catapult', 2000)
a.check_stats()
b = Player('green')
b_castle = Castle('green')
b_hero = Hero('green')
a_castle.release_army('peasant', 20000)
a_castle.release_army('knight', 5000)
a_castle.release_army('catapult', 2000)
a.check_stats()
a_hero.take_army()
a_hero.attack_player('green')
b.check_stats()
b_castle.create_monster('catapult',200)
b.check_stats()
