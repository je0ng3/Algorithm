#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, score, p; cin>>n>>score>>p;
    if(n==0){
        cout<<1<<'\n';
        return 0;
    }
    vector<pair<int,int>> v;
    for(int i=1; i<=n; i++){
        int a; cin>>a;
        v.push_back(make_pair(a,i));
        if(i!=1 && v[i-1].first==v[i].first)
            v[i].second = v[i-1].second;
    }
    if(n>=p){
        if(v[n-1].first>=score) {
            cout<<-1<<'\n';
            return 0;
        }
    }
    for(int i=0; i<n; i++){
        if(v[i].first<=score){
            cout<<v[i].second<<'\n';
            return 0;
        }
    }
    cout<<n+1<<'\n';

}