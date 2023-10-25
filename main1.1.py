# 1.1 Implement a recursive function to calculate the factorial of a given number

"""
1! = 1 × 1
2! = 2 × 1! --->2 × 1
3! = 3 × 2! ... 
.
.
10! = 10 × 9! ---> 10 × 9 × 8 ×... × 1

Formula - n × (n-1)!
"""

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

number = int(input("enter the value :"))
res = factorial(number)

print("The factorial of {} is {}.".format(number, res))
