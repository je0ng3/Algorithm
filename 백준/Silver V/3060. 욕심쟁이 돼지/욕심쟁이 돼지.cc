#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int t; cin>> t;
  while(t--){
    vector<int> v;
    int n; cin>> n;
    int x, day=1;
    for(int i=0; i<6; i++){
      cin >> x;
      v.push_back(x);
    }
    int sum =  accumulate(v.begin(), v.end(), 0);
    while(true){
      if(sum>n){
        cout << day <<'\n';
        break;
      }else{
        sum*=4;
        day++;
      }
    }
  }
}