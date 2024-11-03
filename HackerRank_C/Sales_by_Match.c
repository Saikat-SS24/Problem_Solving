#include<stdio.h>
int main()
{
    int n,i,j,pair=0,a[101]={0};
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&j);
        a[j]++;
    }
    for(i=0;i<101;i++)
    pair=a[i]/2+pair;
    printf("%d",pair);
    
    return 0;
}
