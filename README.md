# 📄Laporan Design Pattern
## Fellicia Devina

# Singleton Pattern 🧍‍♂️
Singleton Pattern adalah pola desain yang memastikan hanya ada satu instance dari suatu kelas dan menyediakan akses global ke instance tersebut.
Pada program ini, PendataanPenjualan menggunakan Singleton Pattern untuk menyimpan daftar handphone yang dijual.
![bentukUmum](https://github.com/user-attachments/assets/e9c8a363-c9d7-43bf-95ac-5ac18fd1eb26)

Dengan ini:
- Hanya ada satu objek yang menangani data penjualan.
- Mencegah duplikasi data saat program dijalankan.
- Memudahkan akses data ke daftar penjualan tanpa harus membuat banyak objek.

## 🏗️ Struktur Kelas (Class Diagram) Singleton Pattern
![classSingleton](https://github.com/user-attachments/assets/b1015eca-cf58-428a-a082-8c8d3a078bef)

- 🔹 `PendataanPenjualan` → Singleton yang mengelola data handphone yang terjual dan menghitung total penjualan.
- 🔹 `Handphone` → Superclass dengan atribut umum untuk membuat objek handphone.
- 🔹 `iPhone`, `Samsung`, `Xiaomi` → Subclass Handphone dengan atribut khusus.

## Use Case Diagram
![usecase](https://github.com/user-attachments/assets/1995dc4f-878e-4fdd-ad50-707a5c248ad4)


### **🧍‍♂️Aktor utama:**
Admin (pengguna sistem)

### **🗒️Use Case:**
- Admin dapat memasukkan informasi handphone yang terjual dan melihat semua daftar penjualan handphone yang telah diinput.
- Melihat  total penjualan berdasarkan merek handphone dan total seluruh penjualan

## 🔄 Alur Kerja Program (Sequence Diagram) Singleton Pattern
![sequenceSingleton](https://github.com/user-attachments/assets/0bc37139-091d-4d0d-ad64-e99dcee38f94)

** 1.  Admin Memasukkan Data**

Admin menginputkan tanggal penjualan handphone.
Sistem meminta detail handphone (merk, model, harga, dll.).

**2️. Menyimpanan Data ke Singleton**

Data handphone dikirim ke  `PendataanPenjualan` (Singleton).
Singleton mengambil objek yang sudah dibuat pada kelas `Handphone` dan menyimpannya dalam daftar tunggal.

**3️. Permintaan & Perhitungan Total Penjualan**

Admin meminta daftar penjualan.
Singleton menghitung total penjualan per merk dan keseluruhan.

**4️. Menampilkan Laporan**

Program utama menampilkan daftar handphone dan total penjualan.
Admin dapat melihat hasil laporan penjualan.


# Facade Pattern 🎭
![facade](https://github.com/user-attachments/assets/1d96adfd-0bbb-4be8-ae8f-0da0cbfa692d)

Facade Pattern adalah pola desain yang menyediakan antarmuka tunggal untuk berinteraksi dengan sistem yang kompleks.

Dengan menggunakan Facade Pattern: 
-  Pengguna tidak perlu berinteraksi langsung dengan subsistem.
-  Kode menjadi lebih terstruktur dan mudah dipahami.

## 🏗️ Struktur Kelas (Class Diagram) Facade Pattern
![facadeClass](https://github.com/user-attachments/assets/ced38177-5665-4300-90a6-c3de3544a719)
)

- 🔹 Facade Class `Manajemen_Penjualan`
➜ Bertindak sebagai antarmuka yang berinteraksi dengan pengguna (Admin), mengakses dan mengelola subsistem Tambah_Data dan Hitung_Penjualan.

- 🔹 Subsystem 1 `Tambah_Data`
➜ Bertanggung jawab untuk menerima input dan menyimpan data handphone yang terjual.

- 🔹 Subsystem 2 `Hitung_Penjualan`
➜ Menghitung total penjualan berdasarkan daftar handphone yang telah dimasukkan.

- 🔹 Class `Handphone` dan Subclass
➜ Mewakili berbagai jenis handphone yang memiliki spesifikasi unik.

## Use Case Diagram
![usecase](https://github.com/user-attachments/assets/1995dc4f-878e-4fdd-ad50-707a5c248ad4)

## 🔄 Alur Kerja Program (Sequence Diagram) Facade Pattern
![facadeSequence](https://github.com/user-attachments/assets/02b400f3-d623-4760-881f-f0e5895157c6)

### **🛠️ Tahapan Proses Sesuai Sequence Diagram**
1. Admin menjalankan program dan memanggil `mulai_proses()`.
2. Facade `Manajemen_Penjualan` meminta input data handphone kepada Admin.
3. Admin memasukkan data, dan Facade `Manajemen_Penjualan` memberikan inputan admin ke subsistem `Tambah_Data` dibuatkan objek handphone sesuai merk menggunakan subclass `Handphone`.
4. Data handphone disimpan ke dalam daftar di sistem `Tambah_Data`
5. Facade meminta sistem `Hitung_Penjualan` untuk menghitung total penjualan.
6. Facade menampilkan semua data handphone dan hasil perhitungan ke Admin.

# Mediator Pattern 🗣️
![mediator](https://github.com/user-attachments/assets/a261f00e-450d-4d2c-b79e-831a5a18dd2b)

Mediator Pattern adalah pola desain yang digunakan untuk mengelola komunikasi antara objek tanpa membuat mereka langsung saling berhubungan. Dengan ini:

- Objek-objek tidak perlu tahu detail objek lain yang berinteraksi dengannya.

- Mengurangi ketergantungan antar objek sehingga meningkatkan fleksibilitas dan skalabilitas kode.

- Memusatkan logika komunikasi dalam satu mediator, mempermudah pemeliharaan kode.

## 🏗️ Struktur Kelas (Class Diagram) Mediator Pattern
![mediator](https://github.com/user-attachments/assets/62d46d64-c1ab-4f1c-9705-8c01e44f87d5)


- 🔹 `Mediator` (Interface): Mendefinisikan metode tambah_penjualan() dan tampilkan_penjualan() yang harus diimplementasikan setiap mediator konkret.

- 🔹 `TokoMediator` (Concrete Mediator): Mengelola daftar handphone yang terjual dan bertanggung jawab untuk menampilkan daftar handphone dan total penjualan.

- 🔹 `Handphone` (Abstract Class): Merupakan superclass dari berbagai merk handphone, dengan atribut seperti merk, model, harga, dan metode daftar_terjual() untuk menambahkan data penjualan.

- 🔹 `iPhone`, `Samsung`, `Xiaomi` (Concrete Classes): Subclass dari Handphone yang mewakili berbagai jenis handphone dengan atribut spesifik masing-masing.

## Use Case Diagram
![usecase](https://github.com/user-attachments/assets/1995dc4f-878e-4fdd-ad50-707a5c248ad4)

## 🔄 Alur Kerja Program (Sequence Diagram) Mediator Pattern
![sequenceMediator](https://github.com/user-attachments/assets/cec32cea-48dc-445c-8f2b-6304ac75af46)

### **🔍 Penjelasan Alur Program**

1. Admin memasukkan tanggal penjualan handphone.
2. Main Program meminta input data handphone (merk, model, harga, dll.).
3. Data yang diinput ditambahkan ke daftar penjualan sesuai dengan merek handphone.
4. TokoMediator membuat objek handphone berdasarkan merek.
5. Handphone diinisialisasi dengan atribut yang diberikan.
6. Objek handphone ditambahkan ke daftar penjualan dalam mediator.
7. Main Program meminta mediator untuk menampilkan daftar penjualan.
8. Mediator mengambil daftar handphone yang telah terjual.
9.  Data dikirimkan kembali ke Main Program.
10.  Total penjualan dihitung berdasarkan harga dan jumlah unit.
11.  Data dikembalikan ke Main Program untuk ditampilkan.
12.  Main Program menampilkan daftar penjualan dan total penjualan kepada admin.

## CLI Apps

Meskipun kita menggunakan design pattern yang berbeda seperti Singleton Pattern, Facade Pattern, atau Mediator Pattern, hasil akhir dari program saat dijalankan akan tetap sama. Hal ini terjadi karena setiap design pattern hanya mengatur bagaimana komponen dalam sistem berinteraksi, bukan mengubah logika bisnis utama dari aplikasi.

### Inputan Admin:
![input](https://github.com/user-attachments/assets/9db8164f-ac71-4da6-8e05-3fb50153b670)

### Hasil:
![hasil](https://github.com/user-attachments/assets/00d9f7c9-604d-4e38-a0eb-cfcfe0f5d091)


