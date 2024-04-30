#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<char> st;
    for(int i=0; i<s.length(); i++){
        char a = s[i];
        if(a=='(') st.push(a);
        else{
            if(st.empty())
                return false;
            else
                st.pop();
        }
    }
    if(st.empty())
        return true;
    else
        return false;

    return answer;
}