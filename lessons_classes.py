#import lessons_utils

# from lessons_utils import print_matrix as  my_print_matrix
#
#
#
# import sys
# import pprint
#
# matrix = [[0]*5 for i in range(3)]
#
# my_print_matrix(matrix)
# pprint.pprint (sys.path)

class Student:

    NUMBER_OF_TASK = 37
    NUMBER_OF_TEST = 12

    def __init__(self, name, age=18):
        #print (" Self", self, id(self))
        self.name = name
        self.age = age
        self.hw_results = [0] * Student.NUMBER_OF_TASK
        self.test_results = [0] * Student.NUMBER_OF_TEST

    def print_info(self):
        print("++++++++++++++++++++")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("H/w result: ", self.hw_results)
        print("Test result: ", self.test_results)
        print("++++++++++++++++++++")
        print()

    def accept_task(self, *number_of_task):
        for task_number in number_of_task:
            self.hw_results[task_number - 1] = 1

    def accept_test(self, *number_of_test):
        for task_test in number_of_test:
            self.test_results[test_number - 1] = 1







student1 = Student("Bill", 22)
# print (type(student1))
student2 = Student("Alise", 24)
student3 = Student("Scott", 18)

student1.accept_task(1,3,7,11,17)
student2.accept_task(1,2,4,7)
student3.accept_task(1,2,3,4,5,6,7)
#print (id(student1),id(student2),id(student1))


# student1.name = "Bill"
# student1.age = 22
# print (student1)
#print( student1.name, student1.age)


# student2.name = "Alise"
# student2.age = 24
# print (student2)
# print( student2.name, student2.age)
# print( student3.name, student3.age)

student1.print_info()
student2.print_info()
student3.print_info()