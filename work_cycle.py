# import random

# import work_6
# for i in range(100, 201, 2):
#     #if i %2 == 0 :
#         print(i)
# for i in range(2110):
#     if work_6.is_year(i):
#         print(i)
# for i in range (100, 201):
#     if work_6.is_year(i):
#s = """Байтовые строки в Python - что это такое и с чем это едят? Байтовые строки очень похожи на обычные строки, но с некоторыми отличиями. Попробуем выяснить, с какими.
#Что такое байты? Байт - минимальная единица хранения и обработки цифровой информации. Последовательность байт представляет собой какую-либо информацию (текст, картинку, мелодию...).
#Создаём байтовую строку"""

import random

# total_sum = 0
# for i in range (101):
#     total_sum = total_sum + i
#
# print(total_sum)

total_sum = 0
for i in range (101):
    total_sum += random.randint(100, 200)
print(total_sum)



