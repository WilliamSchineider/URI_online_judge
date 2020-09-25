// https://www.urionlinejudge.com.br/judge/pt/problems/view/1065

#include <iostream>

using namespace std;

int main () {
    int a, b, c, d, e; // declaration
    int numArray[5];
    int even_num = 0; // inicitalization

// Creates an array with size of 5 elements

    for (int i = 0; i <= 4; i++) { // passing a fixed amout of numbers into an array
        cin >> numArray[i];
    };

    int len = sizeof(numArray)/sizeof(numArray[5]); // defining the size of an array

// Now displays which elements of this array are even

    int numbers = 0;

    for (int n = 0; n <= len; n++) {
        if (numArray[n] % 2 == 0) {
            numbers = numbers + 1;
        };
    };
    cout << numbers << " valores pares" << endl;
}
