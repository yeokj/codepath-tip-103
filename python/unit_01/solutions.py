class Solutions:
    @staticmethod
    def linear_search(items: list[str], target: str) -> int:
        for i in range(len(items)):
            if items[i] == target:
                return i
        return -1 # Space: O(1), Time: O(N)
    
    @staticmethod
    def final_value_after_operations(operations: list[str]) -> int:
        tigger = 1

        for operation in operations:
            if operation == "bouncy" or operation == "flouncy":
                tigger += 1
            else:
                tigger -= 1
        return tigger # Space: O(1), Time: O(N)
    
    @staticmethod
    def tiggerfy(word: str) -> str:
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