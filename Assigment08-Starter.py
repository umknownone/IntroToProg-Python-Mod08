# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# DAlexandrov,11.26.2019,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name \n
        product_price: (float) with the products's standard price

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class \n
        DAlexandrov,11.26.2019,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class

    def __init__(self, product_name: str, product_price: float):
        self.__product_name = product_name
        self.__product_price = product_price

    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, product_name):
        if str(product_name).isnumeric():
            raise Exception("Name of product cannot be numeric.")
        else:
            self.__product_name = product_name

    @property
    def product_price(self):
        return float(self.__product_price).__abs__()

    @product_price.setter
    def product_price(self, value):
        self.__product_price = value

    def __str__(self):
        return self.product_name + ", $%.2f" % self.product_price

    def to_string(self):
        return self.__str__()

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects): \n
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class \n
        DAlexandrov,11.26.2019,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        file = open(file_name, "w")
        for row in list_of_product_objects:  # Write each row of data to the file
            file.write(str(row) + "\n")
        file.close()

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        """
          Desc - Reads data from file, creates a new object for each product and adds that to a list of product objects \n
          :param file_name: (string) with name of file:
          :return: (list) of product objects
        """
        while (True):
            try:
                file = open(file_name, "r")  # Tries to read the file
                break
            except FileNotFoundError:  # If the file isn't found, throws an exception and creates the file and restarts the program
                print()
                print("Cannot find file, creating the " + file_name + " file and restarting...")
                file = open(file_name, "x")
                continue
        file = open(file_name, "r")
        for row in file:
            data = row.split(", $")
            newObj = Product(data[0], float(data[1]))
            lstOfProductObjects.append(newObj)
        file.close()
        return lstOfProductObjects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """A class for performing any input/output:

    methods:
        static: show_menu_items(): -> shows menu of options \n
        static: user_menu_input(): -> (string) of user menu choice \n
        static: show_current_products(list_of_product_objects): prints out current products in list of product objects \n
        static: user_new_item_input(product_name, product_price): -> (list) of product objects


    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class \n
        DAlexandrov,11.26.2019,Modified code to complete assignment 8
    """
    pass
    # TODO: Add code to show menu to user
    @staticmethod
    def show_menu_items():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
            Menu of Options
            1) Show current data
            2) Add a new item.
            3) Save Data to File
            4) Exit Program
            ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def user_menu_input():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def show_current_products(list_of_product_objects):
        """ Shows the current products in the list of product objects
        :param list_of_product_objects: (list) of objects you want to display
        :return: nothing
        """
        print("******* The current products are: *******")
        for obj in list_of_product_objects:
            print(obj.to_string())
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def user_new_item_input(product_name, product_price):
        """
        Desc - Writes data from a list of dictionary rows into a file
        :param product_name: (string) with user product name input:
        :param product_price: (float) with user product price input:
        :return: (list) of product objects
        """
        new_product_object = Product(product_name, product_price)
        lstOfProductObjects.append(new_product_object)  # Add the new row to the list/table
        return lstOfProductObjects
# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

FileProcessor.read_data_from_file(strFileName) # Load data from file into a list of product objects when script starts
while(True):
    IO.show_menu_items() # Show user a menu of options
    str_user_choice = IO.user_menu_input() # Get user's menu option choice

    if(str_user_choice.strip() == "1"): # Show user current data in the list of product objects
        IO.show_current_products(lstOfProductObjects)
        continue

    elif(str_user_choice.strip() == "2"): # Let user add data to the list of product objects
        str_user_product = input("What is the name of the new product you would like to add? ")
        flt_user_price = input("What is the price of the new product that you would like to add? ")
        try:
            IO.user_new_item_input(str_user_product, float(flt_user_price))
        except ValueError as e:
            print()
            print("****** ERROR *******")
            print("Non-numeric value was input for the price. Expecting integer or float.")
        finally:
            continue
        IO.show_current_products(lstOfProductObjects)
        continue

    elif (str_user_choice.strip() == "3"): # let user save current data to file and exit program
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print("Your data has been saved!")
        continue

    elif (str_user_choice.strip() == "4"): # let user exit the program
        print("Exiting...")
        break

    else:
        if not str_user_choice.strip().isnumeric(): # if user input was not numeric
            raise Exception("User input was not a number. Please only choose a number from the menu of options.")
        else:
            print("Invalid choice, please choose an item from the menu.") # if user input was numeric but out side the bounds of menu items
        continue

# Main Body of Script  ---------------------------------------------------- #

