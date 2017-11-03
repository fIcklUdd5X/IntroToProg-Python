#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   <YOUR NAME HERE>, ???, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

# objFileName = "C:\_PythonClass\Todo.txt"
objFileName = "C:\\Users\\Stefan\\Python_Files\\UW_Python\\Mod_1_05\\Todo.txt"
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

import sys

def read_file(file_direct):
    """
    file line is separated by new line '\n'. line is ',' delimited,
    mode is 'r
    returns a list read_data, each line in file is a str.
    '"""

    try:
        with open(file_direct, 'r') as f:
            read_data = f.read()
        read_data = read_data.splitlines()
#        print("read-file object closed? : ", file_object.closed)
        return read_data
    except:
        e = sys.exc_info()[0]
        print("<p>Error: {}</p>".format(e))


def data_to_dict_of_lines(data, sep):
    """
    dicRow = A row of data separated into elements of a dictionary {Task,Priority}
    """
    dicRow = dict()
    for line in data:
        key, value = line.split(sep)
        key, value = key.strip(), value.strip()
        dicRow[key] = value
    return dicRow


def dict_of_line_to_table_of_rows(dict_of_rows, lstTable={}):
    """
    lstTable = A dictionary that acts as a 'table' of rows, {key:list[values]} or here {Priority:list[Task]}
    """

    for task, priority in dict_of_rows.items():
        if priority in lstTable:
            lstTable[priority].append(task)
        else:
            lstTable[priority] = [task]
    return lstTable

# Step 2 - Display a menu of choices to the user

def menue_options():

    menue_dict = {1: 'Show current data',
                  2: 'Add a new item',
                  3: 'Remove an existing item',
                  4: 'Save Data to File',
                  5: 'Exit Program'}

    print("\nMenu of Options:")
    for key in menue_dict:
        print(key, ')  ', menue_dict[key])
    return menue_dict


def menue():
    """display options available and return the choice.
        strChoice is int 1 - 5."""

    menue_dict = menue_options()

    print_arg_1 = None
    print_arg_2 = "\nWhich option would you like to perform? [1 to 5] - "
    valid_args = 1, 2, 3, 4, 5,

    strChoice = exception_catcher(valid_args, print_arg_1, print_arg_2)
    print('\nYour choice: \n{} )  {}\n'.format(strChoice, menue_dict[int(strChoice)]))
    return strChoice

    # Step 3 -Show the current items in the table
    # if (strChoice.strip() == '1'):

def display_data(data):
    """
    displays information currently ready
    :param data: dictionary; key = urgency, list of tasks
    :return: none
    """
    for key in data:
        for item in data[key]:
            if item is None:
                print('{:7}  :  {}'.format(key, None))
            else:
                print('{:7}  :  {}'.format(key, item))


def exception_catcher(valid_args, print_arg_1=None, print_arg_2=None):
    # strChoice = input("\nWhich option would you like to perform? [1 to 5] - ") ==> integer
    # NEXT, catch when , is missing as separator for choice 2: 'Add a new item'.
    print_args = {1: print_arg_1, 2: print_arg_2}
    valid_choice = False
    while not valid_choice:
        if print_arg_1 != None:
            print(print_args[1])
        if print_arg_2 != None:
            in_put = input(print_args[2])
            try:
                in_put = int(in_put)
                if in_put in valid_args:
                    valid_choice = True
                elif in_put not in valid_args:
                    print("You entered: {} but needs to be 1 - 5.".format(in_put))
                    #                in_put in valid_args
                    #                    = "split, strip, is number 1 - 5" #
            except (TypeError, ValueError):
                print("Enter a digit, 1 - 5")

    return str(in_put)


    # Step 4 - Add a new item to the list/Table
    # elif(strChoice.strip() == '2'):

def add_item(data):
    """
    add new item to current
    :param data:  dictionary; key = urgency, list of tasks
    :return: data dictionary
    """

    print('Enter an activity and its urgency. \n'
          'Use the comma "," to separate the activity from the urgency.\n\n')

    str_user_input = input('Enter "activity" "," "urgency" and then "Enter": ')
    add_dicRow = data_to_dict_of_lines([str_user_input], ',')
    new_data = dict_of_line_to_table_of_rows(add_dicRow, data)
    data = new_data
    return data

    # Step 5 - Remove a new item to the list/Table
    # elif(strChoice == '3'):
    #    continue

def remove_from_data(data):

    usr_input = input("Enter activity you want to remove: ")
    boo = False
    for key in data.keys():
        value_list_lower = [value.lower() for value in data[key]]
        if usr_input.lower() in value_list_lower:
            indx = value_list_lower.index(usr_input.lower())
            print("Found {} entered as: {}". format(usr_input, [key][indx]))
        if usr_input.lower() not in value_list_lower:
            print("Nothing found entered as: {}". format(usr_input))
        if usr_input in data[key]:
            data[key].remove(usr_input)
            if usr_input in data[key]:
                print("Item is entered more than once as {}. To remove next one, enter 3 again.". format(usr_input))

    for key, value in data.items():
        if data[key] is not []:
            data[key] = value
    return data

    # Step 6 - Save tasks to the ToDo.txt file

def save_to_file(data, file_address):
    """ 'w' for only writing (an existing file with the same name will be erased) """

    print("Saving data to file.")
    with open(file_address, 'w') as file_object:
        for key, value in data.items():
            for item in data[key]:
                str_write = item + ',' + key + '\n'
                file_object.write(str_write)
    print("file object closed? : ", file_object.closed)
    return data

    # elif (strChoice == '5'):
    #     break #and Exit the program

def exit(data):
    # save data to file before Exit?
    return  False


def run_asmt_5(file_location):
    # Data
    fd = read_file(file_location)
    separator = ','
    tab1 = data_to_dict_of_lines(fd, separator)
    data = dict_of_line_to_table_of_rows(tab1)

    do_dict = {1: display_data,
               2: add_item,
               3: remove_from_data,
               4: save_to_file,
               5: exit}

    temp = True
    while temp:

        choice = menue()  # choice receives a number 1 to 5 in str format
        if choice == '1' or choice == '2' or choice == '3':
            do = do_dict[int(choice)](data)
        elif choice == '4':
            do = do_dict[int(choice)](data, file_location)
        elif choice == '5':
            temp = do_dict[int(choice)](data)
        else:
            print('Problem at "choice = menue()".')


file_location = "C:\\Users\\Stefan\\Python_Files\\UW_Python\\Mod_1_05\\Todo.txt"
run_asmt_5(file_location)

print('Finished')
