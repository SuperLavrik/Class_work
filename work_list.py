lst = [10,20,30, 40, 50,60, 70]

# print (lst[0])


# for i in range(len(lst)):
#     lst[i] **= 2
#
# print(lst)

# for i in range(len(lst)-1,-1,-1):
#     print (i, lst[i])
#     if not lst[i] % 3:
#         del lst[i]
#     #lst[i] **= 2

print (lst)

def delite_by_condition(lst, condition):
    for i in range(len(lst) - 1, -1, -1):
        if condition (lst[i]):
            del lst[i]

def is_odd(num):
    return num % 10 != 0

lst.insert(len(lst)//2, 3)
print (lst)
delite_by_condition(lst, is_odd)
print (lst)