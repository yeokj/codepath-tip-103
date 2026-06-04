class Solutions:
    @staticmethod
    def linear_search(items, target):
        for i in range(len(items)):
            if items[i] == target:
                return i
        return -1 # Space: O(1), Time: O(N)
    
    @staticmethod
    def final_value_after_operations(operations):
        tigger = 1

        for operation in operations:
            if operation == "bouncy" or operation == "flouncy":
                tigger += 1
            else:
                tigger -= 1
        return tigger # Space: O(1), Time: O(N)