
class Electriccar:
    Numberofwheels = "Number of wheels 4"
    Batterycapacity = "Battery capacity 75"
    Numberofseats = "Number of seats 4"
    Seatsize = "Seat size 47"
    Numberofheadlights = "Number of head lights 4"
    Wheelsize = "Wheel size 25"
    Lobovoesteklo = "The car has a windshield"

class Electricmotorcycle(Electriccar):
    Numberofwheels = "Number of wheelss 3"
    Batterycapacity = "Barrery capacity 50"
    Numberofseats = "Number of seats 2"
    Seatsize = "Seatsize 32"
    Numberofheadlights = "Number of headlights 2"
    Wheelsize = "Wheelsize 17"
    Steklo = "The electric motorcycle has a windshield"

class Electroscooter(Electricmotorcycle):
    Numberofwheels = "Number of wheels 2"
    Batterycapacity = "Battery capacity 37"
    Wheelsize = "Wheelsize 13"



    def __init__(self):
        print(self.Numberofseats)
        print(self.Batterycapacity)
        print(self.Seatsize)
        print(self.Wheelsize)
        print(self.Numberofwheels)
        print(self.Numberofheadlights)
        print(self.Lobovoesteklo)
        print(self.Steklo)
factory = Electroscooter()

# class Hello_world:
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#
#
#     def __init__(self):
#         self.world = "World"
#         self._world = "_World"
#         self.__world = "__World"
#
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
# class Hi(Hello_world):
#     def hi_printer(self):
#         print(self.hello)
#         print(self._hello)
#         # print(self.__hello)
#         print(self.world)
#         print(self._world)
#         # print(self.__world)
#
# hello = Hello_world()
# hello.printer()
# hi = Hi()
# hi.hi_printer()


