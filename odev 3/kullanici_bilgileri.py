
import json  # JSON işlemleri için gerekli

def kullanici_ekle():
    """Kullanıcıdan ad, soyad, yaş bilgilerini alarak JSON dosyasına kaydeder"""
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")
    yas = input("Yaşınız: ")

    yeni_kullanici = {"ad": ad, "soyad": soyad, "yas": yas}  # Kullanıcı bilgilerini sözlük olarak sakla

    try:
        with open("kullanicilar.json", "r") as dosya:
            kullanicilar = json.load(dosya)  # Mevcut kullanıcıları yükle
    except (FileNotFoundError, json.JSONDecodeError):
        kullanicilar = []  # Dosya yoksa boş liste oluştur

    kullanicilar.append(yeni_kullanici)  # Yeni kullanıcıyı listeye ekle

    with open("kullanicilar.json", "w") as dosya:
        json.dump(kullanicilar, dosya, indent=4)  # JSON dosyasına kaydet

def kullanici_listele():
    """JSON dosyasındaki tüm kullanıcıları ekrana yazdırır"""
    try:
        with open("kullanicilar.json", "r") as dosya:
            kullanicilar = json.load(dosya)  # JSON dosyasını yükle
            for kisi in kullanicilar:
                print(f"{kisi['ad']} {kisi['soyad']} - {kisi['yas']} yaşında")
    except FileNotFoundError:
        print("Henüz kullanıcı eklenmemiş!")  # Dosya yoksa uyarı ver

# Kullanım
komut = input("Komut girin ('ekle' veya 'listele'): ")
if komut == "ekle":
    kullanici_ekle()
elif komut == "listele":
    kullanici_listele()
