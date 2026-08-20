class SolutionsOne:
    @staticmethod
    def linear_search(items: list[str], target: str) -> int: # Session 1, Set 1, Problem 1: Hunny Hunt
        for i in range(len(items)):
            if items[i] == target:
                return i
        return -1 # Space: O(1), Time: O(N)
    
    @staticmethod
    def final_value_after_operations(operations: list[str]) -> int: # Session 1, Set 1 Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
        tigger = 1

        for operation in operations:
            if operation == "bouncy" or operation == "flouncy":
                tigger += 1
            else:
                tigger -= 1
        return tigger # Space: O(1), Time: O(N)
    
    @staticmethod
    def tiggerfy(word: str) -> str: # Session 1, Set 1, Problem 3: T-I-Double Guh-Er II
        result = ""
        words = word.lower()
        i = 0

        while i < len(words):
            if i < len(words) - 1 and words[i] == 'g' and words[i + 1] == 'g':
                i += 2
                continue
            elif i < len(words) - 1 and words[i] == 'e' and words[i + 1] == 'r':
                i += 2
                continue
            elif words[i] in {'t', 'i'}:
                i += 1
                continue
            else:
                result += words[i]
                i += 1
        return result # Space: O(N), Time: O(N)
    
    @staticmethod
    def non_decreasing(nums: list[int]) -> bool: # Session 1, Set 1, Problem 4: Non-decreasing Array
        violation = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if violation == True:
                    return False
                violation = True
                if i == 1 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return True # Space: O(1), Time: O(N)
    
    @staticmethod
    def find_missing_clues(clues, lower, upper) -> list[list[int]]: # Session 1, Set 1, Problem 5: Missing Clues
        result = []
        start = lower

        for clue in clues:
            if clue > start:
                result.append([start, clue - 1])
            start = clue + 1

        if start <= upper:
            result.append([start, upper])

        return result # Space: O(1), Time: O(N)
    
    @staticmethod
    def transpose(matrix): # Problem 1, Session 2, Set 1: Transpose Matrix
        rows, cols = len(matrix), len(matrix[0])
        result = [[0 for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        return result # Space: O(M * N), Time: O(M * N)