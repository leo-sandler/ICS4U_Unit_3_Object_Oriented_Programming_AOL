# AT END, FIND A WAY TO MAKE SPACING EVEN. POSSIBLY, CREATE TITLES/MESSAGES AFTER SELECTING ONE OF THE OPTIONS FROM
# ALL OPTIONS.


class Employee:
    def __init__(self, name, age, salary, job):
        self.name = name
        self.age = age
        self.salary = salary
        self.job = job


class GeneralManager(Employee):
    def __init__(self):
        super().__init__(name="Kyle Dubas", age=33, salary=1500000, job="General Manager")
        self.vendor_dict = {}
        self.employee_dict = {}
        self.file_reading()

    def file_reading(self):
        employee_file = open("Employees.txt", "r")
        employee_2d_list = [x.split(",") for x in employee_file.read().split("\n")]
        print(employee_2d_list)
        employee_file.close()
        for x in range(0, len(employee_2d_list)):
            self.employee_dict[employee_2d_list[x][0]] = [int(employee_2d_list[x][1]), int(employee_2d_list[x][0]),
                                                          employee_2d_list[x][3]]

        from operator import itemgetter
        list_sorting = sorted(employee_2d_list, key=itemgetter(2), reverse=True)

        with open("Employees.txt", 'w') as emp_file:
            emp_file.writelines(','.join(str(j) for j in i) + '\n' for i in list_sorting)
            # Makes a new line at the end of file. Help to stop doing this.
            emp_file.close()
        # Could have options for printing out the payroll. This could be in alphabetical order by multiple columns
        # or by highest or lowest salary.

    @staticmethod
    def name_input():
        while True:
            name = input("What is the employee's name: ").title()
            if name.isdigit():
                print("Enter a name, not a number.")
                continue
            return name

    @staticmethod
    def age_input():
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

    @staticmethod
    def salary_input():
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

    def all_options(self):
        while True:
            try:
                choice = int(input("\n1) Payroll Viewer\n2) Vendor Creation\n3) Vendor Removal\n4) Add/Remove Vendor "
                                   "Products\n5) Offerings in Each Vendor\n6) Employee Hiring\n7) Employee Firing\n"
                                   "8) Employee Pay Raise\n9) EXIT\nYour Choice: "))
                if choice == 1:
                    self.payroll_viewer()
                if choice == 2:
                    self.vendor_creation()
                if choice == 3:
                    self.vendor_removal()
                if choice == 4:
                    self.vendor_products()
                if choice == 5:
                    self.offerings_for_all_vendors()
                if choice == 6:
                    self.hiring()
                if choice == 7:
                    self.firing()
                if choice == 8:
                    self.pay_raise()
                if choice == 9:
                    exit()
                else:
                    self.all_options()
            except ValueError:
                continue

    def payroll_viewer(self):
        total_payroll = 0
        for x in self.employee_dict.keys():
            print(self.employee_dict[x][2] + ": " + x + "'s salary is $" + "{:,}".format(self.employee_dict[x][1]))
            total_payroll += self.employee_dict[x][1]
        print("\nThe total payroll is $" + "{:,}".format(total_payroll))

    def vendor_creation(self):
        vendor_name = input("What is the name of the new vendor: ").title()
        vendor = Vendor(vendor_name)
        self.vendor_dict[vendor_name] = vendor
        vendor.add_or_remove_products("A")
        '''
        vendor_file = open("Vendors.txt", "w+")
        count = len(vendor_file.read().split()) - 1
        vendor_file.write(str(vendor[count + 1]) + ", " + str(vendor.product_offerings[count + 1]) + "\n")
        vendor_file.close()
        vend = open("Vendors.txt", "r")
        print(vend.read())
        '''

    def vendor_removal(self):
        while True:
            removal_name = input("What vendor do you want to remove: ").title()
            if removal_name in self.vendor_dict:
                del self.vendor_dict[removal_name]
                break

    def vendor_products(self):
        while True:
            vendor_name = input("Enter the name of the vendor you want to edit: ").title()
            if self.vendor_dict[vendor_name]:
                add_or_remove = input("Do you want to add or remove products: ").title()
                if add_or_remove == "Add":
                    self.vendor_dict[vendor_name].add_or_remove_product("A")
                if add_or_remove == "Remove":
                    self.vendor_dict[vendor_name].add_or_remove_product("R")
            else:
                continue

    def offerings_for_all_vendors(self):
        for x in self.vendor_dict:
            x.product_display()

    def hiring(self):
        while True:
            position = int(input("\nThese are the available positions to hire for.\n1) Vendor Employee\n2) "
                                 "Vendor Manager\n3) Head Coach\n4) Assistant Coach\n5) EXIT\nYour Choice: "))
            name = self.name_input()
            age = self.age_input()
            salary = self.salary_input()
            job = ""  # Preventing an error.
            if name not in self.employee_dict:
                if position == 1:
                    Employee(name, age, salary, "Vendor Employee")
                    job = "Vendor Employee"
                if position == 2:
                    Employee(name, age, salary, "Vendor Manager")
                    job = "Vendor Manager"
                if position == 3:
                    Employee(name, age, salary, "Head Coach")
                    job = "Head Coach"
                if position == 4:
                    Employee(name, age, salary, "Assistant Coach")
                    job = "Assistant Coach"
                if position == 5:
                    exit()
                self.employee_dict[name] = [age, salary, job]
                break

    def firing(self):
        while True:
            employee_choice = input("What employee do you want to fire: ")
            if employee_choice in self.employee_dict:
                del self.employee_dict[employee_choice]

    def pay_raise(self):
        while True:
            employee_choice = input("What employee do you want to give a pay raise to: ").title()
            if employee_choice in self.employee_dict:
                try:
                    raise_amount = int(input("How large is the raise: $"))
                    if raise_amount >= 1:
                        self.employee_dict[employee_choice][1] += raise_amount
                        break
                except ValueError:
                    print("Enter a number into the raise amount.")
                    continue


class Vendor:
    def __init__(self, name):
        self.name = name
        self.product_offerings = {}

    def add_or_remove_products(self, a_or_r):
        while True:
            try:
                number_of_products = int(input("How many products do you want to add/remove: "))
                if number_of_products <= 0:
                    print("Enter a number higher than 0.")
                    continue
                break
            except ValueError:
                print("Enter a number please.")
                continue
        count = 0
        while count < number_of_products:
            if a_or_r == "A":
                product = input("\nNew Product: ")
                if product.isdigit():
                    print("Enter a product to be sold, not a number.")
                    continue
                if product.title() in self.product_offerings:
                    print("The " + self.name + " already has that product")
                    continue
                try:
                    price = int(input("Enter the price of " + product.title() + ": $"))
                    if price <= -1:
                        continue
                except ValueError:
                    print("Enter a price")
                    continue
                self.product_offerings[product.title()] = price
            if a_or_r == "R":
                product = input("\nProduct: ")
                if product.isdigit():
                    print("Enter a product, not a number.")
                    continue
                if product.title() in self.product_offerings:
                    del self.product_offerings[product.title()]
                    print(str(product) + " was removed from this vendor.")
            count += 1

    def product_display(self):
        print("\nThese are the available items at " + self.name + ":")
        for x in self.product_offerings:
            print("\nItem: " + x + "\nPrice: " + str(self.product_offerings[x]))


'''
class VendorManager(Employee):
    def __init__(self, name, age, salary, job):
        super().__init__(name, age, salary, job)


class HeadCoach(Employee):
    def __init__(self, name, age, salary, job):
        super().__init__(name, age, salary, job)
        
'''

# Which would better show off my OOP skills. 1: the GM has the ability to control everything. Employee position(Outside
# of skaters) is determined by the GM. The code is ran through the perspective of the GM.

# 2: Employees are created with passwords. This will allow for the python code to act as a database where some employees
# have specific privileges where others do not.


class Skater(Employee):
    def __init__(self, name, age, salary, job, position, goals, shots_on_goal, assists, penalty_minutes, games_played):
        super().__init__(name, age, salary, job)
        self.position = position
        self.goals = goals
        self.shots_on_goal = shots_on_goal
        self.scoring_percentage = shots_on_goal
        self.assists = assists
        self.points = goals + assists
        self.penalty_minutes = penalty_minutes
        self.games_played = games_played
        self.all_stats = {"Name": self.name, "Position": self.position, "Age": self.age, "Salary": self.salary,
                          "Goals": self.goals, "Shots on Goal": self.shots_on_goal, "Scoring Percentage":
                          self.scoring_percentage, "Assists": self.assists, "Points": self.points,
                          "Penalty Minutes": self.penalty_minutes}


class Goalie(Employee):
    def __init__(self, name, age, salary, job, shots_against, saves, shutouts, wins, losses):
        super().__init__(name, age, salary, job)
        self.position = "Goalie"
        self.shots_against = shots_against
        self.saves = saves
        self.goals_against = shots_against - saves
        self.games_played = wins + losses
        self.shutouts = shutouts
        self.wins = wins
        self.losses = losses
        self.save_percentage = (saves / shots_against * 100)
        self.goals_against_average = (self.goals_against / self.games_played)
        self.win_percentage = (wins / self.games_played) * 100
        self.all_stats = {"Name": self.name, "Position": self.position, "Age": self.age, "Salary":
                          self.salary, "Shots Against": self.shots_against, "Goals Against": self.goals_against,
                          "Saves": self.saves, "Save Percentage": self.save_percentage,  "Wins": self.wins,
                          "Losses": self.losses, "Goals Against Average": self.goals_against_average,
                          "Winning Percentage": self.win_percentage, "Shutouts": self.shutouts}


dubas = GeneralManager()
dubas.all_options()


print(dubas.__class__.__name__)

'''
fred = Employee("Frederick Andersen", 29, 5000000)
starter = Goalie(fred.name, fred.age, fred.salary, 100, 95, 2, 8, 2)
statistics_printer(fred)
statistics_printer(starter)

After turning a textfile into the 2D List, it can be turned into class instances:
employees = [Employee(n) for n in file_read[0])]

Could create a coach functionality with the ability to create and alter the line up
Sign in to the database, with TXT file usage. different priveleges for different levels. occupation should be shown.

Could do an entire python file that is imported that includes all instantiations, rather than the TXT file for now.
'''
