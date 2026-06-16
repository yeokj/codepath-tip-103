class SolutionThree:
    @staticmethod
    def arrange_guest_arrival_order(arrival_pattern): # Session 1, Set 1, Problem 1:
        result = []
        stack = []
        n = len(arrival_pattern)

        for i in range(n + 1):
            stack.append(str(i + 1))

            if i == n or arrival_pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())
        
        return "".join(result) # Space: O(N), Time: O(N)