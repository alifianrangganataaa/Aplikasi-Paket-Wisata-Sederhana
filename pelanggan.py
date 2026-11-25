class Pelanggan:
    # Constructor
    def __init__(self, nama, telepon):
        # Atribut private
        self.__nama = nama
        self.__telepon = telepon
        self.__daftar_pesanan = []  # berisi object PaketWisata

    # Getter
    def get_nama(self):
        return self.__nama

    def get_telepon(self):
        return self.__telepon

    # Method: memesan paket wisata
    def pesan_paket(self, paket):
        if paket.kurangi_kuota():
            self.__daftar_pesanan.append(paket)
            return True
        return False

    # Method: menampilkan pesanan pelanggan
    def tampilkan_pesanan(self):
        print("Pelanggan:", self.__nama, "-", self.__telepon)
        for paket in self.__daftar_pesanan:
            print("-", paket.get_nama(), ":", paket.get_harga())