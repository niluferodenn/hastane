import pandas as pd

from doktor import Doktor
from hasta import Hasta
from hemsire import Hemsire
from personel import Personel


def main():
    try:
        personeller = [
            Personel(12345, "Nilüfer", "Öden", "Ortopedi", 50000),
            Personel(12346, "Ali", "Yılmaz", "Ortodonti", 25000)
        ]

        for personel in personeller:
            print(personel)

        doktorlar = [
            Doktor(1, "Ahmet", "Öztürk", "Kardiyoloji", 10000, "Dahiliye ", 5, "ABC Hastanesi"),
            Doktor(2, "Ayşe", "Güven", "Kardiyoloji", 3000, "Dahiliye", 12, "DEF Hastanesi"),
            Doktor(3, "Mehmet", "Demir", "Nöroloji", 10500, "Kadın Doğum", 9, "İzmir Hastanesi")
        ]

        for doktor in doktorlar:
            print(doktor)

        hemsireler = [
            Hemsire(4, "Zeynep", "Kaya", "Dahiliye", 30000, 8, "Sertifika1", "ABC Hastanesi"),
            Hemsire(5, "Esra", "Güzel", "Psikoloji", 5000, 12, "Sertifika2", "DEF Hastanesi"),
            Hemsire(6, "Arzu", "Yıldırım", "Göz Hastalıkları", 45000, 8, "Sertifika3", "İzmir Hastanesi")
        ]

        for hemsire in hemsireler:
            print(hemsire)

        hastalar = [
            Hasta(987, "Didem", "Aslan", "22.09.1987", "Hastalık1", "Tedavi1"),
            Hasta(654, "Ahmet", "Fırat", "22.12.1991", "Hastalık2", "Tedavi2"),
            Hasta(321, "Özge", "Özbilen", "2.07.1975", "Hastalık13", "Tedavi3")
        ]

        for hasta in hastalar:
            print(hasta)

        veriler = []

        for personel in personeller:
            veriler.append({
                "personel_no": personel.get_personel_no(),
                "ad": personel.get_ad(),
                "soyad": personel.get_soyad(),
                "departman": personel.get_departman(),
                "maas": personel.get_maas(),
                "uzmanlik": None,
                "deneyim_yili": None,
                "hastane": None,
                "calisma_saati": None,
                "sertifika": None,
                "hasta_no": None,
                "dogum_tarihi": None,
                "hastalik": None,
                "tedavi": None
            })

        for doktor in doktorlar:
            veriler.append({
                "personel_no": doktor.get_personel_no(),
                "ad": doktor.get_ad(),
                "soyad": doktor.get_soyad(),
                "departman": doktor.get_departman(),
                "maas": doktor.get_maas(),
                "uzmanlik": doktor.get_uzmanlik(),
                "deneyim_yili": doktor.get_deneyim_yili(),
                "hastane": doktor.get_hastane(),
                "calisma_saati": None,
                "sertifika": None,
                "hasta_no": None,
                "dogum_tarihi": None,
                "hastalik": None,
                "tedavi": None
            })

        for hemsire in hemsireler:
            veriler.append({
                "personel_no": hemsire.get_personel_no(),
                "ad": hemsire.get_ad(),
                "soyad": hemsire.get_soyad(),
                "departman": hemsire.get_departman(),
                "maas": hemsire.get_maas(),
                "uzmanlik": None,
                "deneyim_yili": None,
                "hastane": hemsire.get_hastane(),
                "calisma_saati": hemsire.get_calisma_saati(),
                "sertifika": hemsire.get_sertifika(),
                "hasta_no": None,
                "dogum_tarihi": None,
                "hastalik": None,
                "tedavi": None
            })

        for hasta in hastalar:
            veriler.append({
                "personel_no": None,
                "ad": hasta.get_ad(),
                "soyad": hasta.get_soyad(),
                "departman": None,
                "maas": None,
                "uzmanlik": None,
                "deneyim_yili": None,
                "hastane": None,
                "calisma_saati": None,
                "sertifika": None,
                "hasta_no": hasta.get_hasta_no(),
                "dogum_tarihi": hasta.get_dogum_tarihi(),
                "hastalik": hasta.get_hastalik(),
                "tedavi": hasta.get_tedavi()
            })

        df = pd.DataFrame(veriler)
        print(df)

        df.fillna(0, inplace=True)

        uzmanligina_gore_doktor_sayilari = df[df["uzmanlik"] != 0].groupby("uzmanlik").size()
        print("Uzmanlık Alanlarına Göre Doktor Sayıları:\n", uzmanligina_gore_doktor_sayilari)

        deneyimli_doktor_sayisi = df[(df["deneyim_yili"] > 5) & (df["deneyim_yili"] != 0)].shape[0]
        print("5 Yıldan Fazla Deneyime Sahip Doktor Sayısı:", deneyimli_doktor_sayisi)

        hasta_adina_gore_sirali_dataframe = df[df["hasta_no"] != 0].sort_values(by="ad")
        print("Hasta Adına Göre Sıralanmış DataFrame:\n", hasta_adina_gore_sirali_dataframe)

        maasi_7000_uzeri = df[df["maas"] > 7000]
        print("Maaşı 7000 TL Üzerinde Olan Personeller:\n", maasi_7000_uzeri)

        df["dogum_tarihi"] = pd.to_datetime(df["dogum_tarihi"], errors='coerce')
        dogum_1990_sonrasi = df[
            (df["dogum_tarihi"] >= pd.Timestamp("1990-01-01")) & (df["dogum_tarihi"] != pd.Timestamp(0))]
        print("1990 ve Sonrası Doğumlu Hastalar:\n", dogum_1990_sonrasi)

        yeni_df = df[["ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastalik", "tedavi"]]
        print("Yeni DataFrame:\n", yeni_df)

    except Exception as ex:
        print("İşlemler sırasında hata oluştu: {}", format(ex))


if __name__ == "__main__":
    main()
