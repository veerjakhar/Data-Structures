class car:
    def __init__(self, brand, color, model, fuel):
        self.brand = brand
        self.color = color
        self.model = model
        self.fuel = fuel

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = self.new_color

    def show_car(self):
        print("Car's values: Brand is {}\n Color is {}\n Model is {}\n Fuel type is {}".format(self.brand, self.color, self.model, self.fuel))

onecar = car("Tesla", "Blue", "Y", "Petrol")
onecar.show_car()

class suv(car):
    def __init__(self, brand, color, model, fuel, transmission, seats, turbo):
        car.__init__(self, brand, color, model, fuel)
        self.transmisson = transmission
        self.seats = seats
        self.turbo = turbo

    def show_car(self):
        print("Car's values: Brand is {}\n Color is {}\n Model is {}\n Fuel type is {}\n Trassnmisson type is {}\n Number of seats is {}\n Is car tubro {}".format(self.brand, self.color, self.model, self.fuel, self.transmisson, self.seats, self.turbo))
        
twocar = suv("Honda", "White", "Suv", "Petrol", "Geared", "8", "No")
twocar.show_car()
