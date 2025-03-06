# ogrenci_kayit.py

def ogrenci_ekle():
    """Kullanıcıdan öğrenci isimleri alarak ogrenciler.txt dosyasına ekler"""
    with open("ogrenciler.txt", "a") as dosya:  # Dosyayı ekleme modunda aç
        while True:
            isim = input("Öğrenci adı girin ('bitti' yazınca durur): ")
            if isim.lower() == "bitti":  # Kullanıcı "bitti" yazarsa dur
                break
            dosya.write(isim + "\n")  # İsmi dosyaya kaydet

def ogrenci_listele():
    """ogrenciler.txt dosyasındaki tüm öğrencileri ekrana yazdırır"""
    try:
        with open("ogrenciler.txt", "r") as dosya:  # Dosyayı okuma modunda aç
            print("\nÖğrenci Listesi:")
            print(dosya.read())  # Tüm içeriği ekrana yazdır
    except FileNotFoundError:
        print("Henüz öğrenci kaydı yok!")  # Dosya yoksa uyarı ver

# Kullanımı
ogrenci_ekle()
ogrenci_listele()
