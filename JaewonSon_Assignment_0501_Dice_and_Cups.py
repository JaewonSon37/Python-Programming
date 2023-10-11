## Name: Jaewon Son
## Date: October 09 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: https://youtu.be/sdBTHtBc4Kc


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
        return f'Dice and Cup Result: {final_result}'


dice_and_cups_trial = Cup(2, 2, 2)
print(dice_and_cups_trial.roll())
print(dice_and_cups_trial.get_sum())
print(dice_and_cups_trial)