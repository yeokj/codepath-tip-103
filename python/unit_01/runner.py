from solutions import Solutions

# Problem 1:
# Write a function linear_search() to help Winnie the Pooh locate his lost items. 
# The function accepts a list items and a target value as parameters. The function should 
# return the first index of target in items, and -1 if target is not in items. Do not use any built-in functions.

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(Solutions.linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(Solutions.linear_search(items, target))

# Output:
# 3
# -1
