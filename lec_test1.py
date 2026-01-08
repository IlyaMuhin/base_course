class Businessman:
    def_name = 'Ilya'
    def_age = 30


    def __init__(self, name = def_name, age = def_age):
        self.name = name
        self.age = age
        self._money = 10000000
        self._business = 'Нету'
    

    def info(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Капитал: {self._money}')
        print(f'Наличие бизнесса: {self._business}')


    @staticmethod
    def def_info(def_name = def_name,def_age = def_age):
        print(f'Имя:{def_name}')
        print(f'Возраст:{def_age}')

    


    def _make_deal(self,business,price):
        self.business = business
        self.price = price
        self._money -= self.price
        self._business = self.business


    def buy_business(self,house,skidka):
        self.house = house
        self.skidka = skidka 
        restaraunt.final_price(skidka)     
        if self._money >= restaraunt._price: 
            self._make_deal(house,restaraunt._price)           
        else:
            print('Недостаточно денег!')





    def earn_money(self):
        self._money += 10000000


class Business:
    def __init__(self, _area, _price):
            self._area = _area
            self._price = _price
    

    def final_price(self,skidka):
        self.skidka = skidka
        self._price = int(self._price * (100 - self.skidka) / 100)

    def buy_business(self,skidka):
        self.skidka = skidka

    


class RestarauntBusiness(Business):
    def __init__(self):
        super().__init__(_area = 50000000, _price = 20000000)    


Businessman.def_info()
businessman = Businessman()
businessman.info()
restaraunt = RestarauntBusiness()

businessman.buy_business('restaraunt', 100)
businessman.info()