




# Input: 
# N = 192
# Output: Fascinating
# Explanation: After multiplication with 2
# and 3, and concatenating with original
# number, number will become 192384576 
# which contains all digits from 1 to 9.



def is_fascinating_number(num):
    if num <= 0:
        return False

    digits_set = {digit for digit in str(num) + str(num * 2) + str(num * 3)}

    return len(digits_set) == 9 and '0' not in digits_set

num = int(input("Enter a number to check if it's fascinating: "))

if is_fascinating_number(num):
    print(f"{num} is a fascinating number!")
else:
    print(f"{num} is not a fascinating number.")

print("Invalid input. Please enter a valid number.")