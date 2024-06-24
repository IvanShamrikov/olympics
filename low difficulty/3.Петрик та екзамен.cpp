#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int x, y, a, b;
    cin>>a;
    cin>>b;
    cin>>x;
    cin>>y;
    float maxPoints = a + b*2;
    float points = (a-x) + (b-y)*2;
    float result = (points/maxPoints)*100;

    if(result>51) {
        cout<<"YES";

    }else{
        cout<<"NO";
    }

}