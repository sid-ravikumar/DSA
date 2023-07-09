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
    if not array or not all(isinstance(i, int) for i in array):
        raise ValueError("Invalid input. Please provide a non-empty list of integers.")
    if len(array) < 2:
        raise ValueError("Input array must contain at least two elements.")

    seen_numbers = set()  # Store numbers seen so far

    for num in array:
        remainder = targetSum - num  # Calculate remainder needed to reach target sum

        if remainder in seen_numbers:
            return [num, remainder]
        else:
            seen_numbers.add(num)

    return []  # No Pair found. Return empty list.


# Sample Input:
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
# Expected Output: [-1, 11]
print(twoNumberSum(array, targetSum))
