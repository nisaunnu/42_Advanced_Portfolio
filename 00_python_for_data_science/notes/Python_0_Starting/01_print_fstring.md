# print & f-string & for loop 

- [print()](#print)
    - [Virgül (`,`) ile Ayırarak Yazdırma](#1-virgül--ile-ayırarak-yazdırma)
    - [Artı (`+`) Operatörü ile Birleştirme (Concatenation)](#2-artı--operatörü-ile-birleştirme-concatenation)
    - [f-string ile Kısa Bir Karşılaştırma](#f-string-ile-kısa-bir-karşılaştırma)
- [f-string](#f-string)
    - [Temel Kullanım](#temel-kullanım)
    - [f-string'in Özellikleri ve Avantajları](#f-stringin-özellikleri-ve-avantajları)
        - [1. Matematiksel İşlemler](#1-matematiksel-işlemler)
        - [2. Fonksiyon Çağırma](#2-fonksiyon-çağırma)
        - [3. Sayı Biçimlendirme (Formatting)](#3-sayı-biçimlendirme-formatting)
        - [4. Hata Ayıklama (Debugging) Kolaylığı (Python 3.8+)](#4-hata-ayıklama-debugging-kolaylığı-python-38)
        - [5. Çok Satırlı (Multiline) f-string'ler](#5-çok-satırlı-multiline-f-stringler)
    - [Özet](#özet)
- [for döngüsü](#for-döngüsü)
    - [Temel Seviye: Koleksiyonlar Üzerinde Gezinmek](#temel-seviye-koleksiyonlar-üzerinde-gezinmek)
    - [Orta Seviye: Döngü Kontrolü ve Yardımcı Fonksiyonlar](#orta-seviye-döngü-kontrolü-ve-yardımcı-fonksiyonlar)
    - [İleri Seviye: Özel Yapılar ve Kısa Yazımlar](#ileri-seviye-özel-yapılar-ve-kısa-yazımlar)
    - [Uzman Seviye: Arka Planda Neler Oluyor? (Iterator Protokolü)](#uzman-seviye-arka-planda-neler-oluyor-iterator-protokolü)

<br></br>

## `print()` Fonksiyonu

Python'da değişkenleri ve metinleri ekrana yazdırmak için f-string kullanmadan önce sıkça başvurduğumuz "normal" `print()` yöntemleri şunlardır:
<br>

### 1. Virgül (`,`) ile Ayırarak Yazdırma

`print()` fonksiyonunun içine metinleri ve değişkenleri virgülle ayırarak yazabilirsiniz. Bu yöntemin en belirgin özelliği, virgül koyduğunuz her yere otomatik olarak bir **boşluk (space)** eklemesidir. Tip dönüşümü (örneğin sayıyı metne çevirmek) gerektirmez.

```python
isim = "Ahmet"
yas = 25

# Virgül ile kullanım
print("Benim adım", isim, "ve", yas, "yaşındayım.")

```

**Çıktı:**

> Benim adım Ahmet ve 25 yaşındayım.

*Not: Eğer aradaki otomatik boşlukları istemiyorsanız `sep=""` parametresini kullanmanız gerekir.*

<br>

### 2. Artı (`+`) Operatörü ile Birleştirme (Concatenation)

Metinleri uç uca eklemek için `+` operatörünü kullanabilirsiniz. Ancak bu yöntemin iki önemli kuralı vardır:

1. Otomatik boşluk bırakmaz; boşlukları sizin metin içine (örneğin `"ve "` şeklinde) eklemeniz gerekir.
2. Sadece string (metin) ifadeler birbiriyle toplanabilir. Eğer `yas` gibi bir tam sayıyı (integer) birleştirmek isterseniz, onu `str()` fonksiyonu ile metne çevirmek zorundasınız. Aksi takdirde Python hata verir.

```python
isim = "Ahmet"
yas = 25

# Artı (+) operatörü ile kullanım
# yas değişkenini str(yas) diyerek metne çevirmeliyiz
print("Benim adım " + isim + " ve " + str(yas) + " yaşındayım.")

```

**Çıktı:**

> Benim adım Ahmet ve 25 yaşındayım.

<br>

### f-string ile Kısa Bir Karşılaştırma

Yukarıdaki artı (`+`) operatörü örneğine baktığınızda, tırnakları açıp kapatmanın, boşlukları ayarlamanın ve `str()` kullanmanın ne kadar yorucu ve hata yapmaya açık olduğunu görebilirsiniz.

Aynı kodu f-string ile yazdığımızda kodun ne kadar sadeleştiğine tekrar bakalım:

```python
# Normal (+) yöntem:
print("Benim adım " + isim + " ve " + str(yas) + " yaşındayım.")

# f-string yöntemi:
print(f"Benim adım {isim} ve {yas} yaşındayım.")

```
<br></br>

## `f-string` Fonksiyonu

Python 3.6 ile birlikte hayatımıza giren **f-string** (formatted string literals), karakter dizilerini (string) biçimlendirmenin en modern, en okunaklı ve en hızlı yoludur. Kendinden önceki `%` operatörü veya `.format()` metoduna göre kullanımı çok daha basittir.
<br>

### Temel Kullanım

Bir string'in f-string olabilmesi için tırnak işaretinden hemen önce **`f`** veya **`F`** harfi koymanız yeterlidir. Değişkenleri veya ifadeleri string içine yerleştirmek için **süslü parantezler `{}**` kullanılır.

```python
isim = "Ahmet"
yas = 25

# Eski yöntem (.format)
# print("Benim adım {} ve {} yaşındayım.".format(isim, yas))

# f-string yöntemi
mesaj = f"Benim adım {isim} ve {yas} yaşındayım."
print(mesaj)

```

**Çıktı:**

> Benim adım Ahmet ve 25 yaşındayım.

<br>

### f-string'in Özellikleri ve Avantajları

#### 1. Matematiksel İşlemler

Süslü parantezlerin içinde doğrudan matematiksel ifadeler kullanabilirsiniz. Python bu işlemleri hesaplar ve sonucu string'e yazdırır.

```python
sayi1 = 10
sayi2 = 5

print(f"{sayi1} ile {sayi2}'nin toplamı {sayi1 + sayi2}'dir.")

```

**Çıktı:**

> 10 ile 5'in toplamı 15'tir.

<br>

#### 2. Fonksiyon Çağırma

Süslü parantezlerin içinde fonksiyonları veya metotları doğrudan çağırabilirsiniz.

```python
isim = "python"
print(f"Dilin adı: {isim.capitalize()}")

```

**Çıktı:**

> Dilin adı: Python

<br>

#### 3. Sayı Biçimlendirme (Formatting)

Ondalıklı sayıları yuvarlamak, sıfır eklemek veya binlik ayracı kullanmak f-string ile çok kolaydır. Değişkenden sonra `:` koyarak biçimlendirme kurallarını belirtebilirsiniz.

```python
pi_sayisi = 3.1415926535

# Virgülden sonra 2 basamak göstermek için: {:.2f}
print(f"Pi sayısının yaklaşık değeri: {pi_sayisi:.2f}")

para_birimi = 1500000
# Binlik ayracı olarak virgül kullanmak için: {:,}
print(f"Bakiye: {para_birimi:,} TL")

```

**Çıktı:**

> Pi sayısının yaklaşık değeri: 3.14
> Bakiye: 1,500,000 TL

<br>

#### 4. Hata Ayıklama (Debugging) Kolaylığı (Python 3.8+)

Python 3.8 ile birlikte f-string'lere harika bir özellik eklendi. Değişkenin adını ve değerini aynı anda yazdırmak için eşittir (`=`) işaretini kullanabilirsiniz. Bu, özellikle `print()` ile hata ayıklarken büyük zaman kazandırır.

```python
kullanici_adi = "admin"
giris_sayisi = 42

print(f"{kullanici_adi=}")
print(f"{giris_sayisi=}")

```

**Çıktı:**

> kullanici_adi='admin'
> giris_sayisi=42

<br>

#### 5. Çok Satırlı (Multiline) f-string'ler

Uzun metinler yazmak için üçlü tırnak (`"""`) ile birlikte f-string kullanabilirsiniz.

```python
isim = "Ayşe"
meslek = "Yazılım Geliştirici"

profil = f"""
Kullanıcı Profili
-----------------
İsim   : {isim}
Meslek : {meslek}
"""
print(profil)

```

<br>

### Özet

* **Okunabilirlik:** Kodun ne yaptığı ilk bakışta anlaşılır.
* **Hız:** Diğer string biçimlendirme yöntemlerinden (ör. `.format()`) çalışma zamanında (runtime) daha hızlıdır çünkü f-string'ler çalışma zamanında değerlendirilen ifadelerdir.
* **Pratiklik:** Süslü parantez içine doğrudan değişkenleri yazarak kod kalabalığından kurtulursunuz.

<br></br>

Python'daki `for` döngüsü, C veya Java gibi dillerdeki geleneksel "sayaç tabanlı" döngülerden oldukça farklıdır. Python'da `for`, bir **yineleyici (iterator)** olarak çalışır. Yani döngüye bir koleksiyon (liste, metin, sözlük vb.) verirsiniz ve o, arka planda indekslerle uğraşmanıza gerek kalmadan her bir elemanı sırayla size getirir.

İşte en temelden en ileri seviyeye Python'da `for` döngüsü:

---

## `for` döngüsü

### Temel Seviye: Koleksiyonlar Üzerinde Gezinmek

En temel kullanım, bir veri yapısının içindeki öğeleri tek tek alıp işlemektir.

#### 1. Listeler ve Karakter Dizileri (Strings)

Bir listenin veya metnin elemanları üzerinde doğrudan gezinebilirsiniz.

```python
meyveler = ["elma", "armut", "muz"]

for meyve in meyveler:
    print(meyve)

# Metinler de birer harf listesi gibi davranır
for harf in "Python":
    print(harf)

```

#### 2. `range()` Fonksiyonu ile Belirli Sayıda Dönmek

Sadece belirli bir sayı kadar işlem yapmak istiyorsanız `range()` fonksiyonu kurtarıcınızdır. `range(başlangıç, bitiş, adım)` şeklinde çalışır. Bitiş değeri dahil edilmez.

```python
# 0'dan 4'e kadar (4 dahil değil) yazdırır
for sayi in range(5):
    print(sayi)

# 2'den başlayıp 10'a kadar 2'şer atlayarak yazdırır
for cift_sayi in range(2, 11, 2):
    print(cift_sayi)

```

<br></br>

### Orta Seviye: Döngü Kontrolü ve Yardımcı Fonksiyonlar

Döngünün akışına müdahale etmek ve verileri daha akıllıca çekmek için bazı araçlara ihtiyaç duyarız.

#### 1. `break` ve `continue`

* **`break`**: Döngüyü anında tamamen sonlandırır.
* **`continue`**: Döngünün o anki turunu iptal eder ve bir sonraki elemana geçer.

```python
for sayi in range(1, 10):
    if sayi == 3:
        continue  # 3'ü atlar, yazdırmaz
    if sayi == 7:
        break     # 7'ye gelince döngüyü tamamen bitirir
    print(sayi)

```

#### 2. `enumerate()` ile İndeks Takibi

Elemanları alırken aynı zamanda o elemanın kaçıncı sırada (indekste) olduğunu bilmek istiyorsanız, manuel bir sayaç oluşturmak yerine `enumerate()` kullanmalısınız. Bu, Pythonik (Python felsefesine uygun) olan yöntemdir.

```python
diller = ["Python", "Java", "C++"]

for indeks, dil in enumerate(diller):
    print(f"{indeks}. indeksindeki dil: {dil}")

```

#### 3. `zip()` ile Çoklu Listelerde Gezinmek

İki veya daha fazla listeyi aynı anda, yan yana işlemek için `zip()` kullanılır. Listelerden en kısa olanı bitene kadar döngü devam eder.

```python
isimler = ["Ali", "Ayşe", "Veli"]
notlar = [85, 90, 78]

for isim, notu in zip(isimler, notlar):
    print(f"{isim} adlı öğrencinin notu: {notu}")

```

#### 4. Sözlükler (Dictionaries) Üzerinde Gezinmek

Sözlükler (Key-Value yapıları) üzerinde dönerken varsayılan olarak sadece anahtarlar (keys) gelir. Her ikisini de almak için `.items()` metodu kullanılır.

```python
kullanici = {"isim": "Ahmet", "yas": 30, "rol": "Admin"}

# Sadece anahtarlar veya değerler için .keys() veya .values() kullanılabilir
for anahtar, deger in kullanici.items():
    print(f"{anahtar}: {deger}")

```

<br></br>

### İleri Seviye: Özel Yapılar ve Kısa Yazımlar

#### 1. `for ... else` Yapısı

Python'a özgü, az bilinen ama çok güçlü bir yapıdır. Bir `for` döngüsünün sonuna `else` bloğu ekleyebilirsiniz. Bu `else` bloğu, **sadece ve sadece döngü doğal yollarla biterse** çalışır. Eğer döngü bir `break` ifadesi ile kesilirse, `else` bloğu atlanır. (Arama algoritmalarında "bulunamadı" durumunu yakalamak için harikadır).

```python
aranan_sayi = 5
sayilar = [1, 2, 3, 4]

for sayi in sayilar:
    if sayi == aranan_sayi:
        print("Sayı bulundu!")
        break
else:
    print("Döngü bitti ama sayı bulunamadı.")

```

#### 2. List Comprehensions (Tek Satırda `for`)

Bir `for` döngüsünü kullanarak yeni bir liste oluşturmanın en hızlı ve performanslı yoludur.

```python
# Klasik yöntem:
kareler = []
for x in range(5):
    kareler.append(x**2)

# List Comprehension yöntemi (İleri seviye):
kareler_pratik = [x**2 for x in range(5)]

```

<br></br>

### Uzman Seviye: Arka Planda Neler Oluyor? (Iterator Protokolü)

Python'da `for` döngüsünün sihirli bir şekilde çalışmasını sağlayan şey **Iterator Protokolü**'dür. Bir objenin `for` döngüsüne sokulabilmesi (iterable olması) için arka planda belirli dunder (double underscore) metotlarına sahip olması gerekir.

`for` döngüsü tetiklendiğinde Python arka planda şu adımları izler:

1. Verilen objenin `__iter__()` metodunu çağırarak ondan bir yineleyici (iterator) nesnesi alır.
2. Bu yineleyici nesnesinin üzerinden `__next__()` metodunu çağırarak elemanları tek tek çeker.
3. Eğer çekilecek eleman kalmazsa, obje gizlice bir `StopIteration` hatası fırlatır.
4. `for` döngüsü bu hatayı yakalar (size göstermez) ve döngüyü sonlandırır.

Yani yazdığınız basit bir `for` döngüsünün manuel ve arka plandaki tam karşılığı aslında şudur:

```python
liste = [10, 20, 30]
yineleyici = iter(liste) # Arka planda liste.__iter__() çağrılır

while True:
    try:
        eleman = next(yineleyici) # Arka planda yineleyici.__next__() çağrılır
        # ... döngünün içindeki işlemleriniz (örneğin print(eleman))
        print(eleman)
    except StopIteration:
        # Eleman bitince fırlatılan hata yakalanır ve döngü kırılır
        break

```
