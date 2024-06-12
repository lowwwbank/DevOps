#include <iostream>

int main() {
    int a, b;
    std::cout << "Введите два числа для сложения:\n";
    std::cin >> a >> b;
    int sum = a + b;
    std::cout << "Сумма: " << sum << std::endl;
    return 0;
}