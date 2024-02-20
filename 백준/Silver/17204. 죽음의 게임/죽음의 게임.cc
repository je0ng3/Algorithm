#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

vector<vector<int>> v;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int n, k; cin >> n >> k;
  vector<int> v, v2;
  for(int i=0; i<n; i++){
    int x; cin >> x;
    v.push_back(x);
  }
  int a=0, b=-1;
  for(int i=0; i<n; i++){
    v2.push_back(v[a]);
    a=v[a];
    if(a==k){
        b=i+1;
        break;
    }
  }
  cout << b <<'\n';
  
}