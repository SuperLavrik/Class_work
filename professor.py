from person import Person

class Professor(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._salary = 0
        self._groups = []
        self.awards = []


    def add_groups(self, groups):
        if len(self.gruops) > 3 :
            raise ValueError("Too much assigments!")
        self._groups = groups


    def remove_groups(self, gruop):
        if group in groups:
            self._groups.remove(gruop)

    def def_group(self):



    # def print_info(self):
    #     super().print_info()
    #     print('Salary:', self.salary)
    #     if ien(self.groups) > 0:
    #         print('Groups :', self.groups)
    #     print( "Scientific awards: ", self.awards)
    #     print('================================')

     def print_info_ext(self):
        print('Salary:', self._salary)
        if len(self._groups) > 0:
            print('Groups :', self._groups)
        print("Scientific awards: ", self.awards)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary can't be negative !")
        self._salary = salary

