## Name: Jaewon Son
## Date: October 01 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: https://youtu.be/sHEvagz2yrI


import random


def ask_length():

    """Function to ask length input from a user to create a list.

    Returns:
        int: Return a integer between 0 and 100.
    """
    
    while True:

        input_length = input("\nPlease enter any random integer between 0 and 100. Or you can type 'exit' to terminate the program: ")

        if input_length == 'exit':
            return 'exit'
        try:
            input_length = eval(input_length)
            assert type(input_length) == int   # Checking whether the input is an integer  
            assert input_length >= 0    # Preventing the input from going out of the range of 0 to 100  
            assert input_length <= 100
            return int(input_length)
        except:
            print("\nInvalid input. Please enter between 0 and 100. Or you can type 'exit' to terminate the program.")


def generate_list(input_length):

    """Function to create a random numbers list based on the input.

    Returns:
        list: Return list of a random numbers.
    """
    
    list = random.sample(range(1, 101), input_length)   # Creating a list of random numbers 
    list.sort()   # Sorting the list for binary search
    return list 


def ask_sum():

    """Function to ask a target sum input from a user.

    Returns:
        int: Return a positive integer.
    """

    while True:

        input_sum = input("\nPlease enter any positive integer which is to be a sum: ")

        try:
            input_sum = eval(input_sum)
            assert type(input_sum) == int   # Checking whether the input is an integer    
            assert input_sum >= 1   # Preventing the input from going out of the range of 1 to 199  
            assert input_sum <= 199   
            return int(input_sum)
        except:
            print("\nInvalid input. Please enter a positive integer.")


def binary_search(sum, list):

    """Binary serach to find a value in a list.

    Returns:
        bool: Returns true when find a proper value, else returns false.
    """

    value1 = 0
    value2 = len(list) - 1

    while value1 <= value2:
        
        mid = int((value1 + value2) / 2)   # Index of middle        
        mid_value = list[mid]

        if sum == mid_value:
            return mid
        elif sum < mid_value:   # Sum in lower half
            value2 = mid - 1
        else:
            value1 = mid + 1   # Sum in upper half
    return False


def find_two_pair(binary_search, sum, list):

    """Function to generate an output.
    """

    for number1 in list:
        number2 = sum - number1
        if binary_search(number2, list) and number1 != number2:   # Checking two numbers are in the generated list
            return(f"\n{number1} and {number2} in the list are summed to {sum}.\n")
    return(f"\nNone of the two numbers in the list sum to {sum}.\n")


def exit_program():

    """Function to terminate the program.
    """

    print("\nThank you for using the program!\n")


def main_function():

    """Main function for the Goldbach deuce.
    """

    while True:

        input_length = ask_length()

        if input_length != 'exit':
            list = generate_list(input_length)
            input_sum = ask_sum()
            print(f"\nThis is the list generated through a random integer: {list}")
            print(find_two_pair(binary_search, input_sum, list))
        else:
            exit_program()
            break

main_function()