class Ball:
    def __init__(self,color):
        self.color = color

    def name(self):
        print(1)

class Goal(Ball):
    def __init__(self,color):
        super().__init__(color = color)


goal = Goal("red")
goal.name()   
