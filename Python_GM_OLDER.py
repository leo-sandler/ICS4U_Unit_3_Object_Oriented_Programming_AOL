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
