# # # # # # s = "hello python"
# # # # # # lst = [1, 2, 3, 4, 5]
# # # # # # number_list_iterator = lst.__iter__()
# # # # # # # number_list_iterator = iter(lst)
# # # # # # # print(number_list_iterator)
# # # # # # # print(type(number_list_iterator))
# # # # # # print(number_list_iterator.__next__())
# # # # # #
# # # # #
# # # # #
# # # # # # a = 1555
# # # # # # print(len(a))
# # # # # # temp = int("W")
# # # # #
# # # # # try:
# # # # #     a = int(input('A '))
# # # # #     b = int(input('B '))
# # # # #     result = a / b
# # # # #     print('try',result)
# # # # #     # number = [1,2,3]
# # # # # except TypeError:
# # # # #     print('Преобразование')
# # # # # except Exception :
# # # # #     print('----')
# # # # # except ZeroDivisionError:
# # # # #     result = a / 1
# # # # #     print('except', result)
# # # # # else:
# # # # #     print('ELSE')
# # # # # finally:
# # # # #     print("FINALLY")
# # # #
# # # # def cheker(var):
# # # #     if type(var) != str:
# # # #         raise TypeError(f'Sorry, We can\'t work with {type(var)}')
# # # #     else:
# # # #         print(var * 5)
# # # #
# # # # cheker('10')
# # #
# # # class BuildingError(Exception):
# # #     def __str__(self):
# # #         return f"С таким количеством материалов вы не можете построить"
# # #     def check_material(material, limit):
# # #         if material > limit:
# # #             return  "материалов достаточно"
# # #         else:
# # #             raise BuildingError(material)
# # #
# # # material = 100
# # # limit = 150
# # # print(check_material(material, limit))
# # #
# #
# #
# # def raise_of_the_degrees(number, mex_degrees):
# #     i=0
# #     for _ in range(mex_degrees):
# #         yield number**i
# #         i += 1
# #
# # result = raise_of_the_degrees(1220155, 500)
# # print(result)
# # result.__next__()
# # result.__next__()
# # for _ in result:
# #     print(_)
#
#
#
# def count_up_to(x):
#     count = 1
#     while count <=  x:
#         yield count
#         count += 1
# count = count_up_to(10)
# print(count.__next__())
# print(count.__next__())
# print(list(count))


def my_for(iterable):
    iterator = iterable.__iter__()
    while True:
        try:
            print(iterator.__next__(), end=' ')
        except StopIteration:
            break
my_for([1,2,3])
print()
for i in [1,2,3]:
    print(i, end=' ')
