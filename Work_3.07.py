import random
import string
# name_sq = "ABCDEFGH"
#
# print(name_sq)
# for i in range(len(name_sq)):
#     for j in range(1,9):
#         print("%s%d " % (name_sq(i),j), end="\t")
#         print()
# lst = [i for i in range(1,101)]
# print (lst)
#
# alphabet = [chr(i) for i in range(ord('a'), ord('z')+10)]
# print (alphabet)
#
# lst = ['1','2','3']
# lst2 = [int(elem) for elem in lst]
# print(lst2)
#
# s = "This is a string"
# vowels = [c for c in s if c in 'aeiouy']
# print (vowels)
# print (' '.join(vowels))
#
#
# lst_digits = [i for i in range(10)]
# lst_digits2 = [elem**2 for elem in [i for i in range(10)] ]
# print(lst_digits2)
#
# n = 3
# m = 5
# #matrix = [ [0]*n for i in range (m)]
# #print (matrix)
# #print(len(matrix))
#
# matrix = [ [random.randint(1,10)] for j in range (n) for i in range (m)]
# print (matrix)
# print(len(matrix))

text1 = "aaa bbb ccc"
text2 = "bbb ccc bbb"
text_lst1 = text1.split()
text_lst2 = text2.split()

result = []
for word in text_lst1:
    if word in text_lst2:
        result += [word]

print (result)

result2 = [word
           for word in text1.split()
           if word in text2.split()]
print (result2)


print(max([random.randint(20,500) for i in range(random.randint(10,1000))]))

def fibonacci_number(n):
    if n == 0:
        return 1
    elif n == 1 :
        return 1
    else :
        return fibonacci_number(n -1) + fibonacci_number(n-2)

print (fibonacci_number(7))