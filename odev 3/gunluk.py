# gunluk.py
import os  # Dosya işlemleri için gerekli

def gunluk():
    """Kullanıcının notlarını kaydeder, görüntüler veya siler"""
    while True:
        giris = input("Notunuzu girin ('goruntule' ile bak, 'sil' ile sil, 'cikis' ile çık): ")

        if giris.lower() == "goruntule":  # Notları ekrana yazdır
            try:
                with open("gunluk.txt", "r") as dosya:
                    print("\nGünlük Notları:")
                    print(dosya.read())  # Dosya içeriğini göster
            except FileNotFoundError:
                print("Henüz not eklenmemiş!")

        elif giris.lower() == "sil":  # Günlük dosyasını sil
            try:
                os.remove("gunluk.txt")  # Dosyayı kaldır
                print("Günlük silindi!")
            except FileNotFoundError:
                print("Silinecek günlük yok!")

        elif giris.lower() == "cikis":  # Programdan çık
            break

        else:
            with open("gunluk.txt", "a") as dosya:
                dosya.write(giris + "\n")  # Notu dosyaya ekle
                print("Not kaydedildi.")

# Kullanımı
gunluk()
