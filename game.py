import random

def tas_kagit_makas_ORCUN_TURKOKULOGLU():
    print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz!")
    print("Kurallar: Taş makası yener, makas kağıdı yener, kağıt ise taşı yener.")
    print("İlk iki turu kazanan oyunu kazanır. Oyundan çıkmak için 'çıkış' yazabilirsiniz.")
    
    secenekler = ["taş", "kağıt", "makas"]
    oyun_sayisi = 0
    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0
    oyuncu_secim_tarihi = []
    
    while True:
        zorluk = input("Zorluk seviyesini seçin (kolay/orta/zor): ").lower()
        while zorluk not in ['kolay', 'orta', 'zor']:
            zorluk = input("Geçersiz seçim. Lütfen zorluk seviyesini seçin (kolay/orta/zor): ").lower()
        
        oyun_sayisi += 1
        tur_sayisi = 0
        oyuncu_tur_galibiyetleri = 0
        bilgisayar_tur_galibiyetleri = 0
        
        print(f"\n{oyun_sayisi}. Oyun başlıyor!")
        
        while oyuncu_tur_galibiyetleri < 2 and bilgisayar_tur_galibiyetleri < 2:
            oyuncu_secimi = input("Taş, Kağıt, Makas? (Çıkmak için 'çıkış'): ").lower()
            if oyuncu_secimi == 'çıkış':
                print("Oyundan çıktınız. Teşekkürler!")
                return

            if oyuncu_secimi not in secenekler:
                print("Geçersiz seçim, lütfen tekrar deneyin.")
                continue
            
            oyuncu_secim_tarihi.append(oyuncu_secimi)
            
            if zorluk == 'kolay':
                bilgisayar_secimi = random.choice(secenekler)
            elif zorluk == 'orta':
                if len(oyuncu_secim_tarihi) > 1 and random.choice([True, False]):
                    if oyuncu_secim_tarihi[-1] == "taş":
                        bilgisayar_secimi = "kağıt"
                    elif oyuncu_secim_tarihi[-1] == "kağıt":
                        bilgisayar_secimi = "makas"
                    else:
                        bilgisayar_secimi = "taş"
                else:
                    bilgisayar_secimi = random.choice(secenekler)
            elif zorluk == 'zor':
                if len(oyuncu_secim_tarihi) > 2:
                    son_iki_secim = oyuncu_secim_tarihi[-2:]
                    if son_iki_secim.count("taş") > 1:
                        bilgisayar_secimi = "kağıt"
                    elif son_iki_secim.count("kağıt") > 1:
                        bilgisayar_secimi = "makas"
                    elif son_iki_secim.count("makas") > 1:
                        bilgisayar_secimi = "taş"
                    else:
                        bilgisayar_secimi = random.choice(secenekler)
                else:
                    bilgisayar_secimi = random.choice(secenekler)
            
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (
                (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or
                (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or
                (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt")
            ):
                oyuncu_tur_galibiyetleri += 1
                print(f"{oyuncu_tur_galibiyetleri}. turu kazandınız!")
            else:
                bilgisayar_tur_galibiyetleri += 1
                print(f"Bilgisayar {bilgisayar_tur_galibiyetleri}. turu kazandı!")

            tur_sayisi += 1

        if oyuncu_tur_galibiyetleri == 2:
            print(f"\nTebrikler! {oyun_sayisi}. oyunu kazandınız!")
            oyuncu_galibiyetleri += 1
        else:
            print(f"\nBilgisayar {oyun_sayisi}. oyunu kazandı!")
            bilgisayar_galibiyetleri += 1

        print(f"Toplam Skor: {oyun_sayisi} - Oyuncu: {oyuncu_galibiyetleri}, Bilgisayar: {bilgisayar_galibiyetleri}")
        
        while True:
            devam_mi = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
    
            if devam_mi == 'evet':
                if random.choice([True, False]):
                    print("Bilgisayar da oynamak istiyor!")
                    break  # Yeni oyuna başlamak için dış döngüye döner
                else:
                    print("Bilgisayar oyundan çıkmak istedi. Oyun bitti!")
                    print(f"Toplam Oyunlar: {oyun_sayisi}, Oyuncu Galibiyetleri: {oyuncu_galibiyetleri}, Bilgisayar Galibiyetleri: {bilgisayar_galibiyetleri}")
                    return
            elif devam_mi == 'hayır':
                print("Oyun bitti, teşekkürler!")
                print(f"Toplam Oyunlar: {oyun_sayisi}, Oyuncu Galibiyetleri: {oyuncu_galibiyetleri}, Bilgisayar Galibiyetleri: {bilgisayar_galibiyetleri}")
                return
            else:
                print("Yanlış yazdınız, lütfen tekrar giriniz!")


# Oyunu başlatmak için fonksiyonu çağırın
tas_kagit_makas_ORCUN_TURKOKULOGLU()
