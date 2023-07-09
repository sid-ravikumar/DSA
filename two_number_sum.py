# Write a function that takes in a non-empty array of distinct integers and an 
# integer representing a target sum. If any two numbers in the input array sum 
# up to the target sum, the function should return them in an array, in any 
# order. If no two numbers sum up to the target sum, the function should return 
# an empty array.
# 
# Note that the target sum has to be obtained by summing two different integers
# in the array; you can't add a single integer to itself in order to obtain the 
# target sum.
# 
# You can assume that there will be at most one pair of numbers summing up to 
# the target sum.

def twoNumberSum(array, targetSum):
    remainders = {}
    for num in array:
        remainder = targetSum - num
        if remainder in remainders:
            return [num, remainder]
        else:
            remainders[num] = remainder
    return []

# Sample Input:
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
# Expected Output: [-1, 11]
print(twoNumberSum(array, targetSum))