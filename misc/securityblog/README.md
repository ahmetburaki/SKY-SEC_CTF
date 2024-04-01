# Security Blog - MISC

flag: `SKYSEC{4sla_y0rulm4zl4r}`

# Writeup
## Dosyayı İnceleme

Sorudaki .html uzantılı dosyayı açınca bizi sadece *"Blog kısa süreliğine kapanmıştır"* ve *"Destek olmak için Sepolia'dan 0xD6742Fb5aB9CE90E661D70e3Fd2eb26C8e2eB0e9 adresine bağış yapabilirsiniz."* yazısı karşımıza çıkıyor. Bu durumda söz konusu adresi inceliyoruz.

## Blockchain Adresini İnceleme

Bu işlem için bir blockchain explorer kullanmamız gerekmekte. Ben etherscan.io sitesini kullandım. Sepolia testnet için araştırmamı sepolia.etherscan.io üzerinden yaptım.
Dosyadaki adresi etherscan üzerinde arattığımda birçok işlem görüyorum ve site üzerinde bu işlemlerin birçoğunun veri içerdiği söyleniyor.
Veri ile birlikte belli miktar ETH içeren işlemler başta olmak üzere işlemleri inceliyorum.

### Veriyi Okuma

İlgili transferin TxHash'i ile transferin detaylarına bakıyoruz. Transfer detaylarında veriyi hex formatında görebiliyoruz. Bu veriyi bir çevirici yardımıyla UTF-8 formatına çeviriyoruz (ya da etherscan'in kendi çeviricisi kullanılabilir.).

## Flag'i Elde Etme

Verileri okuduğumuzda ilgili flag'i {} işaretleri arasında yazılmış olarak buluyoruz.

Flag formatına uygun olarak düzenlendikten sonra flag'i elde ediyoruz.