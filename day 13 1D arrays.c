#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
 int n=0,a=0,sum=0,i=0;
 scanf ("%d",&n);
  int*arry=(int*) malloc(n*sizeof (int));
  while(a<n)
  {
      scanf("%d",&arry[a]);
      sum=sum+arry[a];
      a++;
 }
  free(arry);
  printf("%d",sum);
       return 0;
}
