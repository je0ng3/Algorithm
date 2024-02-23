#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n; cin>>n;
    int seq[20];
    for(int i=0; i<n; i++){
        cin>>seq[i];
    }
    int y=0, m=0;
    for(int i=0; i<n; i++){
        int yy = seq[i]/30; int mm = seq[i]/60;
        if(seq[i]<30) y+=10;
        else y+=(10*(yy+1));

        if(seq[i]<60) m+=15;
        else m+=(15*(mm+1));
    }

    if(y>m) cout<<"M "<<m<<'\n';
    else if(y<m) cout<<"Y "<<y<<'\n';
    else cout<<"Y M "<< y<<'\n';

}