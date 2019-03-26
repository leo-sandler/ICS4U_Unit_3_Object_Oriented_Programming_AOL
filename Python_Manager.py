employee_dict = {}  # HELP, MAKE THIS NOT GLOBAL


class Employee:
    def __init__(self):
        self.name = self.name_input()
        self.age = self.age_input()
        self.salary = self.salary_input()
        employee_dict[self.name] = self.salary

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

    def pay_raise(self):
        print(self)  # NEED TO FIGURE OUT WHAT CLASS THIS IS BEING CALLED BY. SHOULD BE RESTRICTED TO ONLY THE
        # GM OR A RETAIL MANAGER.COULD HAVE A CLASSNAME VARIABLE, WHICH IS CHECKED TO ENSURE THAT SELF.CLASSNAME
        # MEETS THE REQUIREMENTS.
        while True:
            employee_choice = input("What employee do you want to give a pay raise to: ")
            if employee_choice in employee_dict:
                try:
                    raise_amount = int(input("How large is the raise: "))
                    if raise_amount >= 1:
                        employee_dict[employee_choice].salary += raise_amount
                        employee_dict[employee_choice] += raise_amount
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
                if a_or_r == "A":
                    number_of_products = int(input("How many products do you want to add: "))
                if a_or_r == "R":
                    number_of_products = int(input("How many products do you want to remove: "))
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
                self.product_offerings[product.title()] = price
            if a_or_r == "R":
                product = input("Product: ")
                if product.isdigit():
                    print("Enter a product, not a number.")
                    continue
                if product.title() in self.product_offerings:
                    del self.product_offerings[product.title()]
                    print(str(product) + " was removed from this vendor.")
            count += 1

    def remove_product(self):
        while True:
            try:
                number_of_products = int(input("How many products do you want to remove: "))
                if number_of_products <= 0:
                    print("Enter a number higher than 0.")
                    continue
                break
            except ValueError:
                print("Enter a number please.")
                continue
        count = 0
        while count < number_of_products:
            product = input("What do you want to remove: ").title()
            if product in self.product_offerings:
                del self.product_offerings[product]
                count += 1

    def product_display(self):
        print("\nThese are the available items at " + self.name + ":")
        for x in self.product_offerings:
            print("\nItem: " + x + "\nPrice: " + str(self.product_offerings[x]))


class GeneralManager(Employee):
    def __init__(self):
        super().__init__()
        self.vendor_list = []
        self.vendor_dict = {}

    def all_options(self):
        while True:
            try:
                choice = int(input("1) Payroll Viewer\n2) Vendor Creation\n3) Vendor Removal\n4) Offerings in Each "
                                   "Vendor\n5) Employee Hiring\n6) Employee Firing"))
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
                    exit()
                else:
                    self.all_options()
            except ValueError:
                continue

    def payroll_viewer(self):
        print("\n")
        total_payroll = 0
        for x in employee_dict:
            print(x + "'s salary: " + str(employee_dict[x]))
        for x in employee_dict:
            total_payroll += employee_dict[x]
        print("\nThe total payroll is " + str(total_payroll))

    def vendor_creation(self):
        vendor_name = input("What is the name of the new vendor: ").title()
        vendor = Vendor(vendor_name)  # THIS IS THE INSTANTIATION THAT MUST BE ACCESSED AGAIN.
        self.vendor_dict[vendor_name] = vendor
        vendor.add_product()
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
            if removal_name in self.vendor_list:
                self.vendor_list.remove(removal_name)
                break

    def vendor_products(self):
        while True:
            vendor_name = input("Enter the name of the vendor you want to edit: ").title()
            if self.vendor_dict[vendor_name]:
                add_or_remove = input("Do you want to add or remove products: ").title()
                if add_or_remove == "Add":
                    self.vendor_dict[vendor_name].add_product()
                if add_or_remove == "Remove":
                    self.vendor_dict[vendor_name].remove_product()
                else:
                    continue

    def offerings_for_all_vendors(self):
        for x in self.vendor_list:
            x.product_display()

    def hiring(self):
        job = int(input("\nThese are the available positions to hire for.\n1) Skater\n2) Goalie\n3) Coach\n4) "
                        "Vendor Employee\n5) Maintenance Employee\nYour Choice: "))
        '''
        if job == 1:
            Skater()
        if job == 2:
            Goalie()
        '''
        if job == 3:
            print("NEED COACH")
        if job == 4:
            print("NEED VENDOR EMPLOYEES")
        if job == 5:
            print("NEED MAINTENANCE EMPLOYEES")


    def firing(self):
        print("FIRE")


dubas = GeneralManager()
dubas.vendor_creation()
dubas.vendor_products()



print(dubas.__class__.__name__)  # PRINTING THE NAME OF THE INSTANTIATED CLASS

isinstance(dubas, GeneralManager)  # Checking if dubas is an instance of the class GeneralManager. Returns true.




# fred = Employee("Frederick Andersen", 29, 5000000)
# starter = Goalie(fred.name, fred.age, fred.salary, 100, 95, 2, 8, 2)
# statistics_printer(fred)
# statistics_printer(starter)

# After turning a textfile into the 2D List, it can be turned into class instances:
# employees = [Employee(n) for n in file_read[0])]


# Could create a coach functionality with the ability to create and alter the line up
# Sign in to the database, with TXT file usage. different priveleges for different levels. occupation should be shown.

# Could do an entire python file that is imported that includes all instantiations, rather than the TXT file for now.
