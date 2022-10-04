#include <bits/stdc++.h>
using namespace std;
  
void fun()
{
	for(int i = 1; i <= 1000; i++){
		cout << i << endl;
	}
}
  
int main(){
	

    time_t start, end;
    fun();
    
    double time_taken = double(end - start);
    cout << "O tempo de execução do programa foi de: " << fixed
         << time_taken << setprecision(5);
    cout << " seg " << endl;
    return 0;
}
