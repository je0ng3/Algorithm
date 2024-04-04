#include <iostream>
#include <math.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  int cnt = 0;
  for (int i = 1; i <= n; i *= 10) {
    cnt += (n - i + 1);
  }
  cout << cnt << '\n';
}
