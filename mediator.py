from datetime import datetime
from abc import ABC, abstractmethod

    # ==== Mediator (Interface) ====
class Mediator(ABC):
    @abstractmethod
    def tambah_penjualan(self, handphone):
        pass

    @abstractmethod
    def tampilkan_penjualan(self, tanggal_jual):
        pass

    # ==== Concrete Mediator (Pengelola Komunikasi) ====
class TokoMediator(Mediator):
    def __init__(self):
        self.daftar_hp = []  # List menyimpan handphone yang terjual
    
    def tambah_penjualan(self, handphone):
        self.daftar_hp.append(handphone)

    def tampilkan_penjualan(self, tanggal_jual):
        print(f"\n==== Data Handphone yang Terjual pada {tanggal_jual} ====")
        total_all = 0
        data_terjual = {"iPhone": 0, "Samsung": 0, "Xiaomi": 0}
        
        for hp in self.daftar_hp:
            hp.tampilkan_info()
            total_penjualan = hp.total_penjualan()
            total_all += total_penjualan
            data_terjual[hp.merk] += total_penjualan
        
        print("\n==== Total Penjualan Per Merk ====")
        for merk, total in data_terjual.items():
            print(f"{merk}: Rp{total:,.2f}")
        
        print("\n==== Total Semua Penjualan ====")
        print(f"Total keseluruhan penjualan sebesar Rp{total_all:,.2f}")

    # ==== Abstarct Class Colleague (Kelas Dasar untuk Objek yang Berkomunikasi) ====
class Handphone(ABC):
    def __init__(self, mediator, merk, model, tanggal_jual, harga, jumlah, warna, memori_internal):
        self.mediator = mediator  # punya akses ke Mediator 
        self.merk = merk
        self.model = model
        self.tanggal_jual = datetime.strptime(tanggal_jual, "%d-%m-%Y")
        self.harga = harga
        self.jumlah = jumlah
        self.spesifikasi = {
            "Warna": warna,
            "Memori Internal (GB)": memori_internal
        }

    def daftar_terjual(self):
        self.mediator.tambah_penjualan(self)

    def tampilkan_info(self):
        print(f"\nMerk: {self.merk}")
        print(f"Model: {self.model}")
        print(f"Tanggal Jual: {self.tanggal_jual.strftime('%d-%m-%Y')}")
        print(f"Harga (satuan): Rp{self.harga:,.2f}")
        print(f"Jumlah: {self.jumlah} unit")
        print("Spesifikasi:")
        for key, value in self.spesifikasi.items():
            print(f"  - {key}: {value}")

    def total_penjualan(self):
        return self.jumlah * self.harga

    # ==== Concrete Colleague (Implementasi dari Handphone) ====
class iPhone(Handphone):    # Concrete Colleague 1
    def __init__(self, mediator, model, tanggal_jual, harga, jumlah, warna, memori_internal, ios_version, face_id):
        super().__init__(mediator, "iPhone", model, tanggal_jual, harga, jumlah, warna, memori_internal)
        self.ios_version = ios_version
        self.face_id = face_id
        self.daftar_terjual()  # Otomatis menambahkan ke daftar penjualan saat dibuat

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Versi iOS: {self.ios_version}")
        print(f"Face ID: {'Ya' if self.face_id else 'Tidak'}")

class Samsung(Handphone): # Concrete Colleague 2
    def __init__(self, mediator, model, tanggal_jual, harga, jumlah, warna, memori_internal, oneUI_version, s_pen):
        super().__init__(mediator, "Samsung", model, tanggal_jual, harga, jumlah, warna, memori_internal)
        self.oneUI_version = oneUI_version
        self.s_pen = s_pen
        self.daftar_terjual()

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"One UI Version: {self.oneUI_version}")
        print(f"S-Pen Support: {'Ya' if self.s_pen else 'Tidak'}")

class Xiaomi(Handphone): # Concrete Colleague 3
    def __init__(self, mediator, model, tanggal_jual, harga, jumlah, warna, memori_internal, miUI_version, watt_fastCharge):
        super().__init__(mediator, "Xiaomi", model, tanggal_jual, harga, jumlah, warna, memori_internal)
        self.miUI_version = miUI_version
        self.watt_fastCharge = watt_fastCharge
        self.daftar_terjual()

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"MIUI Version: {self.miUI_version}")
        print(f"Fast Charging (Watt): {self.watt_fastCharge}W")

# ==== Function Input User ====
def input_user():
    model = input("Masukkan model handphone: ")
    harga = float(input("Masukkan harga handphone (Satuan): "))
    jumlah = int(input("Masukkan jumlah handphone: "))
    warna = input("Masukkan warna handphone: ").title()
    memori_internal = int(input("Masukkan memori internal handphone (GB): "))
    return model, harga, jumlah, warna, memori_internal

# ==== Main Program ====
if __name__ == "__main__":
    toko = TokoMediator()
    print("DATA PENJUALAN HANDPHONE TOKO ABC")
    print("="*45 + "\n")
    
    tanggal_jual = input("Masukkan tanggal jual handphone (dd-mm-yyyy): ")
    
    while True:
        merk = input("Masukkan jenis handphone (iPhone/Samsung/Xiaomi) atau 'done' untuk selesai: ").lower()
        if merk == "done":
            break

        if merk == "iphone":
            model, harga, jumlah, warna, memori_internal = input_user()
            ios_version = float(input("Versi iOS: "))
            face_id = input("Mendukung Face ID? (y/n): ").lower() == 'y'
            iPhone(toko, model, tanggal_jual, harga, jumlah, warna, memori_internal, ios_version, face_id)
        
        elif merk == "samsung":
            model, harga, jumlah, warna, memori_internal = input_user()
            oneUI_version = float(input("Versi One UI: "))
            s_pen = input("Mendukung S-Pen? (y/n): ").lower() == 'y'
            Samsung(toko, model, tanggal_jual, harga, jumlah, warna, memori_internal, oneUI_version, s_pen)
        
        elif merk == "xiaomi":
            model, harga, jumlah, warna, memori_internal = input_user()
            miUI_version = float(input("Versi MIUI: "))
            watt_fastCharge = int(input("Fast Charging (Watt): "))
            Xiaomi(toko, model, tanggal_jual, harga, jumlah, warna, memori_internal, miUI_version, watt_fastCharge)
        
        else:
            print("Merk tidak tersedia")

    # Menampilkan laporan penjualan melalui Mediator
    toko.tampilkan_penjualan(tanggal_jual)
