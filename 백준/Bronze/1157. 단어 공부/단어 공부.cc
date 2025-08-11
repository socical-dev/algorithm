#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int cnt[26] = {0};
    for (char c : s) {
        char u = (c >= 'a' && c <= 'z') ? char(c - 'a' + 'A') : c; // 대문자 통일
        cnt[u - 'A']++;
    }

    int mx = -1, who = -1;
    bool tie = false;
    for (int i = 0; i < 26; ++i) {
        if (cnt[i] > mx) {
            mx = cnt[i];
            who = i;
            tie = false;
        } else if (cnt[i] == mx) {
            tie = true;
        }
    }

    if (tie) cout << "?\n";
    else     cout << char('A' + who) << '\n';
    return 0;
}