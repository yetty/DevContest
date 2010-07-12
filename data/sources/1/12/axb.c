#include <stdio.h>

/*
  Ilustracni priklad pro PILSPROG
  netrvalo
  Time&date: 20:51 6.8.2007
  Provede soucin n dvojic zadanych celych cisel
 */

int main(void) {
  int i;
  int a,b;

  scanf("%d",&i);
  for (; i>0; i--){
    scanf("%d",&a);
    scanf("%d",&b);
    printf("%d\n",a*b);
  }
  return 0;
}
