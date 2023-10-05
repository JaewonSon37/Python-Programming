## Name: Jaewon Son
## Date: October 02 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: https://youtu.be/thok_fyDfCk


def ask_row():

    """Function to ask row input from a user.

    Returns:
        int: Return a integer between 0 and 4.
    """

    while True:

        input_row = input("\nPlease enter a row number between 0 and 4. Or you can type 'exit' to terminate the program: ")

        if input_row == 'exit':
            return 'exit'
        try:
            input_row = eval(input_row)
            assert type(input_row) == int   # Checking whether the input is an integer  
            assert input_row >= 0    # Preventing the input from going out of the range of 0 to 4  
            assert input_row <= 4
            return int(input_row)
        except:
            print("\nInvalid input. Please enter between 0 and 4. Or you can type 'exit' to terminate the program.")


def ask_column(row):

    """Function to ask column input from a user.

    Returns:
        int: Return a integer larger than 0 and the same or less than row.
    """

    while True:

        input_column = input("\nPlease enter a column number. It should be the same or more than 0 and the same or less than the row number: ")

        try:
            input_column = eval(input_column)
            assert type(input_column) == int   # Checking whether the input is an integer  
            assert input_column >= 0    # Preventing the input from going out of the range  
            assert input_column <= row
            return int(input_column)
        except:
            print("\nInvalid input. Please enter the same or more than 0 and the same or less than the row number.")


def human_pyramid(row, column, weight):

    """Function to calculate a total weight on a person's back.

    Returns:
        int: Return a total weight.
    """

    if row == 0:   # Base case
        return 0
    elif column == 0:   # Recursion
        return (human_pyramid(row - 1, column, weight) + weight) / 2
    elif row == column:   # Recursion
        return (human_pyramid(row - 1, column - 1, weight) + weight) / 2
    else:   # Recursion
        return weight + (human_pyramid(row - 1, column - 1, weight) / 2) + human_pyramid(row - 1, column, weight) / 2


def exit_program():

    """Function to terminate the program.
    """

    print("\nThank you for using the program!\n")


def main_function():
        
    """Main function for the Human Pyramid.
    """

    while True:

        input_row = ask_row()

        if input_row != 'exit':
            input_column = ask_column(input_row)
            total_weight = human_pyramid(input_row, input_column, 128)
            print(f"\nTotal weight on a person's back at row {input_row}, column {input_column} is {total_weight} pounds\n")
        else:
            exit_program()
            break

main_function()