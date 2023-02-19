phonebook = {}      # membuat dictionary dimana key = nama dan value = nomor telepon

def menu():
    print("+----------------------------+")
    print("|        PHONE BOOK          |")
    print("+----------------------------+")
    print("| 1. Lihat Semua Kontak      |")
    print("| 2. Masukkan Kontak Baru    |")
    print("| 3. Hapus Kontak            |")
    print("| 4. Cari Kontak             |")
    print("| 5. Update Kontak yang Ada  |")
    print("| 6. Keluar                  |")
    print("+----------------------------+\n")
    
    
def Display():
    with open("PhoneBook.txt", "r") as file:       
        kontak = file.read()        # kontak sebagai variabel penyimpan seluruh isi file PhoneBook.txt
    if not kontak:
        print("File tidak ada")
    else:        
        print("\n    Daftar Kontak       ")
        print("Nama\t\tNomor Telepon       ")
        print(kontak)

def Insert():
    nama = input("Masukkan Nama : ")
    nomor = input("Masukkan nomor telepon : ")
    phonebook[nama] = nomor         # untuk menambah key-value di dict phonebook
    with open("PhoneBook.txt", "a") as file:        # a : append untuk menambah data baru di baris bawah file
        file.write(nama + '\t\t' + nomor + '\n')
        print("Kontak Telah Dimasukkan\n")
  
def Delete():
    nama = input("Masukkan nama kontak yang akan dihapus : ")
    with open("PhoneBook.txt", "r") as file:
        line = file.readlines()         # line sebagai variabel penyimpan satu per satu data file sesuai baris
    with open ("PhoneBook.txt", "w") as file:
        for kontak in line:             # kontak digunakan untuk mengakses setiap elemen pada line
            if not kontak.startswith(nama):     # startwith mengembalikkan nilai TRUE apabila string nama dimulai dengan kontak (untuk memfilter kriteria tertentu)
                file.write(kontak)              # apabila tidak sama maka akan ditulis lagi di file
        print("Kontak Telah Dihapus\n")

def Search():
    nama = input("Masukkan nama yang dicari : ")
    with open("PhoneBook.txt", "r") as file:
        for kontak in file:
            if nama in kontak:          # apabila nama yang diinput ada pada file (yang diakses kontak) maka nama yang dicari ketemu
                print("Kontak Ditemukan\n" + kontak)                                                         
                return
            
    print("Kontak Tidak Ditemukan\n")
  
def Update():
    nama = input("Masukkan nama kontak yang akan di-update : ")
    with open("PhoneBook.txt", "r") as file:
        line = file.readlines()
    with open("PhoneBook.txt", "w") as file:
        for kontak in line:
            if kontak.startswith(nama):     # apabila string nama dimulai dengan kontak maka if bernilai true
                pilih = input("1. Nama\n2. Nomor Telepon \nPilih update : ")
                if pilih == "1":
                    namabaru = input("Masukkan Nama Baru : ")
                    nomor = kontak.split('\t\t')[1].strip()     # digunakan untuk mengambil nomor telepon yang ada di file (diakses oleh kontak)    # strip() untuk menghapus spasi dari awal dan akhir string nomor telepon
                    kontak = namabaru + '\t\t' + nomor + '\n'   # karena yang diinput hanya nama, maka untuk nomor mengambil dari file
                elif pilih == "2":
                    nomorbaru = input("Masukkan Nomor yang Baru: ")
                    nama = kontak.split('\t\t')[0].strip()      # digunakan untuk mengambil nama telepon yang ada di file (diakses oleh kontak) 
                    kontak = nama + '\t\t' + nomorbaru + '\n'   # karena yang diinput hanya nomor, maka untuk nama mengambil dari file
                file.write(kontak)
                print(f"Kontak {nama} berhasil diperbarui\n")
            else:
                file.write(kontak)

while True:
    menu()
    pilihan = input("Masukkan pilihan menu : ")
    if pilihan == "1":
        Display()
    elif pilihan == "2":
        Insert()
    elif pilihan == "3" :
        Delete()
    elif pilihan == "4" :
        Search()
    elif pilihan == "5" :
        Update()
    else :break
