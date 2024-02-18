#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int _sum(int n){
    int sum=0;
    while(n!=0){
        sum+=(n%10);
        n/=10;
    }
    return sum;
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    vector<int> v(1000,0),v2(1000,0);
    for(int i=0; i<n; i++){
        int x; cin >> x;
        if(v[x-1]!=0){
            v2[x-1]=x;
        }
        v[x-1]= x;
    }
    int max=0;
    v.erase(remove(v.begin(), v.end(), 0), v.end());
    v2.erase(remove(v2.begin(), v2.end(), 0), v2.end());
    for(int i=0; i<v.size()-1; i++){
        for(int j=i+1; j<v.size(); j++){
            int a = _sum(v[i]*v[j]);
            max = max>a? max: a;
        }
    }
    for(int i=0; i<v2.size(); i++){
        int b = _sum(v2[i]*v2[i]);
        max = max>b? max:b;
    }
    cout << max << '\n';
}