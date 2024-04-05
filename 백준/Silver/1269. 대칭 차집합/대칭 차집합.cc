#include <iostream>
#include <map>
using namespace std;


int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    int a, b; cin>>a>>b;
    int c = a+b;
    map<int, int> m;
    int x;
    while(c--){
        cin>>x;
        if(m.find(x)!=m.end()){
            m.erase(x);
        }else{
            m[x]=1;
        }
    }
    cout<<m.size()<<'\n';

}