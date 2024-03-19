#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    while(true){
        stack<int> s;
        string str;
        getline(cin, str);
        
        for(int i=0;  i<str.length(); i++){
            if(str[i]=='(') 
                s.push(0);
            else if(str[i]=='[') s.push(1);
            else if(str[i]==')'){
                if(s.empty()){
                    s.push(-1);
                    break;
                }
                if(s.top()==0) s.pop();
                else{
                    s.push(-1);
                    break;
                }
            }else if(str[i]==']'){
                if(s.empty()){
                    s.push(-1);
                    break;
                }
                if(s.top()==1) s.pop();
                else{
                    s.push(-1);
                    break;
                }
            }else if(str[i]=='.'){
                break;
            }
        } 

        if(str.length()==1) return 0;
        else if(!s.empty()) cout<<"no"<<'\n';
        else cout<<"yes"<<'\n';
    }
}