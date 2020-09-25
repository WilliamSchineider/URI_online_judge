#include<iostream>
#include<iomanip>

int main () {
    double A, B, C, MEDIA; //declaration

    std::cin >> A;
    std::cin >> B;
    std::cin >> C;
    
    MEDIA = ((A * 2) + (B * 3) + (C * 5)) / (2 + 3 + 5); // assignment

    std::cout << "MEDIA = " << std::fixed << std::setprecision(1) << MEDIA << std::endl;
}