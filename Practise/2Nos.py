# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# Example:

# Given nums = [3, 2, 4], target = 6,

# Because nums[1] + nums[2] = 2 + 4 = 6

# return [1, 2].

# SOLUTION:



# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# # Test the two_sum function
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))  # Output: [0, 1]


# str = 'Hello World!'
# print(str*2)

# def myWrapper(n):
#  return lambda a : a * n
# mulFive = myWrapper(5)
# print(mulFive(1))  

list_1 = [1, 2, [3, 5], 4]
## shallow copy
list_2 = copy(list_1) 
list_2[3] = 7
print(list_2)
# # list_2[2].append(6)
# # list_2    # output => [1, 2, [3, 5, 6], 7]
# # list_1    # output => [1, 2, [3, 5, 6], 4]
# # ## deep copy
# # list_3 = deepcopy(list_1)
# # list_3[3] = 8
# # list_3[2].append(7)

original_list = [1, 2, [3, 5], 4]
copied_list = original_list[:]
copied_list[3]=7
print(copied_list)

