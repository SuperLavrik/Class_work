import math
import random

def max_random_numbers(num_of_numbers, lower_bound=100,upper_bound=200):
    curr_max = 0
    for i in range(num_of_numbers):
        num = random.randint(lower_bound,upper_bound)
        print(num)
        if num > curr_max :
            curr_max = num
    return curr_max

print ("____________________")
result = max_random_numbers(5)
print ("Max :", result)


def min_random_numbers(num_of_numbers, lower_bound=100,upper_bound=200):
    curr_min = upper_bound
    for i in range(num_of_numbers):
        num = random.randint(lower_bound,upper_bound)
        print(num)
        if num < curr_min :
            curr_min = num
    return curr_min

print ("____________________")
result = min_random_numbers(5)
print ("Min :", result)

