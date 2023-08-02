

# Input: N = 5
# arr = {1, 2, 3, 2, 1}
# Output: 3
# Explaination: Only the number 3 is single.


def Sum_Palindrome(x):
    
    y = x[::-1]
    
    print(y) 
    
    sum = int(y) + int(x)

    return sum

x = input("enter =")
print(Sum_Palindrome(x))



