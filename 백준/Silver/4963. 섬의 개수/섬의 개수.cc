#include <iostream>

using namespace std;

#define MAX 1001    
int arr[MAX][MAX];
int w, h;
int cnt = 0;
int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

void dfs(int i, int j){
    arr[i][j] = 0;
    for(int k = 0; k<8; k++){
      if(i+dx[k]>=0 && i+dx[k]<h && j+dy[k]>=0 && j+dy[k]<w){
        if(arr[i+dx[k]][j+dy[k]]==1)
          dfs(i+dx[k],j+dy[k]);
        else
          continue;
        }
    }
}

int main(){
    for(int i=0; i<MAX; i++)
      for(int j=0; j<MAX; j++)
        arr[i][j]=0;
    cin >>w >>h;
    while(w!=0 && h!=0){
        for(int i =0; i<h; i++)
            for(int j = 0; j<w; j++)
                cin >> arr[i][j];
        for(int i =0; i<h; i++){
            for(int j = 0; j<w; j++){
                if(arr[i][j] == 1 ){
                    dfs(i,j);
                    cnt++;
                }
                else
                  continue;
            }
        }
        cout<<cnt<<"\n";
        cnt=0;
        cin >>w >>h;
    }
    return 0;
}