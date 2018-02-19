from car import Car

my_car = Car('Honda', 'Civic', 28)
print(my_car.make)
print(my_car.model)
print(my_car.fuel_efficiency)

your_car = Car('BMW','M3', 18)
# Obviously you are doing way better than me
print(your_car.make)
print(your_car.model)
print(your_car.fuel_efficiency)

print(my_car is your_car)
