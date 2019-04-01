import os


class Employee:
    def __init__(self, name, age, salary, job):  # Class initialization, with parameters
        self.name = name
        self.age = age
        self.salary = salary
        self.job = job  # The 4 attributes are input through parameters.

    '''
    The employee class is used to store data for the managed employees. They are instantiated above through
    parameters. The employee function contains static methods to fill these parameters. Also, there is another 
    staticmethod to update the TXT file after multiple employee-related actions are made.
    '''

    @staticmethod  # All methods tagged with staticmethod do not include self in execution, but relate to the class.
    def name_input():
        while True:
            name = input("What is the employee's name: ").title()  # Preventing capitalization errors.
            if name.isdigit():
                print("Enter a name, not a number.")
                continue  # Restarting the while loop, as the employee name cannot be a number.
            return name  # The employee's name is returned.

    @staticmethod
    def age_input():
        while True:
            try:
                age = int(input("What is the employee's age: "))
                if age <= 13:  # Sensing age, with less than or equal to
                    print("It is not legal to have workers aged under 14.")  # Notifying user.
                    continue  # Restarting the while loop.
                if age >= 122:
                    print("The oldest person ever passed away at 122 years old. Enter a younger age.")
                    continue
                return age  # Returning the value to the user.
            except ValueError:  # Error sensing, if the user enters a string into the input.
                print("Enter a number for employee age.")
                continue

    @staticmethod
    def salary_input():
        while True:  # While loop initialization.
            try:
                salary = int(input("What is the employee's salary: $"))
                if salary <= 0:  # Sensing the value.
                    print("Employees must be paid a positive amount.")
                    continue  # Restarting the loop, due to invalid input.
                return salary
            except ValueError:  # Except, used in the same way as age.
                print("Enter in a number for employee salary.")
                continue

    '''
    These 3 input functions are used to return data that is used when the Employee class is instantiated. They contain 
    while loops, and try + except statements for defensive programming. Inputs are returned after passing through
    defensive programming.
    '''

    @staticmethod
    def employee_file_updating(action, name, age, salary, job):  # Parameters are within this function. However,
        # self is not included within them. Therefore, this is a staticmethod.
        employee_2d_list = file_into_2d_list("Employees")  # Turning the employee file into a 2d list via a function.
        employee_2d_list.sort(key=lambda z: float(z[2]), reverse=True)  # Sorting the 2d list by column 2, which stores
        # employee salary within the text file. Numbers are sorted as floats, rather than integers(in order to sense
        # number length). The sort is reversed to sort from highest to lowest.
        emp_file = open("Employees.txt", "w")
        if action == "ADD_EMP":  # Sensing for the parameter, using an if statement.
            employee_2d_list.append([name, age, salary, job])  # Adding the new employee to the 2d list.
            employee_2d_list.sort(key=lambda z: float(z[2]), reverse=True)  # Sorting again, as an employee
            # is added to the list, and may have a higher salary than some others.
        if action == "DEL_EMP":
            for x in range(len(employee_2d_list)):
                if name == employee_2d_list[x][0]:
                    employee_2d_list.pop(x)  # Removing this employee from the list, according to the action parameter.
        if action == "EMP_PAY":
            for n in range(len(employee_2d_list)):
                if employee_2d_list[n][0] == name:  # Checking where the existing employee is in the 2d list, so their
                    # salary can be changed.
                    employee_2d_list[n][2] = salary  # Changing the value of the list section to the updated salary.
                    employee_2d_list.sort(key=lambda z: float(z[2]), reverse=True)  # Sorting again, as an employee
                    # salary value has changed.
        for x in range(len(employee_2d_list)):
            emp_file.writelines(','.join(str(y) for y in employee_2d_list[x]) + "\n")  # Writing the list to the
            # text file via write lines and list comprehension.
        emp_file.close()  # File closing.
        last_line_deleting("Employees")  # Calling the function to remove the last newline character from the file.

    '''
    The employee_file_updating function is used to update the text file following class-based actions involving 
    employees. A 2d list is used to store and manipulate data. This list is then written to the text file following 
    a change. The parameters include an action, relating to data input relating to an employee. If statements are used
    to sense for this parameter, and execute the proper operation. 
    '''


class GeneralManager(Employee):  # This class inherits from the Employee class.
    def __init__(self):
        super().__init__(name="Kyle Dubas", age=33, salary=1500000, job="General Manager")  # super() is used to
        # fulfill the 4 parameters from the employee class. As well, I set these 4 values to the same thing, as there
        # is only one General Manager. Therefore, the "=" signs allow for me to instantiate this class in the same
        # way each time.
        self.vendor_products_dict = {}  # Storing products and prices at key values of vendors.
        self.vendor_instances = {}  # Storing the vendor class instantiation location at the key of the vendor's name.
        self.employee_dict = {}  # Storing the age, salary, and position data at the key of the employee's name.
        self.employee_file_reading()
        self.vendor_file_reading()  # These 2 file_reading functions transfer data from text files and include them in
        # various classes.

    '''
    The GeneralManager class is used to control this file. The user takes the position of the manager, and all decisions
    are made from this perspective. Dictionaries are used to store data detailing the vendors and employees that are 
    managed by the GM.
    '''

    def employee_file_reading(self):
        employee_2d_list = file_into_2d_list("Employees")  # Function call, with the employee text file.
        employee_2d_list.sort(key=lambda z: float(z[2]), reverse=True)  # Sorting the file, by salary.
        for x in range(0, len(employee_2d_list)):  # For loop, through the 2d list.
            self.employee_dict[employee_2d_list[x][0]] = [int(employee_2d_list[x][1]), int(employee_2d_list[x][2]),
                                                          employee_2d_list[x][3]]
            # Dictionary which has the key of employee name. The value stored is a list of the employee age, salary, and
            # position(in that order, due to the 2d list).

    '''
    The employee text file is turned into a 2d list. After this, the data is stored within the employee dictionary.
    '''

    def vendor_file_reading(self):
        vendor_2d_list = file_into_2d_list("Vendors")  # Turning the file into a 2d list.
        vendor_2d_list.sort(key=lambda z: (z[0]), reverse=False)  # Sorting by vendor name.
        for x in range(0, len(vendor_2d_list)):
            self.vendor_instances[vendor_2d_list[x][0]] = Vendor(vendor_2d_list[x][0])  # Storing vendor instances
            # at the dictionary key corresponding to their name.
            y = 0  # Count variable
            while True:  # Initializing a while loop.
                try:
                    if y % 2 == 1:  # Sensing for an odd number
                        product = vendor_2d_list[x][y].strip(" '" + "['")  # If odd, taking from the product list
                        # ,according to indexes which are separated by commas.
                        price = int(vendor_2d_list[x][y + 1].strip("']"))  # The next even number after corresponds to
                        # the product's price, which is stored as an integer within the product offerings dict.
                        (self.vendor_instances[vendor_2d_list[x][0]]).product_offerings[product] = price  # First, the
                        # vendor instance location is accessed. This is used to add a new product within the product_
                        # offerings dict. The keys for this dictionary are the product, with the key value of price.
                except IndexError:  # Exception, if y becomes too high.
                    break  # If the exception is met, the loop is broken.
                y += 1  # Reiterating increase.

    '''
    The vendor text file is turned into a 2d list, and then stored within multiple dictionaries. This code is different
    than the employee reading. Therefore, I put it into a separate function. However, the purpose of this function
    is the same as the employee file reading.
    '''

    def all_options(self):
        while True:
            try:
                choice = int(input("\n1) Payroll Viewer\n2) Vendor Creation\n3) Vendor Removal\n4) Add/Remove Vendor "
                                   "Products\n5) Offerings in Each Vendor\n6) Employee Hiring\n7) Employee Firing\n"
                                   "8) Employee Pay Raise\n9) Employee Pay Cut\n10) EXIT\nYour Choice: "))  # The
                # options for this input are displayed to the user.
                if choice == 1:  # Corresponding choices are sensed.
                    self.payroll_viewer()  # Functions are called as a result of choices.
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
                    self.pay_raise_or_cut("R")
                if choice == 9:
                    self.pay_raise_or_cut("C")
                if choice == 10:
                    exit("Code Exited.")
                else:
                    continue
            except ValueError:  # This except will trigger if the user enters a string.
                continue  # Restarting the loop.

    '''
    This function is the hub/menu for this code. It is called once within the managing() function. It is the only call
    made within the managing function, as it grants access to all functionality within the code. A while loop with 
    try and except is used for defending inputs. Also, if statements sense for user selections.
    '''

    def payroll_viewer(self):  # The first option within the all_options function.
        total_payroll = 0  # Setting the payroll to 0, which will be increased in the for loop.
        print("\nSalaries are printed in order of salary, from highest to lowest.\n")  # Notifying the user.
        for x in self.employee_dict.keys():  # Looping through the employee dictionary.
            print(self.employee_dict[x][2] + ": " + x + "'s salary is $" + "{:,}".format(self.employee_dict[x][1]))
            # First, the employee's position is shown. Next, their name is shown. Finally, their salary is shown with
            # formatting to add commas to synchronize with thousands.
            total_payroll += self.employee_dict[x][1]  # Reiterating increase to the total payroll, through the
            # accessing the dictionary.
        print("\nThe total payroll is $" + "{:,}".format(total_payroll))  # Showing the user total payroll.

    '''
    The payroll_viewer function loops through the employee dictionary to display employee position, name, and salary.
    After this, the payroll value is increased each time the loop executes through a reiterating increases. This 
    function ends with the displaying of the combined payroll.
    '''

    def vendor_creation(self):  # The second option within the all_options function.
        while True:
            vendor_name = input("\nWhat is the name of the new vendor: ").title()  # Vendor name input, with .title()
            # for capitalization consistency.
            if vendor_name not in self.vendor_instances.keys():  # Checking if the vendor does not exist already.
                vendor = Vendor(vendor_name)  # Instantiating a vendor with the name parameter filled through the input.
                self.vendor_instances[vendor_name] = vendor  # Adding to the vendor_instances dictionary.
                vendor.add_or_remove_products("A", True)  # Adding products to the new vendor.
                break

    '''
    The vendor_creation function uses a user input to create an instance of the Vendor class. Products are added
    to the vendor. Also, the dictionary and the text file are updated.
    '''

    def vendor_removal(self):  # The third option within the all_options function.
        while True:
            removal_name = input("\nWhat vendor do you want to remove: ").title()  # Sensing for which vendor is
            # being removed.
            if removal_name in self.vendor_products_dict:  # Checking that the vendor exists already.
                self.vendor_instances[removal_name].vendor_file_updating("Removal")  # Updating the text file.
                del self.vendor_products_dict[removal_name]
                del self.vendor_instances[removal_name]  # Removing this vendor from both dicts.
                break  # Ending the while loop.

    '''
    The vendor_removal function uses a user input to remove an instance of the Vendor class. The text file is updated
    along with both dictionaries. This uses a while loop for continual input until the condition(the fact that the 
    vendor already exists) is satisfied.
    '''

    def vendor_products(self):  # The fourth option within the all_options function.
        while True:  # Starting a while loop
            vendor_name = input(str("Enter the name of the vendor you want to edit: ")).title()
            for x in self.vendor_instances.keys():
                if x == vendor_name:  # Checking if the vendor exists.
                    add_or_remove = input("(Add/Remove)Do you want to add or remove products: ").title()
                    if add_or_remove == "Add":
                        self.vendor_instances[x].add_or_remove_products("A", False)  # Calling the add function
                        # according to the vendor instance within the loop.
                        break
                    if add_or_remove == "Remove":
                        self.vendor_instances[x].add_or_remove_products("R", False)  # Calling the removal in the same
                        # way as the adding above. The new value is false, because this is for an existing vendor.
                        break  # Breaking the for loop.
            break  # Breaking the while loop

    '''
    The vendor_products function uses a for loop to sense if a user inputted vendor exists. If it does, then the same
    function is called with a different parameter based upon whether the user preference. A while loop asks for a vendor
    name until it the conditions are met.
    '''

    def offerings_for_all_vendors(self):  # The fifth option within the all_options function.
        for x in self.vendor_instances.keys():  # Cycling through all vendor instances.
            self.vendor_instances[x].product_display()  # Calling the product display function according to each
            # vendor instance.

    '''
    The offerings_for_all_vendors function cycles through the vendor instances and displays their products.
    '''

    def hiring(self):  # The sixth option within the all_options function.
        while True:  # While loop
            position = int(input("\nThese are the available positions to hire for.\n1) Vendor Employee\n2) "
                                 "Vendor Manager\n3) Head Coach\n4) Assistant Coach\n5) EXIT\nYour Choice: "))
            name = self.name_input()  # Using Employee static methods to store data. The methods function with self
            # as a result of the inheritance.
            age = self.age_input()
            salary = self.salary_input()
            job = ""  # Initializing a string.
            if name not in self.employee_dict:  # If the employee does not exist.
                if position == 1:
                    job = "Vendor Employee"
                if position == 2:
                    job = "Vendor Manager"
                if position == 3:
                    job = "Head Coach"
                if position == 4:
                    job = "Assistant Coach"  # Employee job is set through changing the string.
                if position == 5:
                    exit()
                Employee(name, age, salary, "Assistant Coach")  # Making an instance of the employee class.
                self.employee_dict[name] = [age, salary, job]  # Updating the dictionary stored within GM for this new
                # employee.
                self.employee_file_updating("ADD_EMP", name, age, salary, job)  # Updating the text file.
                break

    '''
    The hiring uses a while loop for position selection. The employee's attributes are set through static methods from
    inheritance. After this, the dictionary and text file is updated.
    '''

    def firing(self):  # The seventh option within the all_options function.
        while True:
            employee_choice = input("What employee do you want to fire: ").title()  # .title() for capitalization.
            if employee_choice in self.employee_dict:  # Checking that the employee exists.
                self.employee_file_updating("DEL_EMP", employee_choice, self.employee_dict[employee_choice][0], self.
                                            employee_dict[employee_choice][1], self.employee_dict[employee_choice][2])
                # Employee file is updated, through deleting this employee.
                del self.employee_dict[employee_choice]  # The employee is deleted from the dictionary.
                break

    '''
    The firing funciton checks if the selected employee exists, then removes them from the dictionary and text file.
    '''

    def pay_raise_or_cut(self, r_or_c):  # The eighth and ninth option within the all_options function.
        while True:
            employee_choice = input("Whose pay do you want to raise/cut: ").title()
            if employee_choice in self.employee_dict.keys():  # Checking if the employee exists.
                try:  # Try statement.
                    if r_or_c.upper() == "R":  # Pay raise sensing.
                        raise_amount = int(input("How large is the raise: $"))
                        if raise_amount >= 1:  # Checking if the raise is higher than 1.
                            self.employee_dict[employee_choice][1] += raise_amount
                            self.employee_file_updating("EMP_PAY", employee_choice, self.employee_dict[employee_choice]
                                                        [0], self.employee_dict[employee_choice][1], self.employee_dict
                                                        [employee_choice][2])
                            print("Raised " + employee_choice + "'s pay by $" + str(raise_amount))  # Notifying user.
                        break
                    if r_or_c.upper() == "C":
                        cut_amount = int(input("How large is the cut: $"))
                        if 1 <= cut_amount < self.employee_dict[employee_choice][1]:  # Checking if the raise
                            # is larger than 1, but lower than the employee's salary.
                            self.employee_dict[employee_choice][1] -= cut_amount  # Subtraction of employee salary
                            self.employee_file_updating("EMP_PAY", employee_choice, self.employee_dict
                                                        [employee_choice][0], self.employee_dict[employee_choice][1],
                                                        self.employee_dict[employee_choice][2])
                            print("Cut " + employee_choice + "'s pay by $" + str(cut_amount))
                        break
                except ValueError:  # Exception if the value entered is a string, not an integer.
                    print("Enter a number into the raise amount.")
                    continue

    '''
    The pay raise or cut function first check if the selected employee exists. If it does, then the selected option
    is executed according to the parameter. The inputs are defended through if statements + try and except. A while 
    loop continues to ask for an employee to raise/cut until one exists.
    '''


class Vendor:
    def __init__(self, name):
        self.name = name  # Vendor name attribute, filled through the parameter during initialization.
        self.product_offerings = {}

    def add_or_remove_products(self, a_or_r, new):
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
                product = input("\nNew Product: ").title()
                if product.isdigit():
                    print("Enter a product to be sold, not a number.")
                    continue
                if product in self.product_offerings:
                    print("The " + self.name + " vendor already has that product")
                    continue
                try:
                    price = int(input("Enter the price of " + product + ": $"))
                    if price <= 0:
                        continue
                except ValueError:
                    print("Enter a price.")
                    continue
                self.product_offerings[product] = price
                print(product + " was added to the " + self.name + " vendor.")
            if a_or_r == "R":
                product = input("\nProduct: ").title()
                if product.isdigit():
                    print("Enter a product, not a number.")
                    continue
                if product in self.product_offerings:
                    del self.product_offerings[product]
                    print(str(product) + " was removed from this vendor.")
            count += 1

        if new:
            self.vendor_file_updating("Creation")
        elif not new:
            self.vendor_file_updating("Modification")

    def product_display(self):
        print("\nThese are the available items at " + self.name + ":")
        for x in self.product_offerings:
            print("\nItem: " + x + "\nPrice: $" + str(self.product_offerings[x]))

    def vendor_file_updating(self, reason):
        vendor_offerings_list = []
        for k, v in self.product_offerings.items():
            vendor_offerings_list.append(str(k) + "," + str(v))
        vendor_offerings_list.sort()
        vendor_2d_list = file_into_2d_list("Vendors")
        for x in range(len(vendor_2d_list)):
            if reason == "Creation":
                if self.name not in vendor_2d_list:
                    vendor_2d_list.append([self.name, str([y for y in vendor_offerings_list])])
                    break
            elif reason == "Modification":
                vendor_2d_list[x] = ([self.name, str([y for y in vendor_offerings_list])])
                break
            elif reason == "Removal":
                vendor_2d_list.pop(x)
                break
        vendor_2d_list.sort(key=lambda z: (z[0]), reverse=False)
        vend_file = open("Vendors.txt", "w")
        for n in range(len(vendor_2d_list)):
            vend_file.writelines(','.join(str(y) for y in vendor_2d_list[n]) + "\n")
        vend_file.close()
        last_line_deleting("Vendors")


def file_into_2d_list(filename):
    opening = open(str(filename) + ".txt", "r")
    final_2d_list = [x.split(",") for x in opening.read().split("\n")]
    opening.close()
    return final_2d_list


def last_line_deleting(file):
    reading = open(str(file) + ".txt", "rb+")
    reading.seek(-2, os.SEEK_END)
    reading.truncate()
    reading.close()


def managing():
    kyle_dubas = GeneralManager()
    print("The function below gives you multiple options for controlling vendors and employees.\nYou have the role of"
          "Kyle Dubas, the 33 year old general manager of the Toronto Maple Leafs.")
    kyle_dubas.all_options()


managing()
