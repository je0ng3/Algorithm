#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m; cin>> n>> m;
    int j; cin>>j;
    int count=0;
    int x=1;
    while(j--){
        int a; cin>>a;
        while(x>a || a>x+m-1){
            if(x>a) x--;
            else if(a>x+m-1) x++;
            count++; 
        }
    }
    cout<<count<<'\n';
}