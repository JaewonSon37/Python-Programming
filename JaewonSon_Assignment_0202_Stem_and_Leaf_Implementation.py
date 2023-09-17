## Name: Jaewon Son
## Date: September 18 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: 


# Function to greet to user
def greet_to_user():
    print("Welcome to Jaewon Son's Stem-and-Leaf Program!")  


# Function to ask a user to choose a 1, 2, or 3 as an input
def get_input():
    choice = input("\nPlease enter your choice (1, 2, 3, or 0 to exit): ")
    return choice


# Function to read data from a file and return it as a list
def read_text_file(filename):
        
    try:
        with open(filename, 'r') as file:
                data = [int(line.strip()) for line in file.readlines()]
        return data
    
    except:
        print(f"Error: File{filename} not found.")
        return None


# Function to create a dictrionary and a stem-and-leaf plot
def stem_and_leaf_plot(data):
    
    stem_and_leaf_dict = {}
        
    for number in data:
        stem, leaf = divmod(number, 10)
        if stem not in stem_and_leaf_dict:
            stem_and_leaf_dict[stem] = []
        stem_and_leaf_dict[stem].append(leaf)
        
    for stem, leaves in sorted(stem_and_leaf_dict.items()):
        print(f"{stem} | {' '.join(map(str, sorted(leaves)))}")


# Function to exit the program
def exit_program():
    print("Thank you for using Jaewon Son's Stem & Leaf Program!")


# Main Function
if __name__ == "__main__":

    greet_to_user()

    while True:
        choice = get_input()

        if choice == '0':
            exit_program()
            break

        elif choice in ('1', '2', '3'):
            data = read_text_file(f"C:/Users/LG/Desktop/DEPAUL UNIV/2023 Fall/Python Programming/DSC 430 - Week 2/StemAndLeaf{choice}.txt")
            stem_and_leaf_plot(data)

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 0 to exit.")