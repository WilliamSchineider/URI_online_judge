#include<iostream>
#include<iomanip>

int main () {
    double R, A, pi;

    pi = 3.14159;

    std::cout << std::fixed;
    std::cout << std::setprecision(4);
    std::cout << "Qual eh o raio da circunferencia?" << std::endl;
    std::cin >> R;

    A = pi * (R * R);

    std::cout << "A=" << A << std::endl;

    return 0;
}