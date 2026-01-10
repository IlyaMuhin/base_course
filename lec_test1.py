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

    


    def _make_deal(self,business):
        self.business = business
        self._money -= business._price
        self._business = 'Есть'


    def buy_business(self,business,skidka):
        self.business = business
        self.skidka = skidka 
        business.final_price(skidka)     
        if self._money >= self.business._price: 
            self._make_deal(business)           
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
    def __init__(self,price):
        super().__init__(_area = 50000000, _price = price)    


Businessman.def_info()
businessman = Businessman()
businessman.info()
cafe = Business(2342135125,15252567)
restaraunt = RestarauntBusiness(10000000000000000000000000000000)

businessman.buy_business(cafe, 100)
businessman.info()