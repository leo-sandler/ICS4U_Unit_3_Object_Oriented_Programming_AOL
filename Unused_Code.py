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

'''
fred = Employee("Frederick Andersen", 29, 5000000)
starter = Goalie(fred.name, fred.age, fred.salary, 100, 95, 2, 8, 2)

After turning a textfile into the 2D List, it can be turned into class instances:
employees = [Employee(n) for n in file_read[0])]

Could create a coach functionality with the ability to create and alter the line up
Sign in to the database, with TXT file usage. different priveleges for different levels. occupation should be shown.

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

'''

'''
if reason == "Creation":
    vendor_file = open("Vendors.txt", "a")
    vendor_file.write(str(self.name) + "," + str([y for y in vendor_offerings_list]) + '\n')
    vendor_file.close()
if reason == "Removal":
    print("Remove")
if reason == "Modification":
    # NEEDS TO BE EDITED
    vendor_file = open("Vendors.txt", "w")
    vendor_file.write(str(self.name) + "," + str([y for y in vendor_offerings_list]) + '\n')
    vendor_file.close()
'''

'''
def statistics_printer(class_name):
    if isinstance(class_name, (Goalie, Skater)):
        print("\n\n")
        for x in class_name.all_stats:
            print(x + ": " + str(class_name.all_stats[x]))
    else:
        print("restart")


'''