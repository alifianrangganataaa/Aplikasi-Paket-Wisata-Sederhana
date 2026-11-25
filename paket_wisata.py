# Superclass: PaketWisata
class PaketWisata:
    # Constructor
    def __init__(self, nama, harga, kuota):
        # Atribut private
        self.__nama = nama
        self.__harga = harga
        self.__kuota = kuota

    # Getter
    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_kuota(self):
        return self.__kuota

    # Method: mengubah harga dan kuota
    def ubah_data(self, harga, kuota):
        self.__harga = harga
        self.__kuota = kuota

    # Method: mengurangi kuota saat dipesan
    def kurangi_kuota(self):
        if self.__kuota > 0:
            self.__kuota -= 1
            return True
        return False

    # Method: cek status paket
    def cek_status(self):
        if self.__kuota > 0:
            return "Tersedia"
        return "Penuh"

    # Method: menampilkan info paket
    def tampilkan_info(self):
        print("Nama  :", self.__nama)
        print("Harga :", self.__harga)
        print("Kuota :", self.__kuota)