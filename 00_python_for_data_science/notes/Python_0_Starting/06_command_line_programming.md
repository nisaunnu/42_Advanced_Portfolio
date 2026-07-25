# Python - 0 - Starting Not İçeriği

- [Komut Satırı Argümanları ve `sys.argv` Mekanizması](#komut-satırı-argümanları-ve-sysargv-mekanizması)
    - [`sys.argv` Yapısının Anatomisi](#sysargv-yapısının-anatomisi)
    - [Argüman Sayısının Denetlenmesi](#argüman-sayısının-denetlenmesi)
- [Girdi Doğrulama (Data Validation) ve `try-except` Akışı](#girdi-doğrulama-data-validation-ve-try-except-akışı)
- [`AssertionError` Fırlatma ve Savunma Odaklı Programlama](#assertionerror-fırlatma-ve-savunma-odaklı-programlama)

<br></br>

## Komut Satırı Argümanları ve `sys.argv` Mekanizması

Bir programı terminalde çalıştırırken yanına yazdığımız her kelime, işletim sistemi tarafından programa birer **argüman (parametre)** olarak aktarılır. Python bu argümanları yönetmek için yerleşik `sys` modülünün altındaki `argv` nesnesini kullanır.

`sys.argv` (Argument Vector), temel olarak bir **String Listesidir (`list[str]`)**. Terminale girilen komut dizisindeki her boşluk, bu listenin yeni bir elemanı tetiklemesine yol açar.

<br>

### `sys.argv` Yapısının Anatomisi

Diyelim ki terminalde şu komutu çalıştırdık:
`$ python whatis.py 13 5`

Python arka planda `sys.argv` listesini şu şekilde doldurur:

* `sys.argv[0]` $\rightarrow$ `"whatis.py"` (Her zaman çalıştırılan dosyanın adıdır)
* `sys.argv[1]` $\rightarrow$ `"13"` (Kullanıcının gönderdiği ilk argüman)
* `sys.argv[2]` $\rightarrow$ `"5"` (Kullanıcının gönderdiği ikinci argüman)

<br>

### Argüman Sayısının Denetlenmesi

Programın kararlı çalışabilmesi için listenin uzunluğunu (`len(sys.argv)`) kontrol etmek hayati önem taşır:

* `len(sys.argv) == 1`: Kullanıcı hiçbir parametre vermemiştir (Sadece dosya adı var).
* `len(sys.argv) == 2`: Kullanıcı tam olarak 1 adet parametre girmiştir (İstenen durum).
* `len(sys.argv) > 2`: Kullanıcı birden fazla parametre girerek sınırı aşmıştır.

<br></br>

## Girdi Doğrulama (Data Validation) ve `try-except` Akışı

İşletim sistemi sınırından (Terminal) Python'a giren **tüm veriler istisnasız birer String (`str`) nesnesidir.** Kullanıcı terminale `14` yazsa bile Python bunu sayısal bir değer olarak değil, `"14"` metni olarak teslim alır.

Matematiksel bir kontrol (tek/çift sorgusu) yapabilmek için bu metni `int()` fonksiyonu ile tam sayıya dönüştürmemiz (type casting) gerekir. Ancak bu dönüşüm potansiyel bir risk taşır:

* `int("14")` $\rightarrow$ `14` (Başarılı)
* `int("Hi!")` $\rightarrow$ `ValueError` (Hata ve Programın Çökmesi)

Profesyonel bir yazılımın kullanıcı hatalı girdi verdiğinde çökmemesi, bunun yerine hatayı yakalayıp kullanıcıya anlamlı bir mesaj göstermesi gerekir. Bu süreç **Hata Yakalama (Exception Handling)** blokları ile yönetilir.

```python
# Matematiksel Dönüşüm Güvenlik Çemberi
girdi = "Hi!"
try:
    # Python önce bu bloğun içindeki kodu çalıştırmayı dener
    sayi = int(girdi)
except ValueError:
    # Eğer yukarıdaki satırda "ValueError" patlarsa, program çökmez
    # Akış anında buraya kayar ve bu blok çalışır
    print("Dönüşüm başarısız: Girdi bir tam sayı değil!")

```

<br></br>