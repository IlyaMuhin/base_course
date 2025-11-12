class Puppy:
    states = [1, 2, 3]
    def __init__(self, index,):
        self.index = index
        self.state = self.states[0]
    def get_treatment(self):
        if self.state == 3:
            return
        self.state +=1
    def is_healthy(self):
        healthy = None
        if self.state == 3:
            healthy = True
        else:
            healthy = False
        print(f'Здоров ли щенок:{healthy}')
puppy1 = Puppy(1)
puppy2 = Puppy(2)
puppy3 = Puppy(3)
    
# pup1 = Puppy(1)
# print(pup1.state)
# pup1.get_treatment()
# print(pup1.state)
# pup1.get_treatment()
# print(pup1.state)
# pup1.is_healthy()




class Dog:
    def __init__(self, puppies):
        self.puppies = puppies
        puppies1 = [1] * puppies
        print(puppies1)
    def heal_all(self):
        puppies2 = list(map(lambda x: x + 1, puppies1))
        print(puppies2)

dog1 = Dog(2)
dog1.heal_all()


        
            
# dog1 = Dog(3)
# print(dog1.puppies_list)



