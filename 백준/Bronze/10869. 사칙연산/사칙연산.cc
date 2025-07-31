#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;  // 두 정수 입력

    cout << A + B << '\n';  // 1. 합
    cout << A - B << '\n';  // 2. 차
    cout << A * B << '\n';  // 3. 곱
    cout << A / B << '\n';  // 4. 몫 (정수 나눗셈)
    cout << A % B << '\n';  // 5. 나머지

    return 0;
}