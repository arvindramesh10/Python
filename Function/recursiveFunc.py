

# a = 0

# def recursiveFunc():
#     global a
#     a+= 1
#     if a <=10:
#         print(a)
#         recursiveFunc()

# recursiveFunc()

# def fact():

#     global n
#     global factorial
#     for i in range(1,n+1):
#         factorial = factorial*i
#         print(factorial)
#     return factorial

# n = int(input("Enter a value ="))
# factorial = 1
# print(fact)


#TASK
# sum (2)() => 2   
# sum (2)(4)() => 6
# sum (2)(4)(3)() => 9



# def factorial(x):
#     if x==0 or x==1:
#         return 1
#     else:
#         fact = x* (x-1) 
#         return fact

# n=int(input("Enter a number :"))
# factorial(n)
# print(f"Factorial of number {n}! is {fact}")

# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:*20
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value hor a different result
num = 7

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)


# def factorial(n):
#     # Base case: if n is 0 or 1, the factorial is 1
#     if n == 0 or n == 1:
#         return 1
#     else:
#         # Recursive case: call the factorial function with (n-1)
#         return n * factorial(n-1)

.......