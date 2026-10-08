# Studi_Kasus_6_Chirenia-Orphayana-Altris-Ganggung

NAMA : CHIRENIA ORPHAYANA ALTRIS GANGGUNG

NIM : 2609116038

KELAS : A SISTEM INFORMASI

**A. PENJELASAN PROGRAM**

Program ini berjudul **Sistem Manajemen Inventaris Barang Toko Cendana** merupakan program yang digunakan untuk menyimpan, menampilkan dan menambahkan data barang. Data barang disimpan dalam file **JSON** (data.json) sehinggga data yang sudah ditambahkan dapat tersimpan secara permanen dan tidak hilang ketika program dijalanakan kembali.

1. IMPORT LIBRARY JSON

   Program menggunakan library json untuk membaca data dari file **JSON** dan menyimpan data kembali ke dalam file **JSON**.

   <img width="391" height="81" alt="image" src="https://github.com/user-attachments/assets/ef835c94-1a8a-4d7a-ab42-a628bed37d30" />

   <img width="780" height="612" alt="image" src="https://github.com/user-attachments/assets/fa2e1d83-7434-4452-8dfe-70c61254a4dd" />

2. PERULANGAN PROGRAM

   **while True** digunakan agar program terus berjalan dan menu dapat digunakan berulang kali. Program akan berhenti ketika pengguna memilih menu 3.Keluar

   <img width="309" height="66" alt="image" src="https://github.com/user-attachments/assets/0edb191d-46fc-473d-9ad9-e17c3b60d98c" />

3. MENAMPILKAN MENU

   Bagian ini menampilkan tiga pilihan menu kepada pengguna sehingga pengguna dapat memilih untuk menampilkan barang, menambahkan barang atau keluar dari program.

   <img width="643" height="165" alt="image" src="https://github.com/user-attachments/assets/8f43fb17-c322-48a6-84ce-ac375ae111e4" />

   OUTPUT PROGRAM :

   <img width="517" height="128" alt="image" src="https://github.com/user-attachments/assets/4df22e96-71e9-4995-82de-42077b8956d2" />

4. MENU 1 : MENAMPILKAN DATA BARANG

   Ketika pengguna memilih menu 1, program akan membaca data dari file **data.json**

   with open("data.json", "r") as f: data = json.load(f)

   Huruf "r" digunakan untuk membaca(read) file. Kemudian json.load() digunakan untuk mengambil data JSON dan memasukannya ke dalam variabel data. Selanjutnya program memeriska data, jika data kosong maka program akan print("Belum ada data barang") tetapi jika terdapat data maka program menggunakan perulangan **for** untuk menampilkan setiap barang.

   <img width="700" height="417" alt="image" src="https://github.com/user-attachments/assets/b58b5bc6-fc42-4588-bcf9-7eeed7a42ce7" />

   OUTPUT PROGRAM :

   <img width="503" height="464" alt="image" src="https://github.com/user-attachments/assets/686830d4-0ad1-42e1-941c-13f2a80d4610" />

5. MENU 2 : MENAMBAHKAN DATA BARANG

   Ketika pengguna memilih menu 2, program akan kembali membaca data yang sudah tersimpan. Kemudian pengguna diminta memasukan kode barang, nama barang, stok dan harga, data yang dimasukan akan dibuat menjadi sebuah dictionary di **data_baru** lalu dimasukan ke dalam data yang sudah ada menggunakan **data.append(data_baru)**.

   <img width="809" height="505" alt="image" src="https://github.com/user-attachments/assets/99f5ef84-a4d4-463c-ab6d-9b28ae1a725d" />

   OUTPUT PROGRAM :

   <img width="451" height="135" alt="image" src="https://github.com/user-attachments/assets/988014cb-b07d-48be-bf13-5bd800607de4" />

6. MENYIMPAN DATA SECARA PERMANEN

   Setelah data baru ditambahkan, program menyimpannya kembali ke file data.json.

   with open("data.json", "w") as file: json.dump(data, file, indent=4)

   Huruf "w" digunakan untuk menulis(write) data ke dalam file. **json.dump()** digunakan untuk menyimpan data ke dalam format JSON. Dengan bagian ini, data barang yang baru ditambahkan tidak hanya tersimpan selama program berjalan tetapi juga tersimpan di file data.json, sehingga dapat dibaca kembali ketika program di jalankan lagi.

   DATA BARU MASUK KE DALAM LIST DATA JSON :

    <img width="551" height="355" alt="image" src="https://github.com/user-attachments/assets/8228d8e4-2b1b-461e-b83e-87706e01c600" />

7. MENU 3 : KELUAR DARI PROGRAM

   Ketika pengguna memilih menu 3, program akan menampilkan print("Program selesai, terimakasih!") dan menghentikan perulangan while True menggunakan **break** sehingga program selesai dijalankan.

   <img width="505" height="124" alt="image" src="https://github.com/user-attachments/assets/ef899965-341f-4d6a-85cc-ec79c89e27bf" />

   OUTPUT PROGRAM :

   <img width="441" height="94" alt="image" src="https://github.com/user-attachments/assets/a2819422-d2d6-4135-a568-573997d88c27" />

8. PILIHAN MENU TIDAK VALID

   Jika pengguna memilih pilihan selain 1-3, program akan memberikan print("Pilihan tidak tersedia, pilih 1-3!") hal ini digunakan untuk memberitahu pengguna bahwa pilihan yang dimasukan tidak tersedia.

   <img width="516" height="79" alt="image" src="https://github.com/user-attachments/assets/e000bb6b-3608-4640-ae1f-a75a97c4c970" />

   OUTPUT PROGRAM :

   <img width="505" height="90" alt="image" src="https://github.com/user-attachments/assets/cdd47446-48a7-4225-b5f1-9bad03b374c1" />

**B. OUTPUT KESELURUHAN PROGRAM**

<img width="1198" height="557" alt="image" src="https://github.com/user-attachments/assets/34dc359f-80f0-43bd-bad6-7120620a7ef8" />

<img width="1214" height="473" alt="image" src="https://github.com/user-attachments/assets/7e5d6dd8-b2d2-4804-8518-dcf355ae0637" />


   

   
   



   
