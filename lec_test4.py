import numpy as np

class Planet:
    planet_list = ['Меркурий','Венера','Земля','Марс','Юпитер','Сатурн','Уран','Нептун','']
    @staticmethod
    def is_in_solarsystem(index):
        if 1 <= index <= 9:
            if Planet.planet_list[8] == '':
                print('Планета не в Солнечной Системе')
            else:
                print(f'Планета находится в Солнечной Системе: {Planet.planet_list[index - 1]}')
        else:
            print('Планета не в Солнечной Системе')



    def is_Pluto_in_solarsystem(fact):
        if fact == 'Да':
            Planet.planet_list[8] = 'Плутон'
        elif fact == 'Нет':
            Planet.planet_list[8] = ''

    @classmethod
    def check_planets(cls):
        print(cls.planet_list)

    def __init__(self,parity):
        self.parity = parity

    @property
    def odd_even(self):
        if self.parity == 'Even':
            print(f'Четные планеты: {Planet.planet_list[1::2]}')
        elif self.parity == 'Odd':
            print(f'Нечетные планеты: {Planet.planet_list[0::2]}')





Planet.is_in_solarsystem(9)
Planet.check_planets()
Planet.is_Pluto_in_solarsystem('Да')
Planet.check_planets()
Planet.is_in_solarsystem(9)
Planet.is_Pluto_in_solarsystem('Нет')
Planet.check_planets()
planet1 = Planet('Even')
planet1.odd_even
planet1 = Planet('Odd')
planet1.odd_even
