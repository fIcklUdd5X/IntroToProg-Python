# python 3

# Assignment_07_Stefan Lund
#-------------------------------------------------#

#-- Data --#


#-- Input/Output --#


#-- Processing --#

#-------------------------------


# Assignment_07_Stefan Lund
#-------------------------------------------------#


import sys, pickle


class ReadWriteFile(object):

    #file_direct = None
    #data = None
    #file_address = None

    @staticmethod
    def read_from_file(file_direct):
        """

        :param file_direct: file path and file name where the information is to be found
        :type file_direct: binary file
        :return: data as found in the file
        :rtype: type as found in the file
        """

        try:
            with open(file_direct, 'rb') as f:
                data_ = pickle.load(f)

            print("\nReading data from file.\nread file object closed? : ", f.closed)
            return data_

        except FileNotFoundError as e:
            print("e: ", e)
            e = sys.exc_info()[0]
            print("Error: {}".format(e))
            print("Not a problem. File created when saved.")

        except:  # catch all other Errors - not the best solution.
            e = sys.exc_info()[0]
            print("Error: {}".format(e))

    @staticmethod
    def save_to_file(data_, file_address):
        """
        'w' for only writing, existing file with the same name will be erased
        if Customers.dat file doesn't exist, it will be created
        IMPORTANT; path to where the Customers.dat file is intended to be found must exist
                    even if the Customers.dat file does not.
        :param data_: any format
        :param file_address: path to where the Customers.dat file is intended to be found

        """

        print("\nSaving data to file.")
        with open(file_address, 'wb') as file_object:
            pickle.dump(data_, file_object)
        print("write file object closed? : ", file_object.closed)


def main(data_, file_location):
    for d in data_:
        print("{}\ndata to be saved: {}, type: {}".format("-" * 66, d, type(d)))

        in_object = ReadWriteFile()
        in_object.save_to_file(d, file_location)

        out_object = ReadWriteFile()
        da = out_object.read_from_file(file_location)
        print("\ndata retrieved from file: {}, type: {}".format(da, type(da)))
        print("data saved == data retrieved: {}, \ndata saved is data retrieved: {}\n\n".format(d == da, d is da))


path = 'C:\\A_Playground\\Customers.dat'
data_1 = [[1, "Black Pearl"], [2, "Captain Hook"]]
data_2 = {1: "Black Pearl", 2: "Captain Hook"}
data_3 = [1, "Black Pearl"], [2, "Captain Hook"],
data_4 = "1" + "Black Pearl" + "\n" + "2" + "Captain Hook" + "\n"
data = [data_1, data_2, data_3, data_4]

main(data, path)
