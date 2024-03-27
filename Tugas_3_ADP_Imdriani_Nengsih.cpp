#include <iostream>
using namespace std;

int main() {
    int n;
    cout<<"Jumlah huruf pada piramida = ";
    cin >>n;
    int a = 1;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << "  ";
        }

        char huruf = 'A';

        for (int k = 0; k < i; k++) {
            cout << huruf << " ";
            huruf++;
        }

        huruf--;

        for (int k = 1; k < i; k++) {
            huruf--;
            cout << huruf << " ";
        }

        a += 2;

        cout << endl;
    }

    return 0;
}
