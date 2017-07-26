
# заполнение коробок
"""
def fill_truck(max_volume, min_box_volume, max_box_volume):
    total_volume = 0
    while total_volume < max_volume:
        box_volume = random.randint(min_box_volume, max_box_volume)
        free_space = max_box_volume - total_volume
        total_volume += box_volume
        print ("Last box = %d , total_volume %d" % (box_volume,total_volu
"""



while True:
    choice = input("Сделай выбор [1...3},q - выход")
    if choice == "q":
        print("Good bay!!")
        break

    if 1 <= int(choice) <= 3:
        if int(choice) == 1:
            print (" Ага. Все так ....")

        if int(choice) == 2:
            print(" так тебе и нада.")

        if int(choice) == 3:
            print(" Совсем печаль.")
    else :
        print ("Все фигня давай по-новой!!!!")
