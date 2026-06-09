class SolutionTwo:
    @staticmethod
    def total_treasures(treasure_map):
        total = 0

        for v in treasure_map.values():
            total += v
        return total
    
    @staticmethod
    def can_trust_message(message):
        mp = {'a': 0, 'b': 0, }