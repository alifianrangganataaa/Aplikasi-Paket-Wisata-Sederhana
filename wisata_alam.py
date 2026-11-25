from paket_wisata import PaketWisata


# Subclass: WisataAlam
class WisataAlam(PaketWisata):
    # Constructor 
    def __init__(self, nama, harga, kuota, lokasi, tingkat_kesulitan):
        super().__init__(nama, harga, kuota)  # panggil constructor superclass
        # Atribut private subclass
        self.__lokasi = lokasi
        self.__tingkat_kesulitan = tingkat_kesulitan

    # Getter
    def get_lokasi(self):
        return self.__lokasi

    def get_tingkat_kesulitan(self):
        return self.__tingkat_kesulitan

    # menampilkan info wisata alam
    def tampilkan_info(self):
        super().tampilkan_info()
        print("Jenis :", "Wisata Alam")
        print("Lokasi:", self.__lokasi)
        print("Level :", self.__tingkat_kesulitan)