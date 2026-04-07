#include <iostream>

int main()
{
    int a = 0, b = 1; // sets a to 0, and be to 1
    int sum_even = 0; // sets sum_even to 0
    while (b < 4000000) {
        if (b % 2 == 0) { // checks if b is even
            sum_even += b; // if b is even, adds b to sum_even
        }
        int temp = b; // sets temp equal b
        b = a + b; // sets b equal to a plus b
        a = temp; // sets a equal to temp
    }
    std::cout << sum_even << std::endl; // couts what sum_even currently is

    return 0;
}

// answer should be 4613732
