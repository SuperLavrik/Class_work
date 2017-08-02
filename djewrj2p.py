def ret(num, lst):
    print (lst)
    if not num in lst :
        print (num)
        lst.append(num)
        #break

    return lst

lst = [1,2,3]
num = 5
ret(num, lst)
print (lst)

