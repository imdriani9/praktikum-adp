#include <iostream>
using namespace std;

int main() {
	
	string nama, jenis_kelamin;
	int umur, pnr, maskapai, jumlah_kursi, harga_tiket, harga_tiket2, harga_tiket3, harga_tiket1, harga_tiket4, harga_tiket5, harga_tiket6, total_harga;
	float e=1000000, b=3000000, f=7000000;
	cout<<"Nama    : Imdriani Nengsih"<<endl;
	cout<<"NIM     : 2310432035"<<endl;
	cout<<"Shift   : 4"<<endl;
	cout<<endl;
	cout<<endl;
	cout<<"=========================== LAYANAN PEMESANAN TIKET PESAWAT ==========================="<<endl;
	cout<<endl;
	cout<<"Selamat Datang di Layanan Pemesanan Tiket Pesawat"<<endl;
	cout<<"Silakan Masukkan Data Diri Anda"<<endl;
	cout<<endl;
	cout<<"             Nama          : ";
	cin>>nama;
	cout<<"             Umur          : ";
	cin>>umur;
	cout<<"             Jenis Kelamin : ";
	cin>>jenis_kelamin;
	cout<<endl;
	cout<<endl;
	cout<<endl;
	cout<<endl;
	cout<<endl;
	cout<<"_-_-_-_-_-_-_-_-_-_-_-_-_- TUJUAN KEBERANGKATAN DARI PADANG _-_-_-_-_-_-_-_-_-_-_-_-_-"<<endl;
	cout<<endl;
	cout<<"Silakan Pilih Tujuan Pernerbangan Anda"<<endl;
	cout<<"                               |   1. MAKASAR   |"<<endl;
	cout<<"                               |   2. BANTEN    |"<<endl;
	cout<<"                               |   3. BALI      |"<<endl;
	cout<<"---------------------------------------------------------------------------------------"<<endl;
	cout<<"Masukkan nomor urut tujuan penerbangan anda : ";
	cin>>pnr;
	if(pnr==1) {
		cout<<"    Rute penerbangan anda : PADANG-MAKASAR";
	}
	else if (pnr==2) {
		cout<<"    Rute penerbangan anda : PADANG-BANTEN";
	}
	else if (pnr==3) {
		cout<<"    Rute penerbangan anda : PADANG-BALI";
	}
	cout<<endl;
	cout<<endl;
	cout<<endl;
	cout<<endl;
	cout<<endl;
	cout<<"_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- KELAS PENERBANGAN _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"<<endl;
	cout<<"             _______________________________________________________"<<endl;
	cout<<"            |       Jenis Maskapai      ||           Harga          |"<<endl;
	cout<<"            |=======================================================|"<<endl;
	cout<<"            |   1. EKONOMI              ||       Rp.1.000000        |"<<endl;
	cout<<"            |   2. BISNIS               ||       Rp.3.000000        |"<<endl;
	cout<<"            |   3. FIRST CLASS          ||       Rp.7.000000        |"<<endl;
	cout<<"             -------------------------------------------------------"<<endl;
	cout<<" Diskos 25% untuk pembelian lebih dari 3 tiket"<<endl;
	cout<<"-----------------------------------------------------------------------------------------"<<endl;
	cout<<"Silakan masukan jenis maskapai anda : ";
	cin>>maskapai;
	cout<<"Jumlah kursi yang akan dipesan      : ";
		cin>>jumlah_kursi;
	if (maskapai==1) {
		total_harga=harga_tiket=jumlah_kursi*e;
		total_harga=harga_tiket1= 0.75*jumlah_kursi*e;
		if (jumlah_kursi<3) {
			cout<<"Total harga                         : Rp."<<harga_tiket<<endl;
		}
		else if (jumlah_kursi>3) {
			cout<<"Total harga                         : Rp."<<harga_tiket1<<endl;
		}
	}
	else if (maskapai==2) {
		total_harga=harga_tiket2=jumlah_kursi*b;
		total_harga=harga_tiket3=0.75*jumlah_kursi*b;
		if (jumlah_kursi<3) {
			cout<<"Total harga                         : Rp."<<harga_tiket2<<endl;
		}
		else if (jumlah_kursi>3) {
			cout<<"Total harga                         : Rp."<<harga_tiket3<<endl;
		}
	}
		
	else if (maskapai==3) {
		total_harga=harga_tiket4=jumlah_kursi*f;
		total_harga=harga_tiket5=0.75*jumlah_kursi*f;
		if (jumlah_kursi<3) {
			cout<<"Total harga                         : Rp."<<harga_tiket4<<endl;
		}
		else if (jumlah_kursi>3) {
			cout<<"Total harga                         : Rp."<<harga_tiket5<<endl;
		}
	}
	cout<<endl;
	cout<<endl;
	cout<<endl;
	cout<<endl;
	cout<<endl;
	cout<<"                              STRUK PEMESANAN"<<endl;
	cout<<"                    Nama           : "<<nama<<endl;
	cout<<"                    Umur           : "<<umur<<endl;
	cout<<"                    Jenis Kelamin  : "<<jenis_kelamin<<endl;
	cout<<"                    --------------------------------"<<endl;
	cout<<"                    Kota Tujuan    : ";
	if(pnr==1) {
		cout<<"MAKASAR";
	}
	else if (pnr==2) {
		cout<<"BANTEN";
	}
	else if (pnr==3) {
		cout<<"BALI";
	}
	cout<<endl;
	cout<<"                    Jenis Maskapai : ";
	if (maskapai==1) {
		cout<<"EKONOMI";
	}
	else if (maskapai==2) {
		cout<<"BISNIS";
	}
	else if (maskapai==3) {
		cout<<"FIRST CLASS";
	}
	cout<<endl;
	cout<<"                    Jumlah Tiket   : "<<jumlah_kursi<<endl;
	cout<<"                    Total Harga    : Rp."<<total_harga<<endl;
}
