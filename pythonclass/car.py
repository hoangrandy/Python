class Car(object):
    """
    Represent a car in my virtual world.

    Arguments:
    make(string): car make
    model(string): car model
    fuel_efficiency(float): in miles per gallon
    mileage(float, optional): current mileage on car in miles, defaults to 0
    gas (float, optional): current gas in the tank gallons, defaults to 0

    Attributes:
    make(string): car make
    model(string): car model
    fuel_efficiency(float): in miles per gallon
    mileage(float): current mileage on the car in miles
    gas_in_tank(float): current gas in the tank in gallons
    """
    def __init__(self, make, model, fuel_efficiency, mileage=0, gas=0):
        self.make = make
        self.model = model
        self.fuel_efficiency = fuel_efficiency
        self.mileage = mileage
        self.gas_in_tank = gas
