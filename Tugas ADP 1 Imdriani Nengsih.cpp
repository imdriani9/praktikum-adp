#include <iostream>
using namespace std;

int main() {
	const float pi=3.14;
	float r, luas, volume;
	cout<<"   Nama   : Imdriani Nengsih"<<endl;
	cout<<"   No. BP : 2310431035"<<endl;
	cout<<endl;
	cout<<"  Jari-jari = "; cin>>r;
	cout<<endl;
	volume=4/3*pi*r*r;
	cout<<"  Volume = "<<volume<<endl;
	luas=4*pi*r*r;
	cout<<"  Luas = "<<luas<<endl;
	return 0;
}
