# RockPaperScissors

# Taş, Kağıt, Makas Oyunu

Bu Python uygulaması, klasik "Taş, Kağıt, Makas" oyununu oynayabileceğiniz bir komut satırı programıdır. Oyuncu, bilgisayara karşı oynar ve ilk iki turu kazanan oyunu kazanır.

## Özellikler

- **Zorluk Seviyeleri:** Kolay, Orta, Zor
  - **Kolay:** Bilgisayar tamamen rastgele bir seçim yapar.
  - **Orta:** Bilgisayar, oyuncunun bir önceki seçimine göre karar verebilir.
  - **Zor:** Bilgisayar, oyuncunun son iki seçimini analiz ederek tahminde bulunabilir.
  
- **Oyun Süreci:** Oyuncu ve bilgisayar karşılıklı olarak seçim yapar. İlk iki turu kazanan oyuncu, o oyunu kazanmış sayılır.

- **Çıkış Seçeneği:** Oyuncu herhangi bir turda "çıkış" yazarak oyunu sonlandırabilir.

## Kullanım

1. **Oyunu Başlatma:**
    ```python
    tas_kagit_makas_ORCUN_TURKOKULOGLU()
    ```

2. **Zorluk Seviyesini Seçin:** Oyuna başladığınızda, kolay, orta veya zor zorluk seviyesini seçmeniz istenir.

3. **Seçim Yapın:** Oyuncu, "taş", "kağıt" veya "makas" seçeneklerinden birini girer. Oyundan çıkmak için "çıkış" yazabilirsiniz.

4. **Oyun Süreci:** Her turun galibi belirlenir ve ilk iki turu kazanan oyuncu oyunu kazanır. Bir oyunun sonunda, yeni bir oyun oynamak isteyip istemediğiniz sorulur.

## Kurallar

- **Taş, makası yener.**
- **Makas, kağıdı yener.**
- **Kağıt, taşı yener.**
- **İlk iki turu kazanan oyunu kazanır.**

## Oyun Akışı

1. Oyuna başladığınızda, zorluk seviyesini seçmeniz istenir.
2. Seçiminizi yaptıktan sonra bilgisayarın seçimi belirlenir ve sonuç değerlendirilir.
3. İki tur galibiyetine ulaşan ilk taraf oyunu kazanır.
4. Bir oyunun sonunda, tekrar oynamak isteyip istemediğiniz sorulur.
   - **Evet:** Yeni bir oyun başlar.
   - **Hayır:** Oyun sona erer ve toplam sonuçlar görüntülenir.

## Örnek Kullanım

Taş, Kağıt, Makas Oyununa Hoş Geldiniz!

Kurallar: Taş makası yener, makas kağıdı yener, kağıt ise taşı yener.

İlk iki turu kazanan oyunu kazanır. Oyundan çıkmak için 'çıkış' yazabilirsiniz.

Zorluk seviyesini seçin (kolay/orta/zor): zor

1. Oyun başlıyor!
   
Taş, Kağıt, Makas? (Çıkmak için 'çıkış'): taş

Bilgisayarın seçimi: kağıt

Bilgisayar 1. turu kazandı!

Taş, Kağıt, Makas? (Çıkmak için 'çıkış'): makas

Bilgisayarın seçimi: taş

Bilgisayar 2. turu kazandı!

Bilgisayar 1. oyunu kazandı!

Toplam Skor: 1 - Oyuncu: 0, Bilgisayar: 1

Başka bir oyun oynamak ister misiniz? (evet/hayır): hayır

Oyun bitti, teşekkürler!

Toplam Oyunlar: 1, Oyuncu Galibiyetleri: 0, Bilgisayar Galibiyetleri: 1


## Gereksinimler

Bu program, Python 3.x sürümü ile çalışır.

## Geliştirici

Orçun Türkokuloğlu

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.


Bu README.md dosyası, programın özelliklerini, kurallarını, nasıl kullanılacağını ve örnek bir oyun akışını açıkça tanımlar. Ayrıca, gerekli olan yazılım ve geliştirici bilgilerini de içerir.
