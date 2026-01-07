class Buisnessman:
    def_name = 'Ilya'
    def_age = 30


    def __init__(self, name = def_name, age = def_age):
        self.name = name
        self.age = age
        self._money = 100000
        self._business = False
    

    def info(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Капитал: {self._money}')
        print(f'Наличие бизнесса: {self._business}')


    @staticmethod
    def def_info(def_name = def_name,def_age = def_age):
        print(def_name)
        print(def_age)


    def _make_deal(self,business,price):
        self.business = business
        self.price = price


    def buy_business(self,business,skidka):
        


    
