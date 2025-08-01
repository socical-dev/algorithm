#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

const int MAX = 100;

// 소수 판별 함수
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i*i <= n; ++i)
        if (n % i == 0) return false;
    return true;
}

int N;
vector<int> nums;
vector<int> adj[MAX];
bool visited[MAX];
int match[MAX];

// DFS로 이분 매칭 시도
bool dfs(int u) {
    for (int v : adj[u]) {
        if (visited[v]) continue;
        visited[v] = true;
        if (match[v] == -1 || dfs(match[v])) {
            match[v] = u;
            return true;
        }
    }
    return false;
}

// u와 짝지어 모든 수가 소수합으로 매칭 가능한지 확인
bool canMatch(int firstIdx, int pairIdx) {
    vector<int> groupA, groupB;

    // 첫 수와 선택된 수는 미리 짝지음
    for (int i = 0; i < N; ++i) {
        if (i == firstIdx || i == pairIdx) continue;
        if (nums[i] % 2 == 0) groupA.push_back(i);
        else groupB.push_back(i);
    }

    // 양쪽 그룹이 다르면 swap
    if (groupA.size() != groupB.size()) return false;
    if (groupA.size() > groupB.size()) swap(groupA, groupB);

    // 연결 그래프 초기화
    for (int i = 0; i < N; ++i) adj[i].clear();

    // 가능한 짝만 edge로 연결
    for (int a : groupA) {
        for (int b : groupB) {
            if (isPrime(nums[a] + nums[b])) {
                adj[a].push_back(b);
            }
        }
    }

    // 매칭 초기화
    memset(match, -1, sizeof(match));
    int matched = 0;
    for (int a : groupA) {
        memset(visited, 0, sizeof(visited));
        if (dfs(a)) matched++;
    }

    // 모든 짝이 매칭됐는지 확인
    return matched == groupA.size();
}

int main() {
    cin >> N;
    nums.resize(N);
    for (int i = 0; i < N; ++i)
        cin >> nums[i];

    vector<int> result;

    // 첫 번째 수와 짝지을 후보 찾기
    for (int i = 1; i < N; ++i) {
        if (isPrime(nums[0] + nums[i])) {
            if (canMatch(0, i)) {
                result.push_back(nums[i]);
            }
        }
    }

    if (result.empty()) {
        cout << -1 << endl;
    } else {
        sort(result.begin(), result.end());
        for (int x : result) cout << x << " ";
        cout << endl;
    }

    return 0;
}
