#include <iostream>
#include <string>
using namespace std;


int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    string s; cin>>s;
    int count = 0;
    char check = s[0];
    for(int i=1; i<s.length(); i++){
        if(check!=s[i]){
            check=s[i];
            count++;
        }
    }
    cout<<int((count+1)/2)<<'\n';    
}