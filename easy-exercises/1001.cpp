#include<iostream>

using namespace std;

int main () {
    // declaração de variáveis
    int A, B, X;

    // input de dados do usuário
    std::cin >> A;
    std::cin >> B;

    // cálculo
    X = A + B;

    // apresentação do resultado para usuário
    std::cout << "X = " << X << std::endl;

    return 0;
}