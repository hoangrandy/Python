from car import Car

test_car = Car('Porshe', '911', 22)
print('Let us add 15 gallons to the car and drive 100 miles')
test_car.add_gas(15) #fill up the car with 15 gallons of gas

test_car.drive(100) # drive 100 miles which is 6.67 gallons

#What is the mileage now
print('Total mileage of the car: ',test_car.mileage)

# How about a 500 mile drive?
print("Let's try to go 500 more miles")
test_car.drive(500)

print('Toal mileage of car:', test_car.mileage)

print('Oh, oh! What happened. Did we drive to far, check the gas!')
print('Gas in car:', test_car.gas_in_tank)

# Let's use method chaining
print("Add 15 gallons of gas and let's drive 30 miles")

test_car.add_gas(15).drive(30)

print('Mileage: ',test_car.mileage)

print("drive 100 files and add 5 gallons of gas")
test_car.drive(100).add_gas(5)

print('Mileage: ', test_car.mileage)
print('Gas:',test_car.gas_in_tank)
