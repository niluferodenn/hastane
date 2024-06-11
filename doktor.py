from personel import Personel


class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def get_uzmanlik(self):
        return self.__uzmanlik

    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def get_hastane(self):
        return self.__hastane

    def set_hastane(self, hastane):
        self.__hastane = hastane

    def __str__(self):
        return f"{super().__str__()}, Uzmanlık: {self.__uzmanlik}, Deneyim Yılı: {self.__deneyim_yili}, Hastane: {self.__hastane}"

    def maas_arttir(self, oran):
        self.set_maas(self.get_maas() + (self.get_maas() * (oran / 100)))