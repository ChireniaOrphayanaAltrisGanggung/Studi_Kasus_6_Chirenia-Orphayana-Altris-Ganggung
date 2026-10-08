import json

while True:
    print("--SISTEM MANAJEMEN INVENTARIS BARANG TOKO CENDANA--")
    print("1. Tampilkan Barang")
    print("2. Tambahkan Barang")
    print("3. Keluar")
    pilihan = input("Pilih Menu(1-3): ")

#Menampilkan Barang
    if pilihan == "1" :

        with open ("data.json", "r") as f:
            data = json.load(f)

        print("--DATA INVENTARIS BARANG TOKO CENDANA--")

        if len(data) == 0:
            print("Belum ada data barang.")
        else:
            for barang in data:
                print("Kode Barang :", barang["Kode Barang"])
                print("Nama Barang :", barang["Nama Barang"])
                print("Stok :", barang["Stok"])
                print("Harga : Rp.", barang["Harga"])
                print("---")

#Menambahkan Barang
    elif pilihan == "2":
        with open ("data.json", "r") as f:
            data = json.load(f)

        Kode_Barang = input("Masukan Kode Barang: ")
        Nama_Barang = input("Masukan Nama Barang: ")
        Stok = input("Masukan Stok Barang: ")
        Harga = input("Masukan Harga Barang: ")

        data_baru = {
            "Kode Barang":Kode_Barang,
            "Nama Barang":Nama_Barang,
            "Stok": Stok,
            "Harga": Harga
        }

        data.append(data_baru)
        with open("data.json", "w") as file: json.dump(data, file, indent=4)

        print("Data barang berhasil ditambahkan!")

#Keluar dari program
    elif pilihan == "3":
        print("Program selesai, terimakasih!")
        break

    else:
        print("Pilihan tidak tersedia, pilih 1 -3!")






