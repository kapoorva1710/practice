class Engine:
    def engine_type(self):
        return "V8 Engine"

class Wheels:
    def wheel_type(self):
        return "Alloy Wheels"

class Car(Engine, Wheels):
    def car_features(self):
        print(f"This car has a {self.engine_type()} and {self.wheel_type()}.")


car = Car()
car.car_features()
