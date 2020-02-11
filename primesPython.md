**Planning**
-Goal is to create a program that checks if an integer is a prime number
-A prime number is only dibisible by itself and 1
-1 is not a prime number

**V1**
-Given n is the input integer
-If function to exclude 1 from being a prime number
``    if n == 1:
        return False  #1 is not a prime 
``

-For loop will check if n is prime by dividing with % operato with numbers in range 2-n. If at anypoint the answer to the divison is 0, it means the number was perfectly divisible by another number that wasnt itself or 0, therefore FALSE is returned, otherwise TRUE is returned to indicate that it is a prime number

``
    for d in range(2, n):
        if n % d == 0:
            return False
        return True

``
-V1 is flawed as it takes a very long time to process large numbers.


**V2**
-To save time in the calculation, the program will only divide and check numbers 2 through the square root of n
-This is done because the divisors between and after the multiplication of the square root of n will come out duplicate, meaning doing divisons after the sqrt n times sqrt n will be redundant.
``
  max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
        return True
``

**v3**
-There is no point testing even integers after 2, so to save more computing time test only odds.
``
  if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
``




CODE

``
import math


def is_prime_v1(n):
    """return TRUE if 'n' is a prime number. False Otherwise. """
    if n == 1:
        return False  # 1 is not a prime

    for d in range(2, n):
        if n % d == 0:
            return False
        return True


def is_prime_v2(n):
    """return TRUE if 'n' is a prime number. False Otherwise. """
    if n == 1:
        return False  # 1 is not a prime
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
        return True


def is_prime_v3(n):
    """return TRUE if 'n' is a prime number. False Otherwise. """
    if n == 1:
        return False  # 1 is not the prime

    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
        return True
``
