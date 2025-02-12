from datetime import datetime

# ==== Super class ====
class Handphone:
    def __init__(self, merk: str, model: str, tanggal_jual: str, harga: float, jumlah: int, warna: str, memori_internal: int):
        self.merk = merk
        self.model = model
        self.tanggal_jual = datetime.strptime(tanggal_jual, "%d-%m-%Y")
        self.harga = harga
        self.jumlah = jumlah
        self.spesifikasi = {
            "Warna": warna,
            "Memori Internal (GB)": memori_internal
        }

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

# ==== Subclasses ====
class iPhone(Handphone): 
    def __init__(self, model, tanggal_jual, harga, jumlah, warna, memori_internal, ios_version: float, face_id: bool):
        super().__init__("iPhone", model, tanggal_jual, harga, jumlah, warna, memori_internal)
        self.ios_version = ios_version
        self.face_id = face_id

    def tampilkan_info_iphone(self):
        super().tampilkan_info()
        print(f"Versi iOS: {self.ios_version}")
        print(f"Face ID: {'Ya' if self.face_id else 'Tidak'}")

class Samsung(Handphone): 
    def __init__(self, model, tanggal_jual, harga, jumlah, warna, memori_internal, oneUI_version: float, s_pen: bool):
        super().__init__("Samsung", model, tanggal_jual, harga, jumlah, warna, memori_internal)
        self.oneUI_version = oneUI_version
        self.s_pen = s_pen

    def tampilkan_info_samsung(self):
        super().tampilkan_info()
        print(f"One UI Version: {self.oneUI_version}")
        print(f"S-Pen Support: {'Ya' if self.s_pen else 'Tidak'}")

class Xiaomi(Handphone): 
    def __init__(self, model, tanggal_jual, harga, jumlah, warna, memori_internal, miUI_version: float, watt_fastCharge: int):
        super().__init__("Xiaomi", model, tanggal_jual, harga, jumlah, warna, memori_internal)
        self.miUI_version = miUI_version
        self.watt_fastCharge = watt_fastCharge

    def tampilkan_info_xiaomi(self):
        super().tampilkan_info()
        print(f"MIUI Version: {self.miUI_version}")
        print(f"Fast Charging (Watt): {self.watt_fastCharge}W")

# ==== Subsystem 1: Menambah Data Handphone ====
class Tambah_Data:
    def __init__(self):
        self.daftar_hp = []

    def input_user(self):
        model = input("Masukkan model handphone: ")
        harga = float(input("Masukkan harga handphone (Satuan): "))
        jumlah = int(input("Masukkan jumlah handphone: "))
        warna = input("Masukkan warna handphone: ").title()
        memori_internal = int(input("Masukkan memori internal handphone (GB): "))
        return model, harga, jumlah, warna, memori_internal

    def tambah_handphone(self):
        tanggal_jual = input("Masukkan tanggal jual handphone (dd-mm-yyyy): ")

        while True:
            merk = input("Masukkan jenis handphone (iPhone/Samsung/Xiaomi) atau 'done' untuk selesai: ").lower()
            if merk == "done":
                break

            if merk == "iphone":
                model, harga, jumlah, warna, memori_internal = self.input_user()
                ios_version = float(input("Versi iOS: "))
                face_id = input("Mendukung Face ID? (y/n): ").lower() == 'y'
                self.daftar_hp.append(iPhone(model, tanggal_jual, harga, jumlah, warna, memori_internal, ios_version, face_id))
            elif merk == "samsung":
                model, harga, jumlah, warna, memori_internal = self.input_user()
                oneUI_version = float(input("Versi One UI: "))
                s_pen = input("Mendukung S-Pen? (y/n): ").lower() == 'y'
                self.daftar_hp.append(Samsung(model, tanggal_jual, harga, jumlah, warna, memori_internal, oneUI_version, s_pen))
            elif merk == "xiaomi":
                model, harga, jumlah, warna, memori_internal = self.input_user()
                miUI_version = float(input("Versi MIUI: "))
                watt_fastCharge = int(input("Fast Charging (Watt): "))
                self.daftar_hp.append(Xiaomi(model, tanggal_jual, harga, jumlah, warna, memori_internal, miUI_version, watt_fastCharge))
            else:
                print("Merk tidak tersedia")

        return self.daftar_hp, tanggal_jual
    
    def tampilkan_all_info(self, tanggal_jual):
        print(f"\n==== Data Handphone yang Terjual pada {tanggal_jual} ====")
        for hp in self.daftar_hp:
            hp.tampilkan_info()

# ==== Subsystem 2: Penghitungan Penjualan ====
class Hitung_Penjualan:
    def __init__(self, daftar_hp):
        self.daftar_hp = daftar_hp
        self.total_all = 0
        self.data_terjual = {"iPhone": 0, "Samsung": 0, "Xiaomi": 0}

    def hitung_total_penjualan(self):
        for hp in self.daftar_hp:
            self.data_terjual[hp.merk] += hp.total_penjualan()
            self.total_all += hp.total_penjualan()

    def tampilkan_hasil(self):
        self.hitung_total_penjualan()

        print("\n==== Total Penjualan Per Merk ====")
        for merk, total in self.data_terjual.items():
            print(f"{merk}: Rp{total:,.2f}")

        print("\n==== Total Semua Penjualan ====")
        print(f"Total keseluruhan penjualan sebesar Rp{self.total_all:,.2f}")


# ==== Facade Pattern: Manajemen_Penjualan ====
class Manajemen_Penjualan:
    def __init__(self):
        self.tambah_data = Tambah_Data()

    def mulai_proses(self):
        self.daftar_hp, tanggal_jual = self.tambah_data.tambah_handphone()

        if not self.daftar_hp:
            print("Tidak ada data handphone yang ditambahkan.")
            return

        penghitungan = Hitung_Penjualan(self.daftar_hp)

        self.tambah_data.tampilkan_all_info(tanggal_jual)
        penghitungan.tampilkan_hasil()

# ==== Main Program ====
if __name__ == "__main__":
    penjualan = Manajemen_Penjualan()
    print("DATA PENJUALAN HANDPHONE TOKO ABC")
    print("=" * 45 + "\n")

    penjualan.mulai_proses()
