#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <string>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  string str; getline(cin, str);
  stack<char> s;
  for(int i=0; i<str.length(); i++){
    if(!s.empty() && (str[i]==' '||str[i]=='<')){
        while(!s.empty()){
            cout<<s.top();
            s.pop();
        }
        if(str[i]==' ') cout<<' ';
        else{
            while(str[i]!='>'){
                cout<<str[i];
                i++;
            }
        cout<<str[i];
        }
    }else if(str[i]=='<'){
        while(str[i]!='>'){
            cout<<str[i];
            i++;
        }
        cout<<str[i];
    }else if(s.empty() && str[i]==' '){
        cout<<' ';
    }else{
        s.push(str[i]);
    }
  }
  while(!s.empty()){
    cout<<s.top();
    s.pop();
  }

}