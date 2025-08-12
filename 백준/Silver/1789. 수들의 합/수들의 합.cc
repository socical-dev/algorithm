#include <bits/stdc++.h>     
// C++에서 자주 쓰이는 표준 라이브러리들을 한 번에 포함하는 헤더
// <iostream>, <vector>, <algorithm>, <cmath> 등 거의 모든 표준 헤더가 포함됨
// 단, 실제 서비스 코드에서는 필요한 헤더만 포함하는 것이 권장됨 (컴파일 시간 단축 목적)

using namespace std;        
// std::cout, std::cin 처럼 std::를 매번 붙이지 않도록 해줌
// 표준 네임스페이스(std)를 전역으로 사용하겠다는 선언

int main() {                 
// 프로그램의 시작 지점 (main 함수)
// 반환형 int는 프로그램 종료 시 운영체제에 반환하는 값 (0이면 정상 종료)

    ios::sync_with_stdio(false); 
    // C++의 입출력(cin, cout)과 C의 입출력(scanf, printf)을 동기화(sync)할지 여부
    // 기본값 true: 동기화됨 → 속도 느림
    // false로 설정하면 C++ 스트림이 C 스트림과 분리되어 속도가 빨라짐
    // 단, false로 하면 printf/scanf와 cout/cin을 섞어 쓰면 예상치 못한 출력 순서 문제가 생김

    cin.tie(nullptr); 
    // cin과 cout의 묶음을 풀어줌
    // 기본적으로 cin은 입력 전에 cout을 flush(출력 버퍼 비우기)함 → 안전하지만 느림
    // nullptr로 묶음을 풀면 불필요한 flush가 사라져 속도 향상
    // 온라인 저지(BOJ 등)에서 빠른 입출력을 위해 자주 사용

    long long S; 
    // 'long long'은 C++ 정수형 타입 (64비트 정수)
    // - 범위: 약 -9e18 ~ 9e18 (int는 약 ±21억까지만 표현 가능)
    // 문제에서 S 최대값이 4,294,967,295이므로 int(32비트) 범위를 넘어갈 수 있어 long long 사용

    cin >> S; 
    // 표준 입력으로 S 값을 읽어옴

    long long sum = 0; 
    // 현재까지 더한 값의 합을 저장하는 변수 (64비트 정수)
    long long n = 0;   
    // 서로 다른 자연수의 개수를 세는 변수

    while (sum + (n + 1) <= S) { 
        // sum + (n+1): 다음 자연수를 더했을 때의 합
        // 이 값이 S를 초과하지 않으면 계속 반복
        n++;           // 자연수 개수 1 증가 (다음 수 포함)
        sum += n;      // sum에 n을 더함
    }

    cout << n << '\n';  
    // n 값을 출력 후 줄바꿈
    // '\n'은 endl보다 빠름 (endl은 줄바꿈 + flush 수행)

    return 0;          
    // 프로그램 정상 종료 (0 반환)
}