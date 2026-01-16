class Kletki:
    def __init__(self, kol):
        self.kol = kol

    def __add__(self, other):
        return self.kol + other
    
    def __sub__(self, other):
        return self.kol - other
    
    def __mul__(self, other):
        return self.kol * other
    
    def __truediv__(self, other):
        return int(self.kol / other)
    
    @property
    def info(self):
        print(f'Количество клеток в сосуде: {self.kol} ')
    

jar1 = Kletki(8)
jar2 =  Kletki(jar1 - 3)
jar2.info