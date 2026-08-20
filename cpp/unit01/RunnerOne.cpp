#include <iostream>
#include <vector>
#include <string>
#include "SolutionsOne.hpp"

// Helper function to print a 2D integer vector matching Python list formatting
void print2DVector(const std::vector<std::vector<int>>& matrix) {
    std::cout << "[";
    for (size_t i = 0; i < matrix.size(); ++i) {
        std::cout << "[";
        for (size_t j = 0; j < matrix[i].size(); ++j) {
            std::cout << matrix[i][j];
            if (j + 1 < matrix[i].size()) std::cout << ", ";
        }
        std::cout << "]";
        if (i + 1 < matrix.size()) std::cout << ", ";
    }
    std::cout << "]\n";
}

int main() {
    // Session 1, Set 1, Problem 1: Hunny Hunt
    {
        std::vector<std::string> items1 = {"haycorn", "haycorn", "haycorn", "hunny", "haycorn"};
        std::string target1 = "hunny";
        std::cout << SolutionsOne::linearSearch(items1, target1) << std::endl;

        std::vector<std::string> items2 = {"bed", "blue jacket", "red shirt", "hunny"};
        std::string target2 = "red balloon";
        std::cout << SolutionsOne::linearSearch(items2, target2) << std::endl;
        // Expected Output:
        // 3
        // -1
    }

    std::cout << "\n";

    // Session 1, Set 1, Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
    {
        std::vector<std::string> operations1 = {"trouncy", "flouncy", "flouncy"};
        std::cout << SolutionsOne::finalValueAfterOperations(operations1) << std::endl;

        std::vector<std::string> operations2 = {"bouncy", "bouncy", "flouncy"};
        std::cout << SolutionsOne::finalValueAfterOperations(operations2) << std::endl;
        // Expected Output:
        // 2
        // 4
    }

    std::cout << "\n";

    // Session 1, Set 1, Problem 3: T-I-Double Guh-Er II
    {
        std::string word1 = "Trigger";
        std::cout << "\"" << SolutionsOne::tiggerfy(word1) << "\"" << std::endl;

        std::string word2 = "eggplant";
        std::cout << "\"" << SolutionsOne::tiggerfy(word2) << "\"" << std::endl;

        std::string word3 = "Choir";
        std::cout << "\"" << SolutionsOne::tiggerfy(word3) << "\"" << std::endl;
        // Expected Output:
        // "r"
        // "eplan"
        // "chor"
    }

    std::cout << "\n";

    // Session 1, Set 1, Problem 4: Non-decreasing Array
    {
        std::cout << std::boolalpha; // Formats booleans as true/false instead of 1/0
        std::vector<int> nums1 = {4, 2, 3};
        std::cout << SolutionsOne::nonDecreasing(nums1) << std::endl;

        std::vector<int> nums2 = {4, 2, 1};
        std::cout << SolutionsOne::nonDecreasing(nums2) << std::endl;
        // Expected Output:
        // true
        // false
    }

    std::cout << "\n";

    // Session 1, Set 1, Problem 5: Missing Clues
    {
        std::vector<int> clues1 = {0, 1, 3, 50, 75};
        int lower1 = 0, upper1 = 99;
        print2DVector(SolutionsOne::findMissingClues(clues1, lower1, upper1));

        std::vector<int> clues2 = {-1};
        int lower2 = -1, upper2 = -1;
        print2DVector(SolutionsOne::findMissingClues(clues2, lower2, upper2));
        // Expected Output:
        // [[2, 2], [4, 49], [51, 74], [76, 99]]
        // []
    }

    std::cout << "\n";

    // Session 1, Set 1, Problem 6: Vegetable Harvest
    {
        std::vector<std::vector<char>> patch = {
            {'x', 'c', 'x'},
            {'x', 'x', 'x'},
            {'x', 'c', 'c'},
            {'c', 'c', 'c'}
        };
        std::cout << SolutionsOne::harvest(patch) << std::endl;
        // Expected Output:
        // 6
    }

    std::cout << "\n";

    // Session 1, Set 1, Problem 7: Eeyore's House
    {
        std::vector<int> pile1_1 = {1, 3, 4};
        std::vector<int> pile2_1 = {1, 3, 4};
        int k1 = 1;
        std::cout << SolutionsOne::goodPairs(pile1_1, pile2_1, k1) << std::endl;

        std::vector<int> pile1_2 = {1, 2, 4, 12};
        std::vector<int> pile2_2 = {2, 4};
        int k2 = 3;
        std::cout << SolutionsOne::goodPairs(pile1_2, pile2_2, k2) << std::endl;
        // Expected Output:
        // 5
        // 2
    }

    std::cout << "\n";

    // Session 1, Set 1, Problem 8: Local Maximums
    {
        std::vector<std::vector<int>> grid1 = {
            {9, 9, 8, 1},
            {5, 6, 2, 6},
            {8, 2, 6, 4},
            {6, 2, 2, 2}
        };
        print2DVector(SolutionsOne::localMaximums(grid1));

        std::vector<std::vector<int>> grid2 = {
            {1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1},
            {1, 1, 2, 1, 1},
            {1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1}
        };
        print2DVector(SolutionsOne::localMaximums(grid2));
        // Expected Output:
        // [[9, 9], [8, 6]]
        // [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    }

    return 0;
}