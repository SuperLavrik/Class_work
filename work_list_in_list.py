# for i in range(10):
#     print ("%d:" % i, end="")
#     for j in range(10):
#         print(" %d" % j, end="")
#
#     print()

def pyph_table(n =9, m = 9):
    for i in range(1,n + 1):
        #print("%d:" % i, end="")
        for j in range(1,m + 1):
            print(" %d" % (j * i), end="\t")

        print()

pyph_table(4,5)