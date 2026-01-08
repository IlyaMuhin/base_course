class Ball:
    def __init__(self,color):
        self.color = color

    def name(self):
        print(self.__class__.__name__)


ball1 = Ball('red')
ball1.name()