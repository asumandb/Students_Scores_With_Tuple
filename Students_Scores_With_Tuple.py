ogrenci_notlari = (
    ("Ahmet": {"Matematik": 75, "Fizik": 85}),
    ("Zeynep": {"Matematik": 92, "Fizik": 78}), 
    ("Mehmet": {"Matematik": 65, "Fizik": 90})
)

guncellenmis_ogrenci_notlari = []

for isim, notlar in ogrenci_notlari:
    if notlar["Matematik"] < 70:
        yeni_notlar= {"Matematik": notlar["Matematik"] + 10, "Fizik": notlar["Fizik"]}

    else:
        yeni_notlar = notlar

    guncellenmis_ogrenci_notlari.append((isim, yeni_notlar))


ogrenci_notlari = tuple(guncellenmis_ogrenci_notlari)

print(ogrenci_notlari)
