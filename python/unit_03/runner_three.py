from solutions_three import SolutionThree

# Session 1, Set 1, Problem 1:
# You are organizing a prestigious event, and you must arrange the order in which guests arrive based on a set of instructions.

# The instructions are provided as a 0-indexed string arrival_pattern of length n, consisting of the characters:

# 'I' - The next guest should have a higher number than the previous guest.
# 'D' - The next guest should have a lower number than the previous guest.
# You need to create a string guest_order of length n + 1 that satisfies the following conditions:

# guest_order contains each number from 1 to str(n + 1) exactly once. These numbers represent the guests' assigned numbers.
# For every index i from 0 to n - 1:
# If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
# If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
# Among all valid orders, return the lexicographically smallest one.

print(SolutionThree.arrange_guest_arrival_order("IIIDIDDD"))  
print(SolutionThree.arrange_guest_arrival_order("DDD"))

# Output:
# 123549876
# 4321