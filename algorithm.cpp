// C++20 Runner (Requires C/C++ Clang Extension enabled)
#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {10, 25, 40, 55};
    int sum = 0;
    for (int n : nums) {
        sum += n;
    }
    std::cout << "C++ Vector Sum: " << sum << std::endl;
    return 0;
}