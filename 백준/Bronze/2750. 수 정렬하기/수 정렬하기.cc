#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N; cin >> N;
    const int OFFSET = 1000;           // 값 범위: [-1000,1000]
    vector<bool> seen(2001, false);
    for (int i = 0; i < N; ++i) {
        int x; cin >> x;
        seen[x + OFFSET] = true;       // 중복 없음 명시
    }
    for (int i = 0; i <= 2000; ++i)
        if (seen[i]) cout << i - OFFSET << '\n';
    return 0;
}
