# E-Shop - Web

flag: `SKYSEC{$qL1_1$_n07_h4Rd_4c7U4LlY}`

# Writeup
![](https://i.hizliresim.com/bljodap.png)
Web sitesinde çalışan iki adet fonksiyon var. Birisi kayıt olup giriş yapabileceğiniz `accounts`, ikincisi ise ürünleri listeleyebileceğimiz `shop` kısmı. `accounts` uygulaması herhangi bir açık barındırmamakta bu yüzden `shop` kısmından ilerlenmeli.

![](https://i.hizliresim.com/tk67fyq.png)
![](https://i.hizliresim.com/k36suvb.png)
`shop` kısmı incelendiğinde yine çalışan tek bir kısım var, `sıralama ölçütleri`.

![](https://i.hizliresim.com/o971998.png)
URL'deki `year` parametresi `Django`daki `SQL` fonksiyonuna direkt olarak gönderildiği için zafiyet barındırmakta. İlgili [Django Güvenlik güncellemesi](https://docs.djangoproject.com/en/5.0/releases/security/#july-4-2022-cve-2022-34265) `CVE-2022-34265`  `Django`nun `ORM`i içerisinde bulunan `annotate` fonksiyonunda kullanıcak olan `Extract` objesine kullanıcıların argüman verebilme yetkisi üzerinden `SQLi` zafiyetini kapsamakta. 

Zafiyetin oluşmasındaki ana etmen olan `Extarct` objesi `from django.db.models.functions import Extract
` adresinden ulaşılabilir. Kullanım örneği; ` Model.objects.annotate(year_field=Extract("date",**KULLANICI_GİRDİSİ**))`.

Zafiyetli kod örneğinin `ORM` aracılığyla sunucuda çalıştırdığı `SQL` sorgusu; `SELECT "app_model"."id", "app_model"."**date**", "app_model"."field1", "app_model"."field2", "app_model"."field3", "app_model"."field4", "app_model"."field5", django_date_extract('**KULLANICI_GİRDİSİ**', "app_model"."date") AS "year_field  
" FROM "app_model"`. Sorgudan da anlaşılabileceği üzere zafiyetin tetiklenebilmesi için arka uçtaki `Django` modelinde `DatetimeField` kullanılması gerekli.

![](https://i.hizliresim.com/jyxt534.png)
![](https://i.hizliresim.com/gvohjlb.png)
![](https://i.hizliresim.com/26gq5bi.png)
Bayrağın sorgusunun yazılacağı bölümün bulunması için öncelikle tek tek `null` değerler test edilir ve ardından hatalı sonuç alınmayana kadar `null` değerler rastgele `int` değerle değiştirilir, böylelikle arka uçta herhangi bir hatanın önüne geçilmiş olur. Kalan `null` değerleri de `(SELECT flag FROM flag LIMIT 1)` sorgusu test ederek doldurduğumuzda ürün listesi yeni ürün eklenecek ve bu ürünün isminde bayrağı görmüş olacağız.
