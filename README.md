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
![classSingleton](https://github.com/user-attachments/assets/71e4941a-155a-474e-902e-39da376273d2)
- 🔹 `PendataanPenjualan` → Singleton yang menyimpan semua data handphone yang dijual.
- 🔹 `Handphone` → Superclass dengan atribut umum.
- 🔹 `iPhone`, `Samsung`, `Xiaomi` → Subclass dengan atribut khusus.

## Use Case Diagram
![use case](https://github.com/user-attachments/assets/4b4efc06-60a4-4a4a-8573-23f2dfae0e86)

### **🧍‍♂️Aktor utama:**
Admin (pengguna sistem)

### **🗒️Use Case:**
- Menambahkan data handphone → Admin memasukkan informasi handphone yang terjual.
- Melihat daftar handphone terjual → Menampilkan daftar semua penjualan handphone yang telah diinput.
- Melihat total penjualan per merek → Menampilkan total penjualan berdasarkan merek handphone.
- Melihat total seluruh penjualan → Menghitung jumlah semua penjualan pada tanggal tersebut.

## 🔄 Alur Kerja Program (Sequence Diagram) Singleton Pattern
![sequenceSingleton](https://github.com/user-attachments/assets/95a1de40-a565-4d8a-93e3-07bdef0ffdd6)

**1️⃣ Admin Memasukkan Data**

Admin menginputkan tanggal penjualan handphone.
Sistem meminta detail handphone (merk, model, harga, dll.).

**2️⃣ Penyimpanan Data ke Singleton**

Data handphone dikirim ke PendataanPenjualan (Singleton).
Singleton membuat objek handphone sesuai merek dan menyimpannya dalam daftar tunggal.

**3️⃣ Permintaan & Perhitungan Data**

Admin meminta daftar penjualan.
Singleton menghitung total penjualan per merek dan keseluruhan.

**4️⃣ Menampilkan Laporan**

Sistem mengembalikan daftar handphone dan total penjualan.
Admin melihat hasil laporan penjualan.


# Facade Pattern 🎭
![facade](https://github.com/user-attachments/assets/1d96adfd-0bbb-4be8-ae8f-0da0cbfa692d)

## 🏗️ Struktur Kelas (Class Diagram) Facade Pattern
![facadeClass](https://github.com/user-attachments/assets/2fa5e5bc-edb9-406d-9e74-04a8f893b683)

## Use Case Diagram
![use case](https://github.com/user-attachments/assets/4b4efc06-60a4-4a4a-8573-23f2dfae0e86)

## 🔄 Alur Kerja Program (Sequence Diagram) Facade Pattern
![facadeSequence](https://github.com/user-attachments/assets/f5478a69-dc26-4e50-80c7-f95a9f92f062)

# Mediator Pattern 🗣️
![mediator](https://github.com/user-attachments/assets/a261f00e-450d-4d2c-b79e-831a5a18dd2b)

## 🏗️ Struktur Kelas (Class Diagram) Mediator Pattern
![mediatorClass](https://github.com/user-attachments/assets/eb94d72b-ec89-4226-96c7-d1cd3a907f6d)

## Use Case Diagram
![use case](https://github.com/user-attachments/assets/4b4efc06-60a4-4a4a-8573-23f2dfae0e86)

## 🔄 Alur Kerja Program (Sequence Diagram) Mediator Pattern
![](https://github.com/user-attachments/assets/011bec1e-80b6-48e6-8a20-d93cbf67ae89)

