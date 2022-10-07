class Conveer:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
    def __str__(self):
        return f"{self.color} {self.shape}"

volvo = Conveer("red", "wagon") #обєкт класу Conveer
print(volvo) #вивід: red wagon
