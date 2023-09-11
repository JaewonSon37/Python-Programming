## Name: Jaewon Son
## Date: September 10 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link:


def coprime(coprime_test_number1, coprime_test_number2): 
  
  """Function for checking whether two numbers are coprime or not.

  Args:
      coprime_test_number1 (int): Natural number typed by a prompt in the first order.
      coprime_test_number2 (int): Natural number typed by a prompt in the second order.

  Returns:
      bool: Returns true when the numbers are coprime and returns false when the numbers are not coprime.
  """

  if coprime_test_number1 == 1 or coprime_test_number2 == 1:
    return True
  
  else:
    count = 0
    if coprime_test_number1 < coprime_test_number2:
      for i in range(2, coprime_test_number1 + 1):
        if coprime_test_number1 % i == 0:
          if coprime_test_number2 % i == 0:
            count += 1
    else:
      for i in range(2, coprime_test_number2 + 1):
        if coprime_test_number2 % i == 0:
          if coprime_test_number1 % i == 0:
            count += 1

    return count < 1


while True:

  coprime_test_number1 = input('Enter the First Number or Exit: ')
  
  if coprime_test_number1 == 'Exit':
    print('Thank you for using Coprime test!')
    break
  
  coprime_test_number2 = input('Enter the Second Number: ')
  
  if coprime(eval(coprime_test_number1), eval(coprime_test_number2)):
    print('Those two numbers are coprime.')
  
  else:
    print('Those two numbers are not coprime.')
