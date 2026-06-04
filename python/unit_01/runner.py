from solutions import Solutions

# Problem 1, Set 1:
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

print()

# Problem 2, Set 1:
# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

# bouncy or flouncy both increment the value of the variable tigger by 1.
# trouncy or pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations 
# containing a list of operations, return the final value of tigger after performing all the operations.

operations = ["trouncy", "flouncy", "flouncy"]
print(Solutions.final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(Solutions.final_value_after_operations(operations))

# Output:
# 2
# 4

print()

# Problem 3, Set 1:
# T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a 
# new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

word = "Trigger"
print(Solutions.tiggerfy(word))

word = "eggplant"
print(Solutions.tiggerfy(word))

word = "Choir"
print(Solutions.tiggerfy(word))

# Output:
# "r"
# "eplan"
# "chor"