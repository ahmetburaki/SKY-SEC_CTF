# kir_beni - Reverse

flag: `SKYSEC{K4RT4LLAR_YUKSEKTEN_UC4R}`

# Writeup
## Korumanın Aşılması
Soru dnSpy üzerinde açıldığında ConfuserEx imzası görülebiliyor. AntiTamper var mı yok mu diye kontrol etmek için EntryPoint'e gidildiğinde decompiler'ın hata verdiği görülüyor. Module cctor kısmında bulunan 2. çağrıya breakpoint atılıp debugging başlatıldığında, Modules sekmesine gelen modül Memory'de açılır. Runtime'da denemeler yapabilmek için açılan modül üzerinde yine cctor noktasına gidip ilk çağrı noplanır ve dosya kaydedilir.

### Çözüm 1
Flag'in 32 karakter olduğunu ve xor işlemine sokulduğu tahmin edilebilir(*). Debug ederek xor edilmiş flag dizisine ulaştıktan sonra brute force atarak flag elde edilebilir.

### Çözüm 2
XOR işlemi yapılan Dynamic IL operasyonundan dolayı görülemeyebilir. Dynamic IL üretildiği sırada yüklenen IL Body yine debug edilerek(deobfuscate etme ile uğraşmadıysanız) elde edilebilir. Bunu disassemble ettiğimizde 0x22 değeri ile xor operasyonuna sokulup retlendiği görülür.

```csharp
 byte[] sQEtshExuA = {
	0x02, // ldarg.0
    0x1F, // ldc.i4.s
    0x22, // 0x22 (hex)
    0x61, // xor
    0x2A // ret
};
```
 
flag'i içeren byte dizisi debug edilerek alındıktan sonra içerisindeki her bir byte 0x22 ile xor işlemine sokularak flag elde edilir.