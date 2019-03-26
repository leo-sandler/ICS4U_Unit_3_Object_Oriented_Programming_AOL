'''
class Employed:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def from_input(cls):
            input("What is the employee's name: "),
            int(input("Employee age: ")),
            int(input('Employee salary: '))


leon = Employed.from_input()
print(leon.age)
'''

'''
print(dubas)  # calling the method through finding the space where the instantiated function is stored. 
Through directory/path related stuff.
# <__main__.GeneralManager object at 0x000001A5C080E630>  THIS IS WHAT NEEDS TO BE ACCESSED.
'''