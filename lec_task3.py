import numpy as np
states = {1: "Болеет", 2: "Выздоравливает", 3: "Здоров"}
class Puppy:
    def __init__(self, index):
        self.health = None
        self.index = index
    state = states[1]
    def get_treatment(self):
        if self.state == states[3]:
            pass
        elif self.state == states[1]:
            self.state = states[2]
        else:
            self.state = states[3]
    def is_healthy(self):
        if self.state == states[3]:
            self.health = True
        else:
            self.health = False

# pup = Puppy(1)
# pup.get_treatment()
# print(pup.state)            
        




class Dog:
    def __init__(self, puppies_kol):
        self.allhealth = None
        self.puppies_kol = puppies_kol
        self.puppies = []
        for i in range(puppies_kol):
            self.puppies.append(Puppy(i+1))
    def heal_all(self):
        for puppy in self.puppies:
            puppy.get_treatment()
    def all_are_healthy(self):
        for puppy in self.puppies:
            puppy.is_healthy()
            if puppy.health == False:
                self.allhealth = False
        print(self.allhealth)
            
    def give_away_all(self):
        self.puppies = []
dog = Dog(3)
# dog.all_are_healthy()
# dog.heal_all()
# print(Puppy(1).state)
# print(dog.puppies)




class Vet:
    def __init__(self, name):
        self.name = name
        self.plant = dog
    def work(self):
        self.plant.heal_all()
    def care(self):
        self.plant.all_are_healthy()
        if self.plant.allhealth == True:
            self.plant.give_away_all()
            print("Все щенки пристроены!")
        else:
            print("Не все щенки вылечились!")
    def knowledge_base(self):
        for puppy in self.plant.puppies:
            print(puppy.state)
vet = Vet("Виталий")
vet.knowledge_base()
vet.work()
vet.care()
vet.work()
vet.care()
vet.work()
vet.care()

vet.knowledge_base()
vet.work()
vet.knowledge_base()
vet.work()
vet.knowledge_base()

    






    
    

        
       

