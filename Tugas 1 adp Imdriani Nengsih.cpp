#include <iostream>
#include<math.h>
using namespace std;

int main() {
	float n1, n2, n3, n4, n5, rata_rata, ragam, simpangan_baku;
    cout<<"         Menghitung Rata-rata, Ragam dan Simpangan Baku Nilai 5 Mahasiswa"<<endl;
    cout<<endl;
	cout<<"    Nama   : Imdriani Nengsih"<<endl;
	cout<<"    No. BP : 2310431035"<<endl;
	cout<<endl;
	cout<<"Nilai mahasiswa 1 = "; cin>>n1;
	cout<<"Nilai mahasiswa 2 = "; cin>>n2;
	cout<<"Nilai mahasiswa 3 = "; cin>>n3;
	cout<<"Nilai mahasiswa 4 = "; cin>>n4;
	cout<<"Nilai mahasiswa 5 = "; cin>>n5;
	cout<<endl;
	rata_rata=(n1+n2+n3+n4+n5)/5;
	cout<<"Rata-rata      = "<<rata_rata<<endl;
	ragam=(pow((n1-rata_rata),2) + pow((n2-rata_rata ),2) + pow((n3-rata_rata),2) + pow((n4-rata_rata),2) + pow((n5-rata_rata),2))/(5-1);
	cout<<"Ragam          = "<<ragam<<endl;
	simpangan_baku=sqrt(ragam);
	cout<<"Simpangan baku = "<<simpangan_baku<<endl;
	return 0;
}
