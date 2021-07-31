from transportation import car,airplane,transportation,bike,motor

mazda = car.Car()
mazda.drive() # drive method is called.
print(mazda.color) # White

print(issubclass(airplane.Airplane,transportation.Transportation)) # True
print(issubclass(airplane.Airplane,object)) # True
print(issubclass(airplane.Airplane,car.Car)) # False

ezbike = bike.Bike()
ezbike.drive() # bike drive method is called

ezmotor = motor.Motor()
ezmotor.drive() # drive method is called.