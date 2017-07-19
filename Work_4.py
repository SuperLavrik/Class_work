# time = "338:444:44"
#
# idx_contril_1 = time.find(':')
#
# print(idx_contril_1)
#
# idx_contril_2 = time.find(':',idx_contril_1+1,)
#
# print(idx_contril_2)
#
# name = "jeff bezos"
# print(name)
# name_lst = name.split()
# name_lst[0] = name_lst[0].capitalize()
# name_lst[1] = name_lst[1].capitalize()
# new_name = name_lst[0] + " " + name_lst[1]
# print(new_name)

import re

t = "a, c^d:f"


#list = t.split(","," "," ^",":")
#print(list)
# def pow(a,b):
#     print ("I'm inside function!!!")
#     return a**b
#
# d = 4
# e = 5
# result = pow(d,e)
# print (pow(d,e))

import math

#
# def pretty_print(value):
#     print_delim()
#     print("Value :", value)
#     print("***********************")
#
# def print_delim():
#     print ("*****-----****************")
#
# pretty_print(result)

def square_circle(radius):
    return (math.pi * radius**2)

sq_cir = square_circle(5)
print (sq_cir)

def add_and_mulpiply(x, y):
    add_result = x + y
    multi_result = x * y
    return (add_result, multi_result)

result_1, result_2 = add_and_mulpiply(4,5)

print (result_1, result_2)

