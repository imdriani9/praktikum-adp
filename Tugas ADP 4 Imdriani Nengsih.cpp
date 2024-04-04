#include <iostream>
using namespace std;

int main() {
	cout<<"     Nama  : Imdriani Nengsih"<<endl;
	cout<<"     No BP : 2310431035"<<endl;
	cout<<endl;
	cout<<endl;
	int jumlah;
	jumlah=0;
	for(int i=1; i<=100; i++){
		if((i%3==0) || (i%5==0)) {
			std::cout<<"DOR"<<" ";
			jumlah++;
		}
		
		else {std::cout<<i<<"  ";
		}
		if(i%10==0){
		cout<<endl;
		}
	}
	cout<<endl;
	cout<<"Total DOR yang muncul sebanyak = "<<jumlah<<endl;
}
