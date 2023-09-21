## Name: Jaewon Son
## Date: September 20 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: 


import os


def ask_directory_path():

    """Function to ask for a path that contains the 3 text files in a user's directory.

    Returns:
        str: Return path of a directory if the 3 text files exist. Else return empty.
    """
    
    dir_source = input("\nPlease provide a directory path that contains the 3 text files: ")
    
    if (os.path.isfile(os.path.join(dir_source, 'StemAndLeaf1.txt'))):
        if (os.path.isfile(os.path.join(dir_source, 'StemAndLeaf2.txt'))):
            if (os.path.isfile(os.path.join(dir_source, 'StemAndLeaf3.txt'))):
                return dir_source
            else:
                print("\nThe file: StemAndLeaf3.txt does not exist at {dir_source}")
                return ''
        else:
            print("\nThe file: StemAndLeaf2.txt does not exist at {dir_source}")
            return ''
    else:
        print("\nThe file: StemAndLeaf1.txt does not exist at {dir_source}")
        return ''


def greet_to_user():

    """Function to greet to user.
    """

    print("\nWelcome to Jaewon Son's Stem-and-Leaf Program!")  


def get_input():

    """Function to ask a user to choose one of three numbers.

    Returns:
        str: Return "1", "2", or "3" based on typed by a prompt.
    """

    choice = input("\nPlease enter your choice (1, 2, 3, or 0 to exit): ")
    return choice


def read_text_file(filename):

    """Function to read data from a file and return it as a list.

    Returns:
        list: Return a list function based on data from a text file.
    """
        
    try:
        with open(filename, 'r') as file:
                data = [int(line.strip()) for line in file.readlines()]
        return data
    
    except:
        print(f"Error: {filename} not found.")
        return None


def stem_and_leaf_plot(data):

    """Function to create a dictionary and a stem-and-leaf plot.
    """
    
    stem_and_leaf_dict = {}
        
    for number in data:
        stem, leaf = divmod(number, 10)
        if stem not in stem_and_leaf_dict:
            stem_and_leaf_dict[stem] = []
        stem_and_leaf_dict[stem].append(leaf)
        
    for stem, leaves in sorted(stem_and_leaf_dict.items()):
        print(f"{stem} | {' '.join(map(str, sorted(leaves)))}")


def exit_program():

    """Function to exit the program if user wants.
    """
    
    print("\nThank you for using Jaewon Son's Stem & Leaf Program!\n")


def main_function():

    """Main function of stem-and-leaf-plot.
    """

    dir_source = ask_directory_path()
    if (len(dir_source) == 0):
        os._exit(0)

    greet_to_user()

    while True:
        choice = get_input()

        if choice == '0':
            exit_program()
            break

        elif choice in ('1', '2', '3'):
            data = read_text_file(dir_source + f"\StemAndLeaf{choice}.txt")
            stem_and_leaf_plot(data)

        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 0 to exit.")

main_function()
