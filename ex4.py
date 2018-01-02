
#adding values to variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
#This used to be passengers / cars_driven but its redundant so I just replayed with drivers
average_passengers_per_car = passengers / drivers

#Print out with the variable cars how many cars are available
print "There are", cars, "cars available."

#print out with the variable drivers how many drivers are available
print "There are", drivers,  "drivers available."

#print out the number of empty cars that are there
print "There will be", cars_not_driven, "empty cars today."

#print out the number of seats available
print "We can transport", carpool_capacity, "people today."

#print out the number of people that need rides
print "we have", passengers, "to carpool today."

#print out the number of people that each driver need to take in each car
print "We need to put about", average_passengers_per_car, "in each car."
