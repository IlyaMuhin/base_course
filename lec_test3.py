import math

class ClassVector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        return f'Длина вектора: {math.sqrt(self.x**2 + self.y**2 + self.z**2)}'

    def __str__(self):
        return f'Вектор с координатами: {self.x, self.y, self.z}'

    def __repr__(self):
        return f"ClassVector(x='{self.x}', y={self.y}, z={self.z})"
    
    def __add__(self, other):
        return ClassVector(self.x + other.x,self.y + other.y,self.z + other.z)
    
    def __sub__(self, other):
        return ClassVector(self.x - other.x,self.y - other.y,self.z - other.z)
    
    def __mul__(self, other):
        return ClassVector(self.x * other.x,self.y * other.y,self.z * other.z)
    
    def __eq__(self, other):
        return repr(self) == repr(other)
    
    def __ne__(self, other):
        return repr(self) != repr(other)
    
    def __pow__(self, other):
        return ClassVector(self.x ** other,self.y ** other,self.z ** other)
    
    
        
    

vector1 = ClassVector(1,2,3)
vector2 = ClassVector(2,3,4)
vector3 = vector1**2
print(vector3)

