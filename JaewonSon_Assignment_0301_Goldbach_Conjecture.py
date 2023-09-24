## Name: Jaewon Son
## Date: September 24 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: 


def greet_to_user():

    """Function to greet to user.
    """

    print("\nWelcome to Goldbach Conjecture Test!")
    print("\nYou can check below that the every even integer consist of the two primes.")


def is_prime_number():

    """Find prime numbers and put the numbers is a list.

    Returns:
        list: Return list of the prime numbers.
    """

    prime_list = []

    for num in range(2, 100):
        if num == 2 or num == 3:   # 2 and 3 are prime numbers
            prime_list.append(num)
            continue
        else:
            for divisor in range(2, num):   # Loop to check the num is a prime or not
                if num % divisor == 0:
                    break
            else:
                prime_list.append(num)

    return prime_list


def test_goldbach_conjecture(numbers_in_prime_list):

    """Shows that even numbers are made up of the sum of two primes.
    """

    for test_number in range(4, 101):
        if test_number % 2 == 0:
            prime_number1 = (test_number // 2)   # Start calculating from half of the test_number
            while True:
                prime_number2 = test_number - prime_number1   # Sum of the prime_number1 and prime_number2 is same as test_number 
                if (prime_number1 in numbers_in_prime_list) and (prime_number2 in numbers_in_prime_list):   # Checking prime_number1 and prime_number2 are including in the numbers_in_prime_list
                    print(f"{test_number} = {int(prime_number1)} + {int(prime_number2)}")
                    break
                else:
                    prime_number1 -= 1


def main_function():
    
    """Main function for Goladbach conjecture test.
    """

    greet_to_user()

    numbers_in_prime_list = is_prime_number()

    test_goldbach_conjecture(numbers_in_prime_list)

main_function()