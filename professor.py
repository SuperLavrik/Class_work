from person import Person

class Professor(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
    #     self.name = name
    #     self.age = age
    #
    # def print_info(self):
    #     print('================================')
    #     print('Name:', self.name)
    #     print('Age:', self.age)
    #     print('================================')
