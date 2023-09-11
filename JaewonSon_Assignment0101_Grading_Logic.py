## Name: Jaewon Son
## Date: September 10 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link:


def compute_grade():
    
    """Function for compute total score of a assignment.

    Returns:
        int: Returns integer based on number typed by a prompt.
    """

    question1 = input('Did you submit the assignment as a single uncompressed .py file? [Yes or No]: ')

    if question1 == 'No':
        return('Your assignment grade is 0')

    question2 = input('Did you include your name and date in the assignment? [Yes or No]: ')

    if question2 == 'No':
        return print('Your assignment grade is 0')

    question3 = input('Did you include the honor statement in the assignment? [Yes or No]: ')

    if question3 == 'No':
        return('Your assignment grade is 0')

    question4 = input('Did you include a link to an YouTube video in the assignment? [Yes or No]: ')

    if question4 == 'No':
        return('Your assignment grade is 0')

    question5 = input('Evaluate the correctness of the code.\nEnter the point between 0 to 10: ')

    question6 = input('Evaluate the elegance of the code.\nEnter the point between 0 to 10: ')

    question7 = input('Evaluate the code hygiene.\nEnter the point between 0 to 10: ')

    question8 = input('Evaluate the quality of the discussion on the video.\nEnter the point between 0 to 10: ')

    question9 = input('Did you submit the assignment before the deadline? [Yes or No]: ')

    if question9 == 'No':
        question10 = input('How many hours late did you submit it?: ')
        return eval(question5) + eval(question6) + eval(question7) + eval(question8) - 0.4 * eval(question10)
    
    else:
        return eval(question5) + eval(question6) + eval(question7) + eval(question8)


total_score = compute_grade()
print(total_score)
