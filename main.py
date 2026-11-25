from wisata_alam import WisataAlam
from wisata_budaya import WisataBudaya
from pelanggan import Pelanggan

# List penyimpan object paket wisata
daftar_paket = []

# Membuat 1 object pelanggan
pelanggan = Pelanggan("Budi", "081234567890")


# Mencari paket berdasarkan nama
def cari_by_nama(nama):
    for paket in daftar_paket:
        if paket.get_nama().lower() == nama.lower():
            return paket


# Menu 1: Tambah data
def tambah():
    jenis = input("Jenis (1=Alam, 2=Budaya): ")
    nama = input("Nama  : ")
    harga = int(input("Harga : "))
    kuota = int(input("Kuota : "))
    if jenis == "1":
        lokasi = input("Lokasi : ")
        level = input("Tingkat kesulitan : ")
        daftar_paket.append(WisataAlam(nama, harga, kuota, lokasi, level))
    else:
        situs = input("Situs budaya : ")
        bahasa = input("Bahasa pemandu : ")
        daftar_paket.append(WisataBudaya(nama, harga, kuota, situs, bahasa))
    print("Data berhasil ditambah!")


# Menu 2: Tampilkan data
def tampilkan():
    for paket in daftar_paket:
        paket.tampilkan_info()
        print("-" * 25)


# Menu 3: Cari data
def cari():
    paket = cari_by_nama(input("Nama paket: "))
    if paket:
        paket.tampilkan_info()
    else:
        print("Data tidak ditemukan.")


# Menu 4: Ubah data
def ubah():
    paket = cari_by_nama(input("Nama paket yang diubah: "))
    if paket:
        harga = int(input("Harga baru : "))
        kuota = int(input("Kuota baru : "))
        paket.ubah_data(harga, kuota)
        print("Data berhasil diubah!")
    else:
        print("Data tidak ditemukan.")


# Menu 5: Cek status data
def cek_status():
    for paket in daftar_paket:
        print(paket.get_nama(), ":", paket.cek_status())


# Menu 6: Pelanggan memesan paket
def pesan():
    paket = cari_by_nama(input("Nama paket yang dipesan: "))
    if paket and pelanggan.pesan_paket(paket):
        print("Pemesanan berhasil!")
    else:
        print("Pemesanan gagal (paket tidak ada / penuh).")


# Menu 7: Tampilkan pesanan pelanggan
def lihat_pesanan():
    pelanggan.tampilkan_pesanan()


# Dictionary menu: pilihan -> fungsi 
menu = {
    "1": tambah,
    "2": tampilkan,
    "3": cari,
    "4": ubah,
    "5": cek_status,
    "6": pesan,
    "7": lihat_pesanan,
}

# Data contoh agar mudah dicoba
daftar_paket.append(WisataAlam("Papandayan", 500000, 5, "Garut", "Sedang"))
daftar_paket.append(WisataBudaya("Kampung Naga", 300000, 3, "Tasikmalaya", "Indonesia"))

# Program utama
while True:
    print("\n=== APLIKASI PAKET WISATA ===")
    print("1. Tambah Paket")
    print("2. Tampilkan Paket")
    print("3. Cari Paket")
    print("4. Ubah Paket")
    print("5. Cek Status Paket")
    print("6. Pesan Paket")
    print("7. Tampilkan Pesanan")
    print("0. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "0":
        print("Terima kasih!")
        break
    if pilihan in menu:
        menu[pilihan]()  # panggil fungsi sesuai pilihan
    else:
        print("Pilihan tidak valid!")