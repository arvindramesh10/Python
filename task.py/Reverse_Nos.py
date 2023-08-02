

# Input: 200                                                                       
# Output: 2
# Explanation: By reversing the digts of 
# number, number will change into 2.


# Input : 122
# Output: 221
# Explanation: By reversing the digits of 
# number, number will change into 221.


def reverse_digits(num):
    
    number = str(num)
    
    reversed_str = number[::-1]
    
    reverse_num = int(reversed_str)
    
    return reverse_num


num= int(input("Enter a number :"))

reverse_num = reverse_digits(num)

print(reverse_num)
