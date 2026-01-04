class Planet:
    @staticmethod
    def is_big_planet(diameter):
        if diameter > 10000:
            return True
        else:
            return False
        
Planet.is_big_planet(100)




class SummatorClass:
    @staticmethod
    def sum_1(a, b):
        print(a + b)

    def sum_2(self,a,b):
        print(a+b)

    def sum_3(self,a,b):
        return SummatorClass.sum_1(a,b)