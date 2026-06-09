from solutions_two import SolutionTwo

# Session 1, Set 1, Problem 1: Counting Treasure
# Captain Blackbeard has a treasure map with several clues that point to different locations on an island. 
# Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary 
# treasure_map where keys are location names and values are integers representing the number of treasures buried 
# at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(SolutionTwo.total_treasures(treasure_map1)) 
print(SolutionTwo.total_treasures(treasure_map2))

# Output:
# 15
# 50

print()

# Session 1, Set 1, Problem 2: Problem 2: Pirate Message Check
# Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message 
# if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, 
# write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, 
# and False otherwise.

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(SolutionTwo.can_trust_message(message1))
print(SolutionTwo.can_trust_message(message2))

# Output:
# True
# False