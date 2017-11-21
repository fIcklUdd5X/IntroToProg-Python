# python 3


# 1) Create and test a new Python file using the following code:
# 2) Create one or more classes to store and process Product data using the code.


class UserInput(object):

    @staticmethod
    def user_input(file):
        obj_file = False
        try:
            obj_file = open(file, "r+")

            # would like to write this in a class Processing - not sure how to do do:
            # try - except while file stays open
            try:
                print("Type in a Product Id, Name, and Price you want to add to the file")
                print("(Enter 'Exit' to quit!)")
                while True:
                    str_usr_input = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
                    if str_usr_input.lower() == "exit":
                        return False
                    else:
                        print("\nYou Entered: {}".format(str_usr_input))
                        obj_file.seek(0, 2)  # go to end of file --> always add str_usr_input at end of file
                        obj_file.write(str_usr_input + "\n")
            finally:
                return False

        except FileNotFoundError as e:
            print("Error: " + str(e) + "\n Please check the file name")
        except Exception as e:
            print("Error: " + str(e))
        finally:
            if obj_file is not None:
                obj_file.close()


class ReadFile(object):
    # would like to write class OpenFile that the read ReadFile and WriteFile can call.

    @staticmethod
    def read_file(file, message):
        obj_file = False
        try:
            obj_file = open(file, "r+")

            # would like to write this in a class ReadFile - not sure how to do do:
            # try - except while file stays open
            try:
                print(message)
                obj_file.seek(0)
                print(obj_file.read())
            except Exception as e:
                print("Error: " + str(e))

        except FileNotFoundError as e:
            print("Error: " + str(e) + "\n Please check the file name")
        except Exception as e:
            print("Error: " + str(e))
        finally:
            if obj_file is not None:
                obj_file.close()


class RunFileIO(object):

    @staticmethod
    def run_file_io(file):
        read = ReadFile()
        read.read_file(file, "Here is the current data:")
        write = UserInput()
        if not write.user_input(file):
            read.read_file(file, "Here is the saved data:")


File = "Products.txt"
r = RunFileIO()
r.run_file_io(File)
