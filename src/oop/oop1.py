# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    pass


class GroundVehicle(Vehicle):
    pass
    # def __init__(self, Own_Attributes):
    # super().__init__(Vehicle_Attributes)


class FlightVehicle(Vehicle):
    pass
    # def __init__(self, Own_Attributes):
    # super().__init__(#Vehicle_Attributes)


class Starship(FlightVehicle):
    pass
    # def __init__(self, own_Attributes):
    # super()__init__(self, Flightvehicle_Attributes)


class Airplane(FlightVehicle):
    pass
    # def __init__(self, Own_Attributes)
    # super().__init__(FlightVehicle_Attributes)


class Car(GroundVehicle):
    pass
    # def __init__(self, Own_Attributes)
    # super().__init__(#GroundVehicle_Attributes)


class Motorcycle(GroundVehicle):
    pass
    # def __init__(self, Own_Attributes)
    # super().__init__(GroundVehicle_Attributes)
