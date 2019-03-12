def statistics_printer(class_name):
    if isinstance(class_name, (Goalies, Skaters)):
        print("\n\n")
        for x in class_name.all_stats:
            print(x + ": " + str(class_name.all_stats[x]))
    else:
        print("restart")


employee_dict = {}  # FIND A WAY TO INCORPORATE WITHIN A CLASS


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        employee_dict[self.name] = self.salary  # IF POSSIBLE, FIND A WAY TO GET LINE 10 INCORPORATED.


class Skaters(Employee):
    def __init__(self, name, age, salary, position, goals, shots_on_goal, assists, penalty_minutes, games_played):
        super().__init__(name, age, salary)
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


class Goalies(Employee):
    def __init__(self, name, age, salary, shots_against, saves, shutouts, wins, losses):
        super().__init__(name, age, salary)
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


class Vendor:
    def __init__(self, name):
        self.name = name
        self.employee_list = []
        self.product_offerings = {}

    def add_product(self):  # BEING ABLE TO SPECIFY NUMBER OF PRODUCTS TO ADD, USING LEN. ALSO, BEING ABLE TO REMOVE
        # PRODUCTS.
        while True:
            product = input("New Product: ")
            if product.isdigit():
                print("Enter a product to be sold, not a number.")
                continue
            if product.title() in self.product_offerings:
                print("The " + self.name + " already has that product")
                continue
            try:
                price = int(input("Enter the price of " + product.title() + ": "))
                if price <= -1:
                    continue
            except ValueError:
                print("Enter a price")
                continue
            break
        self.product_offerings[product.title()] = price

    def product_display(self):
        print("\n\nThese are the available items at " + self.name + ":")
        for x in self.product_offerings:
            print("\nItem: " + x + "\nPrice: " + str(self.product_offerings[x]))


class GeneralManager(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.vendor_list = []

    def payroll_viewer(self):
        print("\n")
        total_payroll = 0
        for x in employee_dict:
            print(x + "'s salary: " + str(employee_dict[x]))
        for x in employee_dict:
            total_payroll += employee_dict[x]
        print("\nThe total payroll is " + str(total_payroll))

    def vendor_creation(self):  # NEEDS WORK
        vendor_name = input("What is the name of the new vendor: ").title()
        Vendor(vendor_name)
        self.vendor_list.append(vendor_name)

    def vendor_removal(self):  # NEEDS WORK
        while True:
            removal_name = input("What vendor do you want to remove: ").title()
            if removal_name in self.vendor_list:
                self.vendor_list.remove(removal_name)
                break

    def offerings_for_all_vendors(self):  # NEEDS WORK
        for x in self.vendor_list:
            current = Vendor(x)
            print(current.product_display())


starter = Goalies("Frederick Andersen", 29, 5000000, 100, 95, 2, 8, 2)
carl = Employee("H", 20, 5)
b = Employee("A", 20, 99)

dubas = GeneralManager("Kyle", 22, 8)
dubas.payroll_viewer()
team_merch = Vendor("Merchandise")
team_merch.add_product()
team_merch.add_product()
pizza = Vendor("Pizza Pizza")
pizza.add_product()
pizza.add_product()





# fred = Employee("Frederick Andersen", 29, 5000000)
# starter = Goalies(fred.name, fred.age, fred.salary, 100, 95, 2, 8, 2)
# statistics_printer(fred)
# statistics_printer(starter)


# Could create a coach functionality with the ability to create and alter the line up
# Sign in to the database, with TXT file usage. different priveleges for different levels. occupation should be shown.

