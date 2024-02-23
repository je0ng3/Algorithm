#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int a; cin>>a;
    while(a!=0){
        string str=to_string(a);
            int check=1;
            for(int i=0; i<str.size(); i++){
                if(str[i]!=str[str.size()-i-1]){
                    check=0;
                }
            }
            if(check)
                cout<<"yes"<<'\n';
            else
                cout<<"no"<<'\n';
        cin>>a;
    }

}