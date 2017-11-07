# python 3

# Assignment_06_Stefan Lund
#-------------------------------------------------#

#-- Data --#


#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo_.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo_ items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo_.txt file

# Step 7
# Exit program
#-------------------------------

# objFileName = "C:\_PythonClass\Todo_.txt"
# objFileName = "C:\\Users\\Stefan\\Python_Files\\UW_Python\\Mod_1_05\\Todo_.txt"
# strData = ""
# dicRow = {}
# lstTable = []

#-- Processing --#
# Step 1
# When the program starts, load the any data you have       - read_file(file_direct)
# in a text file called ToDo_.txt into a python Dictionary.  - data_to_dictionary(data, sep, , lstTable={})

import sys


def read_file(file_direct, sep):
    """
        input file is (new line) '\n' delimited and each line is 'sep' delimited
        mode is (read) 'r'
        returns:
            if file exists and is not None, data, a dictionary of key = 'Priority' and value is a list of 'Task'
            if no file is found, returnvalue is not given but is read as None
    '"""

    try:
        with open(file_direct, 'r') as f:
            read_data = f.read()

        data = dict()
        read_data = read_data.splitlines()

        for line in read_data:
            add_str_to_data = line
            data_to_dictionary(data, add_str_to_data, sep)
        return data

    except: # catch all - not good but the best I can come up with for the moment.
            # if 'FileNotFoundError' == str(e).split("'")[1]:  Not a problem. File created when saved.
        e = sys.exc_info()[0]
        print("<p>Error: {}</p>".format(e))


def data_to_dictionary(data, add_str_to_data, sep):
    """
        :param data: dictionary of key = 'Priority' and value is a list of 'Task'
        :param add_str_to_data: string of 'Task , Priority'
        :param sep: separator, delimiter in 'add_str_to_data'

        return data: dictionary , {Priority1:list[Task1, Task2 ...], Priority2:list[Task3, Task4 ...]}
    """

    if add_str_to_data is None:
        return data

    else:
        key, value = add_str_to_data.split(sep)
        key, value = key.strip(), value.strip()

        # Switch! key  = Priority, value = Task.
        #  Think: dict[key = high] = ['Pay Bills', 'Wedding Anniversary', 'Homework Due']
        if data is None:
            data = dict()
        if value in data:
            data[value].append(key)
        else:
            data[value] = [key]
    return data


# Step 2 - Display a menu of choices to the user

def menu_options(prnt=1):
    """
    overloaded function
    options menue is a dictionary with int keys and lists of options to print and corresponding functions
    :param prnt: prints the options menue only if param prnt not given (or set to 1)
    :return: returns the options menue
    """

    menu_dict =  {1: ['Show current data', display_data],
                  2: ['Add a new item', add_item],
                  3: ['Remove an existing item', remove_from_data],
                  4: ['Save Data to File', save_to_file],
                  5: ['Exit Program', exit]}

    if prnt == 1:
        print("\nMenu of Options:")
        for key in menu_dict:
            print(key, ')  ', menu_dict[key][0])
    return menu_dict


def menu():
    """
        displays options available.
        uses exception_catcher() to verify user input is a valid choice.
        return:  choice made from available options, strChoice is int 1 - 5.
    """

    menu_dict = menu_options()

    valid_args = tuple(menu_dict.keys())
    valid_args_str = [str(item) for item in valid_args]
    print_arg_1 = None
    print_arg_2 = ("\nWhich option would you like to perform? [{} to {}]: ".
                   format(valid_args[0], valid_args[len(valid_args) - 1]))

    strChoice = exception_catcher(valid_args_str, print_arg_1, print_arg_2)
    print('\nYour choice: \n{} )  {}\n'.format(strChoice, menu_dict[int(strChoice)][0]))
    return strChoice

# Step 3
# Display all todo_ items to user


def display_data(data):
    """
    displays information currently ready
    :param data: dictionary; key = urgency, list of tasks
    :return: none
    """
    print('{:10}  :    {}\n{}'.format('Priority', 'Task', '-' * 30))
    if data is None:
        print("No data recorded. data @ display_data: {}".format(data))

    else:
        for key in data:
            for item in data[key]:
                if item is None:
                    print('{:10}  :    {}'.format(key, None))
                else:
                    print('{:10}  :    {}'.format(key, item))


def exception_catcher(valid_args, print_arg_1=None, print_arg_2=None):
    """

    :param valid_args: string format
                        from menu(), list of digits in string format
                        from add_item(), for the moment only the separator can be verified
    :param print_arg_1: string printed to screen
    :param print_arg_2: string used with the input() function
    :return: in_put, verified user input

    Set out to create a catch all function. Don't think it's a good idea. Too many moving parts.
    """

    import string
    valid_choice = False
    while not valid_choice:
        if print_arg_1 is not None:
            print(print_arg_1)
        if print_arg_2 is not None:
            in_put = input(print_arg_2)
            if ''.join(char for char in valid_args) in string.digits:
                if in_put in valid_args:
                    in_put = int(in_put)
                    valid_choice = True
                else:
                    print("Enter a digit, {} - {}".
                          format(in_put, valid_args[0], valid_args[len(valid_args) - 1]))

            elif ''.join(char for char in valid_args) in string.punctuation:
                if valid_args in in_put:
                    valid_choice = True
                else:
                    print('You forgot the {}'.format(valid_args))

            else:
                print("Add another elif selection to catch this input.")
                pass
    return str(in_put)


# Step 4 - Add a new item to the list/Table

def add_item(data):
    """
    add new item to current dictionary
    :param data:  dictionary; key = urgency, list of tasks, urgency can be words or numbers
    :return: data
    """

    valid_args = ","
    print_arg_1 = "Enter an activity and its priority.\n" \
                  "Use the comma ',' to separate the activity from the priority.\n\n"
    print_arg_2 = 'Enter "Activity" "," "Priority" and then "Enter": '
    str_user_input = exception_catcher(valid_args, print_arg_1, print_arg_2)
    data = data_to_dictionary(data, str_user_input, valid_args)
    return data

#1 Step 5 - Remove a new item to the list/Table

def remove_from_data(data):
    """
        removes only first value found with identical case sensitive spelling, looks for other entries
        with identical spelling but not case sensitive. alerts if usr_input is not found and also
        if more than one entry is found with the same spelling.

        usr_input: string format input of item to be removed
        :param data: dictionary; key = urgency, list of tasks, urgency can be words or numbers
        :return: new dictionary named data, if the key holds an empty list [], key is removed
                before being returned
    """

    usr_input = input("Enter activity you want to remove: ")
    for key in data.keys():
        value_list_lower = [value.lower() for value in data[key]]
        if usr_input.lower() not in value_list_lower:
            print("Nothing found entered as: {} with priority: {}". format(usr_input, key))
        else:
            if usr_input in data[key]:
                data[key].remove(usr_input)
                value_list_lower = [value.lower() for value in data[key]]
            if usr_input.lower() in value_list_lower:
                indx = value_list_lower.index(usr_input.lower())
                print("Found {} entered as: {} with Priority: {}". format(usr_input, data[key][indx], key))

    for key, value in data.items():
        if data[key] is not []:
            data[key] = value
    return data

# Step 6 - Save tasks to the txt file named ToDo_.txt

def save_to_file(data, file_address, separator):
    """
    'w' for only writing, existing file with the same name will be erased
    if ToDo.txt file doesn't exist, it will be created
    IMPORTANT; path to where the ToDo.txt file is intended to be found must exist
    :param data: dictionary; key = urgency, list of tasks, urgency can be words or numbers
    :param file_address: path to where the ToDo.txt file is intended to be found
    :param separator: separator, delimiter in each line of string "Activity,Priority" saved to ToDo.txt file

    """

    print("Saving data to file.")
    with open(file_address, 'w') as file_object:
        for key, value in data.items():
            for item in data[key]:
                str_write = item + separator + key + '\n'
                file_object.write(str_write)
    print("file object closed? : ", file_object.closed)
    return data

# elif (strChoice == '5'):
#     break #and Exit the program

def exit(data, path, sep):
    """

    :param data: dictionary; key = urgency, list of tasks, urgency can be words or numbers
    :param path: :param file_address: path to where the ToDo.txt file is intended to be found
    :param sep: separator, delimiter in each line of string "Activity,Priority" saved to ToDo.txt file
    :return: False
    """
    # save data to file before Exit?
    save_to_file(data, path, sep)
    return False

# Data
def run_asmt_6(file_path, sep):
    """
    function putting the other function together to operate as desired. needs to be changed if more
        alternatives are added to the menu
    :param file_path: path to the ToDo.txt including the ToDo.txt file name
    :param sep: separator used in ToDo file as well as for def add_data and def save_to_file
    """

    data = read_file(file_path, sep)

    do_dict = menu_options(0)

    temp = True
    while temp:

        choice = menu()  # choice receives a number 1 to 5 in str format
        if choice == '1' or choice == '2' or choice == '3':
            do = do_dict[int(choice)][1](data)
        elif choice == '4':
            do = do_dict[int(choice)][1](data, file_path, sep)
        elif choice == '5':
            temp = do_dict[int(choice)][1](data, file_path, sep)
        else:
            print('Problem at "choice = menu()".')


# file_location and separator are constants and could have been declared global
# with more practice I will hopefully be able to see this as early as while still
# writing the pseudo code.
file_location = "C:\\Users\\Stefan\\Python_Files\\UW_Python\\Mod_1_06\\ToDo.txt"
separator = ','
run_asmt_6(file_location, separator)

print('Finished')

# could have made a user input function, def in_put(user_input, separator = None)
# with overloading, Task, Priority and Task. The separator (",") would have
# been entered with a default value of None and the function
# would have performed differently depending on the presence or not of the ",".
# Example; add - arguments = Task, Priority, remove - argument = Task.