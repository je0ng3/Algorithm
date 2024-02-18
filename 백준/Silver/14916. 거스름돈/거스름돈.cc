#include <iostream>
using namespace std;

int main(){
    int n; cin >> n;
    int count = 0;
    while((n%5)!=0){
        n-=2; count++;
        if(n<0) {
            count=-1;
            break;
        }
    }
    if(count!=-1){
       count += n/5;
        n = n%5;
        count += n/2;
    }
    cout << count << '\n';
}