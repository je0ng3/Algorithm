#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

vector<vector<int>> v;

int check(){
    int count=0;
    int d1=0, d2=0;
    for(int i=0; i<5; i++){
        if(accumulate(v[i].begin(), v[i].end(), 0)==0) count++;
        if(v[0][i]+v[1][i]+v[2][i]+v[3][i]+v[4][i]==0) count++;
    }
    for(int i=0; i<5; i++){
        d1+=v[i][i];
        d2+=v[i][4-i];
    }
    if(d1==0) count++; if(d2==0) count++;
    if(count>=3) {return count;}
    else {return -1;}
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  vector<int> v2;
  int x;
  for(int i=0; i<5; i++){
    v2.clear();
    for(int j=0; j<5; j++){
        cin >> x;
        v2.push_back(x);
    }
    v.push_back(v2);
  }
  for(int i=0; i<25; i++){
    cin>>x;
    for(int k=0; k<5; k++){
        for(int j=0; j<5; j++){
            if(v[k][j] == x){
                v[k][j]=0;
            }
        }
    }
    int a = check();
    if(a>0){
        cout << i+1 <<'\n';
        break;
    }
  }
}