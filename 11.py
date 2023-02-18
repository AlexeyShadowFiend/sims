# import random
# class F:
#     def __init__(self):
#         self.__a = 100
#         self.__b = 300
#         self.sum = None
#     def __method(self):
#         c = random.randint(1,2)
#         if c == 1:
#             self.sum = self.__a * self.__b
#         elif c == 2:
#             self.sum = self.__b + self.__a
#
#     def printer(self):
#         print(self.__method())
#         return self.__method()
#
# gg = F()
# gg.printer()

from random import randint
class F():
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __in_method(self):
        self.operacion = randint(1, 2)
        if self.operacion == 1:
            return self.__a + self.__b
        else:
            return self.__a - self.__b

    def printer(self):
        print(self.__in_method())

ob = F(10,15)
ob.printer()

