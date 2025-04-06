class MathOperations:
    pi = 3.14159 

    def __init__(self, num):
        self.num = num

    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2


print(MathOperations.add(5, 3)) 
print(MathOperations.circle_area(7)) 
