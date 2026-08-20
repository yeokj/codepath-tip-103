from solutions_one import SolutionsOne

# Session 1, Set 1, Problem 1: Hunny Hunt
# Write a function linear_search() to help Winnie the Pooh locate his lost items. 
# The function accepts a list items and a target value as parameters. The function should 
# return the first index of target in items, and -1 if target is not in items. Do not use any built-in functions.

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(SolutionsOne.linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(SolutionsOne.linear_search(items, target))

# Output:
# 3
# -1

print()

# Session 1, Set 1 Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

# bouncy or flouncy both increment the value of the variable tigger by 1.
# trouncy or pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations 
# containing a list of operations, return the final value of tigger after performing all the operations.

operations = ["trouncy", "flouncy", "flouncy"]
print(SolutionsOne.final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(SolutionsOne.final_value_after_operations(operations))

# Output:
# 2
# 4

print()

# Session 1, Set 1, Problem 3: T-I-Double Guh-Er II
# T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a 
# new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

word = "Trigger"
print(SolutionsOne.tiggerfy(word))

word = "eggplant"
print(SolutionsOne.tiggerfy(word))

word = "Choir"
print(SolutionsOne.tiggerfy(word))

# Output:
# "r"
# "eplan"
# "chor"

print()

# Session 1, Set 1, Problem 4: Non-decreasing Array
# Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing 
# by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

nums = [4, 2, 3]
print(SolutionsOne.non_decreasing(nums))

nums = [4, 2, 1]
print(SolutionsOne.non_decreasing(nums))

# Output:
# True
# False

print()

# Session 1, Set 1, Problem 5: Missing Clues
# Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. 
# Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. 
# The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within 
# the inclusive range [lower, upper].

# A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

# Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of clues is 
# included in any of the ranges, and each missing number is covered by one of the ranges.

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(SolutionsOne.find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(SolutionsOne.find_missing_clues(clues, lower, upper))

# Output:
# [[2, 2], [4, 49], [51, 74], [76, 99]]
# []

print()

# Session 2, Set 1, Problem 1: Transpose Matrix
# Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. 
# The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(SolutionsOne.transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(SolutionsOne.transpose(matrix))

# Output:
# [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]
# [
#     [1, 4],
#     [2, 5],
#     [3, 6]
# ]