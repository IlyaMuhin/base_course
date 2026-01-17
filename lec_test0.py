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
    def __init__(self, lines):
        self.lines = lines

    def __mul__(self, other):
        return self.lines * other
    
    def __add__(self, other):
        return self.lines + other

    def __sub__(self, other):
        return self.lines - other
    
    def __truediv__(self, other):
        return int(self.lines / other)
    
    @property
    def show(self):
        print(' ==================================')
        for i in range(self.lines):
            print('|                                  |')
            print(' ==================================')



    
    

    

pl1 = Planet(3)
pl2 = Planet(4)
print(pl1 <= pl2)

table1 = Table(3)
table2 = Table(table1 * 2)
table2.show