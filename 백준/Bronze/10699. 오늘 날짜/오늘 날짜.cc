#include <iostream>
#include <ctime>
using namespace std;
#define _CRT_SECURE_NO_WARNINGS


int main(){
  time_t now = time(NULL);
  struct  tm*t = localtime(&now);

  printf("%d-%02d-%02d\n", t->tm_year+1900, t->tm_mon+1, t->tm_mday);
  return 0;
}
