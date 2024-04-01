# Touravel - Mobile

flag: `SKYSEC{h4m4m1_t3m1z_kull4n1n}`

# Writeup
## Uygulamaya Göz Atma

touravel.apk dosyasını ortama kurduğumuzda bizi belirli şehirlerdeki gezilecek yerleri tanıtan bir uygulama karşılıyor.
Uygulama içerisinde biraz gezildikten sonra İstanbul'daki yerlerden **Tarihi Hamam** hakkında bilgi bulunmadığını ve fotoğrafın gösterilemediğini fark ediyoruz.

## Dosya Analizi

.apk dosyasını analiz ettiğimizde *Tarihi Hamam* sayfasında fotoğraf gösterilmemesine rağmen **assets\flutter_assets\images** dizininde **tarihihamam.png** dosyası bizi karşılıyor. Ama bu dosya açıldığında fotoğraf gösterilemiyor.
Bu dosyayı herhangi bir hex düzenleyicisinde incelediğimizde bu dosya .png uzantılı bir dosya olduğu için, header'ı onaltılık sistemde `89 50 4E 47 0D 0A 1A 0A` olması gerekirken `89 50 4E 47 33 31 1A 0A` olduğunu fark ediyoruz. 
Header'ları düzenledikten sonra .png dosyası gerektiği gibi açılıyor.

## Flag Elde Etme

"tarihihamam.png" dosyasını açtıktan sonra herhangi bir steganografi methodu kullanmamıza gerek kalmadan bir QR koda ulaşıyoruz.
Bu QR kodunu basit haliyle çoğu QR kod okuyucu okuyamadığı için Photoshop veya GIMP benzeri bir uygulamadan arka planı daha kolay temizlemek için renk düzeylerini ayarlıyoruz. Gölgeleri ve açık tonları histogramın sağ tarafında birbirine yaklaştırdıktan sonra arka planı daha rahat bir şekilde beyaza boyayabiliyoruz.

*Alternatif olarak QR kodu siz de tekrardan pixel art şeklinde çizebilirsiniz.*

En son aşamadaki QR kodu okutunca flag'i elde etmiş oluyorsunuz.