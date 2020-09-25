#include<iostream>
#include<iomanip>

int main () {
    double A, B, MEDIA;

    std::cin >> A;
    std::cin >> B;

    MEDIA = ((A * 3.5) + (B * 7.5)) / (3.5 + 7.5);

    std::cout << "MEDIA = " << std::fixed << std::setprecision(5) << MEDIA << std::endl;
}