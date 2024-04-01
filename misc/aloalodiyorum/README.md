# aloalodiyorum - MISC

flag: `SKYSEC{Baumeisterstraße}`

# Writeup
# Giriş

Bu yazı YTÜ SKYLAB kulübünün düzenlediği SKYDAYS etkinliğindeki CTF yarışmasındaki sorunun çözümünü anlatmaktadır. Sorunun tek çözümü bu değildir, başka çözümler olabilmektedir.

# Soru

![1.jpeg](SKYDAYS%20CTF%20MISC-01%20fbbe09aca3f743e4aecb4afb0ddaa496/1.jpeg)

 Arkadaşım bana telefonunu kaybettiğini ve telefonun şarjı bittiği için telefonunu bulamadığını söyledi. Kendisinin bulut depolamasına baktığımızda en son çekilen fotoğrafın bu olduğunu gördük. Arkadaşımın telefonunu bulmasına yardım eder misin? (Bayrak şu şekildedir: SKYSEC{fotoğraftaki benzin istasyonunun bulunduğu sokağın adı})

# Çözüm

 Fotoğrafı inceleyelim ve bu fotoğrafın nereden çekildiğini bulmamız için ipucu toplayalım:

![Untitled](SKYDAYS%20CTF%20MISC-01%20fbbe09aca3f743e4aecb4afb0ddaa496/Untitled.png)

1. Camda indirim afinişi görüyoruz ve bu afiş “kik” adındaki mağazaya aitmiş.
2. Bir benzin istasyonunun yakınında çekilmiş fotoğrafımız.
3. Benzin istasyonunun renklerini ve desenini görüyoruz.
4. “DHL” markasının kargomatı tarzı bir dolap görüyoruz.
5. Plaka sansürlenmiş fakat başını rahatça okuyabiliyoruz: DN, mavi kuşağın üzerinde ise D yazıyor.

 Bu bilgileri bir araya getirip aramaya başlayalım:

 Plakanın mavi kısmında ‘D’ harfinin olması alman plakası olduğu anlamına geliyor. ‘DN’ kısmını aratırsak ise plakanın ‘Düren’ kayıtlı olduğunu görüyoruz:

![Untitled](SKYDAYS%20CTF%20MISC-01%20fbbe09aca3f743e4aecb4afb0ddaa496/Untitled%201.png)

 1 numaralı ipucundaki “kik” yazısını internette arattığımızda markanın bir alman giyim mağazası olduğunu görüyoruz. Bu iki ipucu fotoğrafın Almanya’da olabileceğini kuvvetlendiriyor.

 Almanya’daki benzin istasyonlarının fotoğraflarına internetten bakalım:

![Untitled.jpg](SKYDAYS%20CTF%20MISC-01%20fbbe09aca3f743e4aecb4afb0ddaa496/Untitled.jpg)

 Burada bir fotoğraf dikkatimizi çekiyor, bize verilen fotoğraftakine çok benzer renk ve desene sahip benzin istasyonunu görüyoruz. Markanın adının “star” olduğunu öğreniyoruz. Almanya-Düren’deki “star” benzin istasyonlarını “Google Earth”de aratalım:

![temp.jpg](SKYDAYS%20CTF%20MISC-01%20fbbe09aca3f743e4aecb4afb0ddaa496/temp.jpg)

 Bu istasyonlara baktığımızda fotoğraftakine benzer bir yeri göremiyoruz. Düren yerine tüm Almanya’yı aratalım:

![temp.jpg](SKYDAYS%20CTF%20MISC-01%20fbbe09aca3f743e4aecb4afb0ddaa496/temp%201.jpg)

 Karşımıza çıkan istasyonların resimlerine göz attığımızda işaretli yerdeki istasyonun fotoğrafa benzediğini görüyoruz. Yakından bakalım:

![temp.jpg](SKYDAYS%20CTF%20MISC-01%20fbbe09aca3f743e4aecb4afb0ddaa496/temp%202.jpg)

 Sokak görüntüsüne geçtiğimizde istasyonun ve çevresinin bize verilen fotoğrafla uyuştuğunu görüyoruz. Konumu bulduk, bayrak için istasyonun adresine ihtiyacımız var:

![Untitled.jpg](SKYDAYS%20CTF%20MISC-01%20fbbe09aca3f743e4aecb4afb0ddaa496/Untitled%201.jpg)

 Böylelikle bayrağımızı bulmuş olduk: SKYSEC{Baumeisterstraße}.