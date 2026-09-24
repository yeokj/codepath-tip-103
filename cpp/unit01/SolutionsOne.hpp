#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class SolutionsOne {
public:
    // Session 1, Set 1, Problem 1: Hunny Hunt
    static int linearSearch(const std::vector<std::string>& items, const std::string& target) {
        int n = items.size();

        for (int i = 0; i < n; ++i) {
            if (items[i] == target) return i;
        }
        return -1; // Space: O(1), Time: O(N)
    }

    // Session 1, Set 1, Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
    static int finalValueAfterOperations(const std::vector<std::string>& operations) {
        int result = 1, n = operations.size();

        for (const std::string &op : operations) {
            if (op == "bouncy" || op == "flouncy") ++result;
            else --result;
        }
        return result; // Space: O(1), Time: O(N)
    }

    // Session 1, Set 1, Problem 3: T-I-Double Guh-Er II
    static std::string tiggerfy(const std::string& word) {
        std::string result = "";
        int n = word.length(), i = 0;

        while (i < n) {
            if (i < n - 1 && (tolower(word[i]) == 'g' && tolower(word[i + 1]) == 'g')) {
                i += 2;
                continue;
            }
            else if (i < n - 1 && (tolower(word[i]) == 'e' && tolower(word[i + 1] == 'r'))) {
                i += 2;
                continue;
            }
            else if (tolower(word[i]) == 't' || tolower(word[i]) == 'i') {
                ++i;
                continue;
            }
            else {
                result.push_back(tolower(word[i]));
                ++i;
            }
        }
        return result; // Space: O(1), Time: O(N)
    }

    // Session 1, Set 1, Problem 4: Non-decreasing Array
    static bool nonDecreasing(std::vector<int>& nums) {
        bool violation = false;
        int n = nums.size();

        for (int i = 1; i < n; ++i) {
            if (nums[i] < nums[i - 1]) {
                if (violation) return false;
                violation = true;

                if ( i == 1 || nums[i - 2] <= nums[i]) nums[ i - 1] = nums[i];
                else nums[i] = nums[i - 1];
            }
        }
        return true; // Space: O(1), Time: O(N)
    }

    // Session 1, Set 1, Problem 5: Missing Clues
    static std::vector<std::vector<int>> findMissingClues(const std::vector<int>& clues, int lower, int upper) {
        // TODO: Implement logic
        return {};
    }

    // Session 1, Set 1, Problem 6: Vegetable Harvest
    static int harvest(const std::vector<std::vector<char>>& vegetablePatch) {
        // TODO: Implement logic
        return 0;
    }

    // Session 1, Set 1, Problem 7: Eeyore's House
    static int goodPairs(const std::vector<int>& pile1, const std::vector<int>& pile2, int k) {
        // TODO: Implement logic
        return 0;
    }

    // Session 1, Set 1, Problem 8: Local Maximums
    static std::vector<std::vector<int>> localMaximums(const std::vector<std::vector<int>>& grid) {
        // TODO: Implement logic
        return {};
    }
};