INPUT PRINT AND NUMBERS
  Sum of Three Numbers 
  `` 
  # This program reads two numbers and prints their sum:
  a = int(input())
  b = int(input())
  c = int(input())
  print(a + b + c)

  # Can you change it so it can add three numbers?

  ``
    
    Square
    ``
    # Read an integer:
  a = int(input())
  # Read a float:
  b = int(a * a)
  # Print a value:
  print(b)
  
    ``
    
    Apple Sharing
    ``
   # Read the numbers like this:
   N = int(input())
   K = int(input())
   # Print the result with print()

   # Example of division, integer division and remainder:
   print(K // N)
   print(K % N)
    ``
    
    Previous and Next
    ``
    # Read an integer:
  a = int(input())
  b = int(a+1)
  c = int(a-1)
  # Print a value:
  print("The next number for the number", str(a) ,"is", str(b),)
  print("The previous number for the number", str(a) ,"is", str(c),)

    ``
    
    Two Timestamps
    ``
    # Read an integer:
    hour1 = int(input())
    minute1 = int(input())
    second1 = int(input())
    hour2 = int(input())
    minute2 = int(input())
    second2 = int(input())
    total1 = int(hour1 * 3600 + minute1 * 60 + second1)
    total2 = int(hour2 * 3600 + minute2 * 60+ second2)
    print(total2 - total1)

    ``
    
INTEGER AND FLOAT NUMBERS
  Last Digit of Int
  ``
  # Read an integer:
num = int(input())
num = (num % 10)


print(num)


  ``
  
  Tens Digit
  ``
  number = int(input())
d = int()
counter = number
while counter > 0:
    counter = ( counter // 10 )
    d = d+1



if d == 2:
    d = 0
if d == 3:
    d = 1
while d > 2:
    d = d-1
if number > 9:
    number = str(number)
    print (number[d])
else:    
    print (0)
  ``
  
  Car Route
  ``
  N = int(input())
M = int(input())


if (M % N == 0):
    print(M/N)
else:
    print(M//N+1)
    ``
