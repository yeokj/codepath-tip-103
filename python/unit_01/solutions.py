class Solutions:
    @staticmethod
    def linear_search(items, target):
        for i in range(len(items)):
            if items[i] == target:
                return i
        return -1 # Space: O(1), Time O(N)