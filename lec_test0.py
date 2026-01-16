class Planet:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius
    
    def __ne__(self, other):
        return self.radius != other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __le__(self, other):
        return self.radius <= other.radius
    
    def __ge__(self, other):
        return self.radius >= other.radius


class Table:
    def __init__(self, columns):
        self.columns = columns

    def __mul__(self, other):
        return self.columns * other
    
    def __add__(self, other):
        return self.columns + other
    
    @property
    def show(self):
        print(' ==================================')
        for i in range(self.columns):
            print('|                                  |')
            print('|==================================|')
        print('|                                  |')
        print(' ==================================')


    
    

    

pl1 = Planet(3)
pl2 = Planet(4)
print(pl1 <= pl2)

table1 = Table(3)
table2 = Table(table1 + 10)
table2.show