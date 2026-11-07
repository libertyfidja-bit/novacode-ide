#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {3, 9, 15, 21, 42};
    int sum = 0;
    for (int n : nums) sum += n;
    std::cout << "[C++ Runner] Array sum = " << sum << std::endl;
    return 0;
}