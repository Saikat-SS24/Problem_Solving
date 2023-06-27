#include<iostream>
using namespace std;
void sumfour()
{
    int a,b,c,d;
    cin>>a;
    cin>>b;
    cin>>c;
    cin>>d;
    if(a>b && a>c && a>d)
    {
        cout<<a;
    }
    else if(b>a && b>c && b>d)
    {
        cout<<b;
    }
    else if(c>a && c>b && c>d)
    {
        cout<<c;
    }
    else if(d>a && d>b && d>c)
    {
        cout<<d;
    }
    else
    {
        cout<<0;
    }
}
int main()
{
    sumfour();
    return 0;
}
