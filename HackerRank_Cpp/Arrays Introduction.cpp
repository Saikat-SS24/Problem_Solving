#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    int a[1000],n,i;
    cin>>n;
    for(i=1;i<=n;i++)
    {
        cin>>a[i];
    }
    for(i=0;i<n;i++)
    {
        cout<<a[n-i]<<" ";
    }
    return 0;
}
