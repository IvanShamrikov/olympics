#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
	//зчитуємо данні
    int n, m;
    cin>>n;
    cin>>m;
	//проходимо по кожному рядку у коробці
    int res = 0;
    for(int i = 1;i<=n;i++){
		//формула суми ряду арифметичної прогресії для знаходження кількості цукерок в трикутрій коробці
		int num = ((1+i)*i)/2;
		//якщо ділиться націло то інкрементуємо результат
        if(num%m == 0){
            res++;
        }
    }
    cout<<res<<"\n";
}