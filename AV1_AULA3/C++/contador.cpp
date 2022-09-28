#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main(){
	
	clock_t tempo;
	tempo = clock();
	
	for(int n = 0; n <= 1000; n++){
		cout << n << endl;
	}
	
	cout << "\n";
	printf("Tempo:%f ",(clock() - tempo) / (double)ClOCKS_PER_SEC);
	cout << "\n";
	system("pause");
	return 0;
}
