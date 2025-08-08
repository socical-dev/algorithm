#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T; // 테스트 케이스 개수 입력

    for (int i = 1; i <= T; ++i) {
        int A, B;
        cin >> A >> B; // A와 B 입력
        cout << "Case #" << i << ": " << A + B << '\n'; // 출력 포맷
    }

    return 0;
}