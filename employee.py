# Employee class same as used in Inheritance folder


class Employee:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.__age = age
# property decorator allows us to define method but access it like a attribute

    @property
    def describe(self):
        return '{} {} is {} years old.'.format(self.first, self.last, self.__age)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith', 40)
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# When called the employee 1 age shows that the object has no attribute age
# This is because its because its being accessed from outside of the class
# print (emp_1.__age)

# here its being accessed from inside of the class so the age is displayed.
print(emp_1.describe)

