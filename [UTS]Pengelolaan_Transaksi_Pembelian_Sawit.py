#Anggota Kelompok
anggota = ["HANIA DWI ANDINI", "SULTHAN RAFI AZIS", "MUHAMMAD FARHAN FIKRILLAH", "MOHAMMAD INDRA RAMADHANI", "NAJMAH TIANNISA HAKIM"]
print("\nKelompok 10:")
for kelompok in anggota:
    print(kelompok)
print("\n")


pembelian = []
urutan = 0

while True:
    print("=======================================================")
    print("======== Pengelolaan Transaksi Pembelian Sawit ========")
    print("=======================================================\n")
    print("1. Menambah transaksi pembelian sawit")
    print("2. Lihat daftar pembelian sawit")
    print("3. Hapus daftar pembelian sawit")
    print("4. Keluar dari program")
    print("\n-------------------------------------------------------\n") 
        
    pilihan = input("Pilih menu (1/2/3/4): ")
        
    if pilihan == "1" :
        print("\n--------------- Kelola Pembelian sawit ----------------\n")
        print("Harga per-kg: Rp. 2000")
        berat = float(input("Total berat sawit yang ingin dibeli (kg): "))
        harga = float(2000)
        hasil = float(berat * harga)
        print(f"harga beli: Rp. {hasil}")
        if hasil >= 100000000 :
            print("Pembelian tidak valid, tidak bise melebihi Rp. 100000000")
        else :
            nama = input("Masukkan nama penjual: ")
            hari = input("Masukkan hari pembelian: ")
            tgl = input("Masukkan tanggal pembelian (Tanggal/Bulan/Tahun):")
            urutan += 1
            pembelian_data = [urutan, nama, hari, tgl, berat, hasil]
            pembelian.append(pembelian_data)
        print("\n------------- Pembelian berhasil tercatat -------------\n")

    elif pilihan == "2" :
        if not pembelian:
            print("Belum ada data pembelian.\n")
        else:
            print("\n------------------ Daftar pembelian -------------------\n")
            for pembelian_data in pembelian: 
                print(f"Pembelian ke-{pembelian_data[0]}:")
                print(f"Nama penjual: {pembelian_data[1]}")
                print(f"Waktu pembelian: {pembelian_data[2]}, {pembelian_data[3]}")
                print(f"Total berat sawit yang dibeli: {pembelian_data[4]} Kg")
                print(f"Harga beli: Rp. {pembelian_data[5]}")
                print("-------------------------------------------------------")
            total_pembelian_keseluruhan = sum(data[5] for data in pembelian)
            print(f"\nTotal pengeluaran keseluruhan: Rp. {total_pembelian_keseluruhan}\n")

    elif pilihan == "3":
        if not pembelian:
            print("Belum ada data pembelian untuk dihapus.\n")
        else:
            print("\n------------- Hapus Data Pembelian Sawit --------------\n")
            for pembelian_data in pembelian:
                print(f"Pembelian ke-{pembelian_data[0]}:")
                print(f"Nama penjual: {pembelian_data[1]}")
                print(f"Waktu pembelian: {pembelian_data[2]}, {pembelian_data[3]}")
                print(f"Total berat sawit yang dibeli: {pembelian_data[4]} Kg")
                print(f"Harga beli: Rp. {pembelian_data[5]}")
                print("-------------------------------------------------------")
            urutan_pembelian = int(input("\nUrutan pembelian yang akan dihapus: \n")) - 1
            print("-------------------------------------------------------\n")
            if urutan_pembelian < len(pembelian):
                pembelian.pop(urutan_pembelian)
                urutan -= 1
                for i in range(len(pembelian)):
                    pembelian[i][0] = i + 1
                print("Data pembelian berhasil dihapus dan urutan diperbarui.\n")
            else:
                    print("Urutan pembelian tidak valid.\n")
        
    elif pilihan == "4":
        print("Terima kasih! Aplikasi ditutup.")
        print("\n=======================================================")
        print("\n")
        break
        
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.\n")
