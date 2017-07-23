def is_year(year):
    return year %4 ==0 and year %100 != 0 or year %400 == 0
# if year %4 ==0 and year %100 != 0 or year %400 == 0:
#     return True
#
# else :
#     return False

# x = 4
# y = 101
# if 3 <=  x <= 100 and x !=4 or y >= 100 and y <= 200 :
#     print ("inside")
# else :
#     print("outside")

year = 2024

print (year)
if is_year(year):
    print ("leap year! ")
else :
    print("regular year! ")


# year = 2000
# if year %4 ==0 and year %100 != 0 or year %400 == 0:
#     print ("leap year! ")
# else :
#     print("regular year! ")

