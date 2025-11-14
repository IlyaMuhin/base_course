class Puppy:
    states = {1: "Болеет", 2: "Выздоравливает", 3: "Здоров"}
    def __init__(self, index, state):
        self.index = index
    state = states[1]
    def get_treatment(self):
        if self.state == self.states[3]:
            pass
        elif self.state == self.states[1]:
            self.state = self.states[2]
        else:
            self.state = self.states[3]
pup = Puppy(1)
print(pup.state)
pup.get_treament()
print(pup.state)
pup.get_treament()
print(pup.state)
pup.get_treament()
print(pup.state)
pup.get_treament()
print(pup.state)
