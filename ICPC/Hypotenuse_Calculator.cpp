#include <iostream>
#include <cmath>

int main() {
    using std::cout;
    using std::cin;
    using std::endl;

    double a;
    double b;
    double c;

    cout << "Enter side A: ";
    cin >> a;

    cout << "Enter side B: ";
    cin >> b;

    a = pow(a, 2);
    b = pow(b, 2);
    c = sqrt(a + b);

    cout << "size C: " << c << endl;

    return 0;
}