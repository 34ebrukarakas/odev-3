# telefon_rehberi.py

def rehber_ekle():
    """Kullanıcıdan ad ve telefon numarası alıp rehbere ekler"""
    with open("rehber.txt", "a") as dosya:
        ad = input("Ad: ")
        telefon = input("Telefon: ")
        dosya.write(f"{ad}:{telefon}\n")  # Ad ve numarayı dosyaya ekle

def rehber_ara():
    """Girilen isme ait telefon numarasını rehberden bulur"""
    isim = input("Aranacak isim: ")
    try:
        with open("rehber.txt", "r") as dosya:
            for satir in dosya:
                kayit = satir.strip().split(":")  # Ad ve numarayı ayır
                if kayit[0].lower() == isim.lower():
                    print(f"{kayit[0]}: {kayit[1]}")
                    return
        print("Kayıt bulunamadı.")
    except FileNotFoundError:
        print("Rehberde hiç kayıt yok.")  # Dosya yoksa uyarı ver

def rehber_listele():
    """Tüm rehber kayıtlarını ekrana yazdırır"""
    try:
        with open("rehber.txt", "r") as dosya:
            print("\nTelefon Rehberi:")
            print(dosya.read())  # Tüm rehberi yazdır
    except FileNotFoundError:
        print("Rehber boş!")  # Dosya yoksa uyarı ver

# Kullanım
komut = input("Komut girin ('ekle', 'ara', 'listele'): ")
if komut == "ekle":
    rehber_ekle()
elif komut == "ara":
    rehber_ara()
elif komut == "listele":
    rehber_listele()
