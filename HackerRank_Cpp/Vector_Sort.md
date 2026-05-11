## Vector-Sort

```bash
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    int ele;
    vector<int> v;
    
    for(int i = 0; i < n; i++)
    {
        cin >> ele;
        v.push_back(ele);
    }
    sort(v.begin(), v.end());
    for(int i : v)
    {
        cout << i << " " ;
    }
       
    return 0;
}
```