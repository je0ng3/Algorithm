#include <iostream>
#include <map>
using namespace std;


int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    int a, b; cin>>a>>b;
    map<int, int> m;
    int x;
    while(a--){
        cin>>x;
        m[x]=1;
    }
    while(b--){
        cin>>x;
        if(m.find(x)!=m.end())
            m.erase(x);
    }
    cout<<m.size()<<'\n';
    for (auto it : m)
        cout<<it.first<<' ';

}