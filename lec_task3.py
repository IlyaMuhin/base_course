class Puppy:
    states = ['Болеет', 'Выздоравливает', 'Здоров']
    def __init__(self, index, ):
        self.index = index
        self.state = self.states[0]
    def get_treatment(self):
        if self.states.index(self.state) == 2:
            return
        self.state = self.states[self.states.index(self.state)+1]
    def is_healthy(self):
        healthy = None
        if self.state == 'Здоров':
            healthy = True
        else:
            healthy = False
        print(f'Здоров ли щенок:{healthy}')
    

# puppy1 = Puppy(1)
# print(pup1.state)
# pup1.get_treatment()
# print(pup1.state)
# pup1.get_treatment()
# print(pup1.state)
# pup1.is_healthy()




class Dog:
    def __init__(self, puppies):
        self.puppies = puppies
        self.puppies_list = []
        for i in range(self.puppies):
            globals()[f'puppy{i+1}'] = Puppy(i+1)
            self.puppies_list.append(f'puppy{i+1}')
    def heal_all(self):
            
# dog1 = Dog(3)
# print(dog1.puppies_list)



