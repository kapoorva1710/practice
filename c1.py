class Person:
    
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.display_info()
person2.display_info()
