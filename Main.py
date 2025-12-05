from Castle import Castle, castle_list, released_army
from Hero import Hero, hero_list
from Player import Player, players_list
from Monster import Monster
from NPC import NPC, npc_list, npc_stats, volves, giant, goblin, dragon

a = Player('red')
a_castle = Castle('red')
a_hero = Hero('red')
b = Player('green')
b_castle = Castle('green')
b_hero = Hero('green')
b_castle.create_monster('catapult',20)
b.check_stats()
b_hero.attack_player('green')
b.check_stats()
b.create_hero()