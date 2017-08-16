from person import Person


class Student(Person):
    NUMBER_OF_TASKS = 37
    NUMBER_OF_TESTS = 12
    TEST_WEIGHTS = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 15]

    def __init__(self, name, age=18):
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.hw_results = [0] * Student.NUMBER_OF_TASKS
        self.test_results = [0] * Student.NUMBER_OF_TESTS

    def print_info(self):
        # print('================================')
        # print('Name:', self.name)
        # print('Age:', self.age)
        super().print_info()
        print('H/w results:', self.hw_results)
        print('Test result:', self.test_results)
        print('Total rank:', self.total_rank())
        print('================================')

    def accept_task(self, *number_of_tasks):
        for task_number in number_of_tasks:
            self.hw_results[task_number-1] = 1

    def accept_test(self, *number_of_tests):
        for test_number in number_of_tests:
            self.test_results[test_number-1] = 1

    def total_rank(self):
        total_rank = sum(self.hw_results)
        for i in range(Student.NUMBER_OF_TESTS):
            total_rank += self.test_results[i] * Student.TEST_WEIGHTS[i]
        return total_rank


student1 = Student('Bill', 22)
student2 = Student('Alice')
student3 = Student('Scott', 18)

student1.accept_task(3,5,7,11,13,17,19)
student2.accept_task(1,2,3,4,5,6)
student2.accept_test(1,2,3,4,5,6,12)
student3.accept_task(1,2,3,12)

student1.print_info()
student2.print_info()
student3.print_info()