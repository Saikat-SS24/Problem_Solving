#include<iostream>
#include<string>
using namespace std;
int main()
{
    string a,b,full;
    char x,y;
    getline (cin, a);
    getline (cin, b);
    cout<<a.length()<<" "<<b.length()<<endl;
    full = a + b;
    cout<<full;
    
    x = b[0];
    y = a[0];
    a[0] = x;
    b[0] = y;
    cout<<"\n";
    cout<<a<<" "<<b;
    return 0;
}
