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


class 
    
    

    

pl1 = Planet(3)
pl2 = Planet(4)
print(pl1 <= pl2)