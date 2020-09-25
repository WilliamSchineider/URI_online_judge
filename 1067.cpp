#include <iostream>

using namespace std;

int main () {
    int X; // delcaration

    cin >> X;

    for (int i = 0; i <= X; i++) {
        if (i % 2 != 0) {
            cout << i << endl;
        }
    }
}