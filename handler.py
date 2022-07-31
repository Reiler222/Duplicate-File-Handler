import sys
import os

path = None
format = None
sorting_option = None
inventory_dict = {}

def output(dict_to_output):
    pass
    #for key, value in dict_to_output:
    #    pass


def sorting():
    if sorting_option == '1':
        sorted_dict = {k: v for k, v in sorted(inventory_dict.items(), key=lambda item: item[0], reverse=True)}
    else:
        sorted_dict = {k: v for k, v in sorted(inventory_dict.items(), key=lambda item: item[0])}
    print()
    output(sorted_dict)
    print(sorted_dict)


# TODO: Añadir un filtro para que, si ya existe un "size", añada la ruta del archivo a la lista valor de ese "size"
def find_files():
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(format):
                complete_name = os.path.join(root, name)
                size = os.path.getsize(complete_name)
                if size in inventory_dict.keys():
                    inventory_dict[size].append(complete_name)
                else:
                    inventory_dict[size] = complete_name
    sorting()

try:
    path = sys.argv[1]
except IndexError:
    print("Directory is not specified")
    exit()

format = input("Enter file format:\n")

while True:
    sorting_option = input("Size sorting options:\n1. Descending \n2. Ascending\n")
    if sorting_option not in ["1", "2"]:
        print("Wrong option")
    else:
        break

find_files()
try:
    root = args[1]
    extension = input('Enter file format:\n')
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            filename, file_extension = os.path.splitext(name)
            if file_extension == extension or extension == '':
                file_path = os.path.join(root, name)
                size = os.path.getsize(file_path)
                if size in size_paths_dic.keys():
                    size_paths_dic[size].append(file_path)
                else:
                    paths_list = [file_path]
                    size_paths_dic[size] = paths_list
                #print(os.path.join(root, name))
    sorting_opt()
except IndexError:
    print('Directory is not specified')