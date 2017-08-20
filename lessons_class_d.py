# import lessons_utils
from lessons_utils import print_matrix as my_print_matrix
import sys
import pprint
import math
import collections

#
# matrix = [[0]*5 for i in range(3)]
#
# print_matrix = True
#
# if print_matrix:
#     my_print_matrix(matrix)
#
# print(math.pi)
# d = collections.OrderedDict()
# pprint.pprint(sys.path)

from student import Student
from professor import Professor




if __name__ == '__main__':

    student1 = Student('Bill', 22)
    student2 = Student('Alice')
    student3 = Student('Scott', 18)

    student1.accept_task(3,5,7,11,13,17,19)
    student2.accept_task(1,2,3,4,5,6)
    student2.accept_test(11,12)
    student3.accept_task(1,2,3)
    student3.accept_test(1,2,3,4,5,6,7,8,9,10,11,12)

    # student1.print_info()
    # student1.print_info()
    # student2.print_info()
    # student3.print_info()

    # print(id(Student))
    # print(type(type(type(Student))))


    # pprint.pprint(Student.__dict__)
    # pprint.pprint(student1.__dict__)


    # student1.__dict__["name"] =  " William"
    # print(student1.__dict__["name"])
    # print (student1.name)

    pr1 = Professor("Donald Knuth",42)
    pr1.print_info()
    pr1.salary =  1000


    print (pr1.get_groups())
    pr1.groups = [" Math","CS","ML","AI"]
    print(pr1.get_groups())





    #
    # monkey patching