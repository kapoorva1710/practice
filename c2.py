class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print(f"{self.year} {self.brand} {self.model}")


car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)


car1.display_details()
car2.display_details()
