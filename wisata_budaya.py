from paket_wisata import PaketWisata


# Subclass: WisataBudaya 
class WisataBudaya(PaketWisata):
    # Constructor
    def __init__(self, nama, harga, kuota, situs, bahasa_pemandu):
        super().__init__(nama, harga, kuota)  # panggil constructor superclass
        # Atribut private subclass
        self.__situs = situs
        self.__bahasa_pemandu = bahasa_pemandu

    # Getter
    def get_situs(self):
        return self.__situs

    def get_bahasa_pemandu(self):
        return self.__bahasa_pemandu

    # Override: menampilkan info wisata budaya
    def tampilkan_info(self):
        super().tampilkan_info()
        print("Jenis  :", "Wisata Budaya")
        print("Situs  :", self.__situs)
        print("Pemandu:", self.__bahasa_pemandu)