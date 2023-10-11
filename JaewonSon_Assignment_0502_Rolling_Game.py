## Name: Jaewon Son
## Date: October 10 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: https://youtu.be/opiRLSolpdI


import random


class Six_Sided_Dice:

    def __init__(self):

        """Initialize a 6-sided dice object.
        """

        self.sides = 6   # A number of sides of a dice
        self.face_value = 0

    def roll(self):

        """Simulate rolling a dice and set a random face value.
        """

        self.face_value = random.randint(1, self.sides)   # Random number generator from 1 to 6

    def get_face_value(self):

        """Get the current face value shown on a dice.

        Returns:
            int: Returns one of random number from 1 to the number of sides.
        """

        return self.face_value
    
    def __repr__(self):

        """Prints the result.

        Returns:
            int: Returns the number of sides and a number shown on the face of a dice.
        """

        return f'{self.sides}-sided Dice ({self.face_value})'


class Ten_Sided_Dice(Six_Sided_Dice):

    def __init__(self):

        """Initialize a 10-sided dice object.
        """
        super().__init__()
        self.sides = 10   # A number of sides of a dice


class Twenty_Sided_Dice(Six_Sided_Dice):

    def __init__(self):

        """Initialize a 20-sided dice object.
        """

        super().__init__()
        self.sides = 20   # A number of sides of a dice


class Cup:

    def __init__(self, number_of_six_sided_dice = 1, number_of_ten_sided_dice = 1, number_of_twenty_sided_dice = 1):

        """Initialize a Cup object with specified quantities of dice.
        """

        self.trial_list = []   # A list for storing generated numbers
        for _ in range(number_of_six_sided_dice):   # Generate numbers that will show when rolling six-sided dice
            self.trial_list.append(Six_Sided_Dice())
        for _ in range(number_of_ten_sided_dice):   # Generate numbers that will show when rolling ten-sided dice
            self.trial_list.append(Ten_Sided_Dice())
        for _ in range(number_of_twenty_sided_dice):   # Generate numbers that will show when rolling twenty-sided dice
            self.trial_list.append(Twenty_Sided_Dice())

    def roll(self):

        """Simulate rolling all the dice in the cup and return the total_sum.

        Returns:
            int: Returns the total_sum which is the value of a sum of all numbers shown on the face of the dice.
        """

        for dice in self.trial_list:
            dice.roll()
        total_sum = sum(dice.get_face_value() for dice in self.trial_list)
        return total_sum

    def get_sum(self):

        """Calculate and return the total_sum of the face values of all dice in the cup.

        Returns:
            int: Returns the total_sum which is the value of a sum of all numbers shown on the face of the dice.
        """

        total_sum = sum(dice.get_face_value() for dice in self.trial_list)
        return total_sum

    def __repr__(self):

        """Prints the result.

        Returns:
            str: Returns the number shown on the face of each dice.
        """

        final_result = ', '.join([repr(dice) for dice in self.trial_list])
        return final_result


def greet_user():

    """Greet to a user.
    """

    print("\nWelcome to the Rolling Game!")


def ask_name():

    """Ask a username.

    Returns:
        str: Returns a username that will be used for the Rolling Game.
    """
    
    user_name = input("\nPlease enter you name: ")
    return user_name


def whether_play_first():

    """Asking a user whether to play the Rolling Game or not.

    Returns:
        int: Returns 1 when a user is going to play, else returns 0.
    """

    while True:

        whether_play = input("\nWould you like to participate in the Rolling Game? ['1': Yes / '0': No]: ")

        if whether_play == '0':   # 0 means a user is not going to play the game
            return 0
        try:
            whether_play = eval(whether_play)
            assert type(whether_play) == int   # Checking an input is whether valid or not
            assert int(whether_play) == 1
            return whether_play
        except:
            print("\nInvalid input. Choose '1' or '0'.")


def whether_play_again():

    """Asking a user whether to play the Rolling Game again or not.

    Returns:
        int: Returns 1 when a user is going to play again, else returns 0.
    """

    while True:

        whether_play = input("\nWould you like to play the Rolling Game again? ['1': Yes / '0': No]: ")

        if whether_play == '0':   # 0 means a user is not going to play the game
            return 0
        try:
            whether_play = eval(whether_play)
            assert type(whether_play) == int   # Checking an input is whether valid or not
            assert int(whether_play) == 1
            return whether_play
        except:
            print("\nInvalid input. Choose '1' or '0'.")


def goal():

    """Generate a random number between 1 to 100 which will be used for the Rolling Game.

    Returns:
        int: Returns any random number between 1 to 100.
    """

    goal = random.randint(1, 101)   # Random number generator from 1 to 100
    return goal


def number_of_six_sided_dice():

    """Asking a user how many dice would like to roll.

    Returns:
        int: Returns a number entered by a user.
    """

    while True:

        first_dice = input("\nHow many six-sided dice would you like to roll?: ")

        try:
            first_dice = eval(first_dice)
            assert type(first_dice) == int   # Checking an input is whether valid or not
            assert first_dice >= 0
            return first_dice
        except:
            print("\nInvalid input. Please enter again.")


def number_of_ten_sided_dice():

    """Asking a user how many dice would like to roll.

    Returns:
        int: Returns a number entered by a user.
    """

    while True:

        second_dice = input("\nHow many ten-sided dice would you like to roll?: ")

        try:
            second_dice = eval(second_dice)
            assert type(second_dice) == int   # Checking an input is whether valid or not
            assert second_dice >= 0
            return second_dice
        except:
            print("\nInvalid input. Please enter again.")


def number_of_twenty_sided_dice():

    """Asking a user how many dice would like to roll.

    Returns:
        int: Returns a number entered by a user.
    """

    while True:

        third_dice = input("\nHow many twenty-sided dice would you like to roll?: ")

        try:
            third_dice = eval(third_dice)
            assert type(third_dice) == int   # Checking an input is whether valid or not
            assert third_dice >= 0
            return third_dice
        except:
            print("\nInvalid input. Please enter again.")  


def rolling_game():

    """Main function for the Rolling Game.
    """

    greet_user()

    user_name = ask_name()

    play_or_not = whether_play_first()

    rolling_game_score = 0   # Starting game score

    while True:

        if play_or_not == 0:   # Exit the program
            break

        else:
            target_point = goal()   # Target value

            print(f"\n{user_name}, your goal is to get as close as possible to the {target_point}. Good luck!")

            six_sided_dice = number_of_six_sided_dice()   # The number of 6-sided dice a user wants to roll
            ten_sided_dice = number_of_ten_sided_dice()   # The number of 10-sided dice a user wants to roll
            twenty_sided_dice = number_of_twenty_sided_dice()   # The number of 20-sided dice a user wants to roll

            rolling_game = Cup(six_sided_dice, ten_sided_dice, twenty_sided_dice)   # Creates a cup filled with dice according to a user's input
            rolling_game.roll()   # Roll the cup
            point = rolling_game.get_sum()
            print(f"\nThe result of Dice and Cup is {point}: ", rolling_game)   # Report the result to a user

            if target_point == point:   # A condition for updating the rolling_game_score 
                rolling_game_score += 10   # Update rolling_game_score
                print("\nPerferct! You got 10 points.")

            elif 0 <= target_point - point <= 3:   # A condition for updating the rolling_game_score 
                rolling_game_score += 5   # Update rolling_game_score
                print("\nNice! You got 5 points.")

            elif 0 <= target_point - point <= 10:   # A condition for updating the rolling_game_score 
                rolling_game_score += 2   # Update rolling_game_score
                print("\nNot bad! You got 2 points.")

            else:   # When the value difference is more than 10 or the point is larger than target_point
                rolling_game_score += 0
                print("\nOops! You got 0 point.")

            print(f"\n{user_name}, your current score is {rolling_game_score}!")   # Report the result to a user

            if whether_play_again() == 0:   # Exit the program
                break

    print(f"\nThank you for playing the Rolling Game, {user_name}! Your final score is {rolling_game_score}.\n")   # Report the result to a user    
            

if __name__ == "__main__":
    rolling_game()