## Name: Jaewon Son
## Date: September 25 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: https://youtu.be/_IxK0CEZw4c


def greet_to_user():

    """Function to greet to user.
    """

    print("\nWelcome to Happy Numbers Discriminator!")


def get_input():

    """Function to get input from a user.

    Returns:
        int: Return 0 for exit the program, else positive integer
    """

    while True:

        input_number = input("\nPlease enter any positive number which you want to know whether is the happy number or not. You can also type '0' to exit: ")

        if input_number == '0':
            return 0
        try:
            input_number = eval(input_number)
            assert type(input_number) == int   # Check input is an integer
            assert input_number > 0   # Prevent input of minus value
            return input_number
        except:
            print("\nInvalid input. Please enter a positive number.")


def is_happy_number(test_number):

    """Function to check the integer  is 'happy' or 'sad'.

    Returns:
        turple: Boolean True or False and numbers visited in the verfication process
    """
        
    verification_list = [test_number]   # List for storing all numbers visited in the verification process

    while test_number != 1:   # Exit the while loop if test_number is or become 1

        square_sum = 0

        for digit in str(test_number):   # Seperate test_number to individual digit
            square_sum += int(digit) * int(digit)   # Calculate the digit-square sum

        test_number = square_sum

        if square_sum in verification_list:
            return False, verification_list   # The test_number is 'sad'

        verification_list.append(square_sum)

    return True, verification_list   # The test_number is 'happy'


def single_output(test_number, happy_or_sad, verification_list):

    """Function to print the output of input integer and its returning.
    """

    if happy_or_sad:
        print(f"\n{test_number} is a happy number: {verification_list}")
    else:
        print(f"\n{test_number} is a sad number: {verification_list}")


def exit_program():

    """Function to exit the program if user wants.
    """
    
    print("\nThank you for using Happy Numbers Discriminator.\n")


def main_function():

    """Main function for Happy Number Discriminator.
    """

    greet_to_user()

    result_dict = {}

    while True:

        test_number = get_input()

        if test_number == 0:
            print("\nSumming up the results: \n", result_dict)
            exit_program()
            break

        happy_or_sad, verfication_list = is_happy_number(test_number)

        single_output(test_number, happy_or_sad, verfication_list)

        if happy_or_sad:
            happy_sad = 'happy'
        else:
            happy_sad = 'sad'
        result_dict[test_number] = (happy_sad, verfication_list)
            
main_function()