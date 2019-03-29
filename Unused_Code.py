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

'''
        salaries = []
        for x in range(len(employee_2d_list)):
            salaries.append(employee_2d_list[x][2])
        salaries.sort(key=float, reverse=True)
        salaries_sorted = []
        for x in range(len(salaries)):
            salaries_sorted.append((salaries[x], x))
        '''


'''
class Employee:
    def __init__(self):
        name = self.name_input()
        age = self.age_input()
        salary = self.salary_input()

    def name_input(self):
        while True:
            name = input("What is the employee's name: ")
            if name.isdigit():
                print("Enter a name, not a number.")
                continue
            return name

    def age_input(self):
        while True:
            try:
                age = int(input("What is the employee's age: "))
                if age <= 13:
                    print("It is not legal to have workers aged under 14.")
                    continue
                return age
            except ValueError:
                print("Enter a number for employee age.")
                continue

    def salary_input(self):
        while True:
            try:
                salary = int(input("What is the employee's salary: "))
                if salary <= 0:
                    print("Employees must be paid a positive amount.")
                    continue
                return salary
            except ValueError:
                print("Enter in a number for employee salary.")
                continue


class Player(Employee):
    def __init__(self, goals):
        super().__init__()
        self.goals = goals



leo_v2 = Player(100)

print(leo_v2.goals)
print(leo_v2.salary_input())
'''
# self.employee_dict[self.name] = [name, age, salary, position]
# could make a dictionary for each superior employee. would look like {"Mike Babcock": [N,A,S,P][N,A,S,P]}
# Coulc inclue password/sign in functionality.