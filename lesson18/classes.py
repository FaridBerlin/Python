class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("is moving.")

    def get_make_model(self):
        return f"I am a {self.make} {self.model}."

my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
print(my_car.get_make_model())
my_car.moves()


your_car = Vehicle('Mercedes', 'SL AMG')
print(your_car.get_make_model())
your_car.moves()