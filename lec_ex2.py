class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name

    def __len__(self):
        return len(self.planets)
    
    def __add__(self, other):
        self.planets.append(other)
        return StarSystem(self.planets, self.name)
    
    def __bool__(self):
        return len(self.planets) > 0
    

    def __getitem__(self, key):
        return self.planets[key]
    

system1 = StarSystem(['p1','p2'], 'System_1')
system2 = StarSystem([], 'System_2')
print(len(system1))
system1 += 'p4'
system1 += 'p5'
print(system1.planets)

print(bool(system1))
print(bool(system2))

system1[0]
system1[0:2]