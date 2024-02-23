#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n,m; cin>>n>>m;
    int seq[50]; fill_n(seq, 50, 1);
    int c=0; //가로줄에 필요한 경비수;
    for(int i=0; i<n; i++){
        string s; cin>>s;
        int a=1;
        for(int j=0; j<m; j++){
            if(s[j]=='X')  {
                seq[j]=0;
                a=0;
            }
        }
        if(a) c++;
    }
    int b=0;//세로줄에 필요한 경비수 
    for(int i=0; i<m; i++){
        b+=seq[i];
    }
    int count = (c>b)?c:b;
    cout<<count<<'\n';

}