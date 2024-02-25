#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

bool cmp(pair<char, int>&a, pair<char,int>&b){
    return a.second>b.second;
}

int main(){
  int n; cin>>n;
  map<char, int> word;
  vector<string> str;
  while(n--){
    string s; cin>>s;
    str.push_back(s);
    for(int i=0; i<s.size(); i++){
        if(word.count(s[i])>0){
            word[s[i]]+=pow(10,s.size()-i-1);
        }else{
            word[s[i]]=pow(10,s.size()-i-1);
        }
    }
  }
  vector<pair<char,int>>v;
  for(auto& i:word){
    v.emplace_back(i.first, i.second);
  }
  sort(v.begin(), v.end(), cmp);
  int num=9;
  for(auto& i:v){
    word[i.first]=num;
    num--;
  }
  int sum=0;
  for(auto& a:str){
    for(int i=a.size()-1; i>=0; i--){
        sum+=word[a[i]]*(pow(10,a.size()-i-1));
    }
  }
  cout<<sum<<'\n';

}
