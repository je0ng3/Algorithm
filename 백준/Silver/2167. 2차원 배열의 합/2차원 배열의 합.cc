#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n, m; cin>>n>>m;
  vector<vector<int>> v;
  for(int i=0; i<n; i++){
    vector<int> v2;
    for(int j=0; j<m; j++){
        int x; cin>>x; v2.push_back(x);
        if(j==0) continue;
        v2[j] += v2[j-1];
    }
    v.push_back(v2);
  }
  
  int k; cin >> k;
  int x1, y1, x2, y2;
  while (k--) {
    cin >> x1 >> y1 >> x2 >> y2;
    int sum=0;
    if(y1==1){
        for(int i=x1; i<=x2; i++){
            sum+=(v[i-1][y2-1]);
        }
    }
    else{
        for(int i=x1; i<=x2; i++){
            sum+=(v[i-1][y2-1]-v[i-1][y1-2]);
        }
    }
    cout<<sum<<'\n';
  }
  
  
}