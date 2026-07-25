# Functions & print & type & if/elif/else

- [Fonksiyon Nasıl Yazılır? (`def` Anahtar Kelimesi)](#fonksiyon-nasıl-yazılır-def-anahtar-kelimesi)
- [print() ve return Arasındaki Hayati Fark](#print-ve-return-arasındaki-hayati-fark)
- [Nesnelerin Tipini Bulmak: type()](#nesnelerin-tipini-bulmak-type)
- [Akış Kontrolü: Hangi Tipe Hangi Mesaj? (if / elif / else)](#akış-kontrolü-hangi-tipe-hangi-mesaj-if--elif--else)
- [Python'da `==` ve `is` Operatörleri Arasındaki Fark](#not-pythonda--ve-is-operatörleri-arasındaki-fark)
- [Lambda Fonksiyonları](#lambda-fonksiyonları)
    - [Temel Sözdizimi (Syntax)](#-temel-sözdizimi-syntax)
    - [Lambda'nın Gerçek Gücü: Yüksek Mertebeden Fonksiyonlar](#lambda'nın-gerçek-gücü-yüksek-mertebeden-fonksiyonlar)
    - [İleri Seviye: Lambda'nın Sınırları ve PEP 8 Standartları](#ileri-seviye-lambda'nın-sınırları-ve-pep-8-standartları)

<br></br>

## Fonksiyon Nasıl Yazılır? (`def` Anahtar Kelimesi)

Python'da bir fonksiyon tanımlamak (define) için `def` anahtar kelimesi kullanılır. Temel anatomi şudur:

```python
def fonksiyon_ismi(parametreler):
    # Yapılacak işlemler
    # Kod blokları...
```

### Parametre (Argüman) Nedir?

Fonksiyonlar dışarıdan veri alıp o veri üzerinde işlem yapabilirler. Parantez içine yazdığımız değişkenlere parametre denir.

Egzersizdeki prototipi inceleyelim:
`def all_thing_is_obj(object: any) -> int:`

Burada **Type Hinting (Tip İpucu)** kullanılmış. Bu, kodun çalışmasını etkilemez ama kodu okuyan yazılımcıya (veya editöre) rehberlik eder:

* `object: any` -> Bu fonksiyon `object` adında bir parametre alacak ve bu parametrenin veri tipi `any` (yani liste, string, sayı vb. **herhangi bir şey**) olabilir.
* `-> int:` -> Bu fonksiyon görevini bitirdiğinde bana bir **tam sayı (integer)** döndürecek (`return` edecek) demektir.

*(Not: Fonksiyonu sadece `def` ile tanımlamak, kodun çalışması için yeterli değildir. Sadece "böyle bir alet ürettim ve kenara koydum" dersiniz. Aleti kullanmak için onu ismiyle **çağırmanız (call)** gerekir. Egzersiz dosyasında "Running your function alone does nothing" (Fonksiyonu tek başına çalıştırmak hiçbir şey yapmaz) denmesinin sebebi tam olarak budur. `tester.py` dosyası senin fonksiyonunu import edip çağırarak test eder.)*

<br>

## `print()` ve `return` Arasındaki Hayati Fark

* **`print()`:** Sadece ve sadece terminale (ekrana) yazı yazdırmaya yarar. İnsan gözünün görmesi içindir. Bilgisayar veya programın geri kalanı o değeri kullanamaz, sadece ekranda belirip kaybolan bir ışıktır.
* **`return`:** Fonksiyonun çalışmasını bitirir ve elde edilen sonucu **fonksiyonun çağrıldığı yere geri fırlatır**. Fırlatılan bu değer başka bir değişkene atanabilir, matematikte kullanılabilir.

**Örnekle Anlayalım:**

```python
# Sadece print yapan fonksiyon
def topla_ve_yazdir(a, b):
    print(a + b)

# Return yapan fonksiyon
def topla_ve_dondur(a, b):
    return a + b

# Kullanımları:
sonuc_1 = topla_ve_yazdir(5, 5) 
# Ekranda 10 yazar ama sonuc_1 değişkenine hiçbir şey atanmaz (None olur).
# sonuc_1 + 2 yapmaya çalışırsanız HATA alırsınız.

sonuc_2 = topla_ve_dondur(5, 5) 
# Ekranda hiçbir şey yazmaz! Ama 10 değeri sonuc_2'nin içine girer.
# print(sonuc_2 + 2) derseniz ekranda 12 görürsünüz.

```

**Egzersizindeki Durum:**
Fonksiyon hem ekrana `List : <class 'list'>` gibi yazılar yazdırmalı (`print` kullanılmalı), hem de en sonda görevi bitirirken `42` sayısını geri döndürmeli (`return 42` kullanılmalı).

Dikkat edildiğinde `tester.py` dosyasının en son satırında `print(all_thing_is_obj(10))` diyor. Yani fonksiyon 10 sayısı için çalışacak, ekrana "Type not found" yazdıracak, sonra `42` sayısını fırlatacak ve dışarıdaki `print` komutu da fırlatılan bu `42`'yi ekrana basacak.

<br>

## Nesnelerin Tipini Bulmak: `type()`

Python'da "her şey bir nesnedir" (Everything is an object). Metinler, sayılar, listeler... Her birinin bir sınıfı (class) vardır.

Bir nesnenin hangi sınıfa ait olduğunu bulmak için `type()` fonksiyonunu kullanırız. Ve `type()` fonksiyonunun çıktısı tam da egzersizdeki formatta!

```python
isim = "Ahmet"
liste = [1, 2, 3]

print(type(liste))  # Çıktı: <class 'list'>
print(type(isim))   # Çıktı: <class 'str'>

```

<br>

## Akış Kontrolü: Hangi Tipe Hangi Mesaj? (`if / elif / else`)

Artık sana gelen nesnenin tipini nasıl bulacağını biliyorsun. Şimdi gelen tipe göre farklı mesajlar yazdırman gerekiyor. Bunun için `if` (eğer) ve `elif` (değilse eğer) yapılarını kullanmalısın.

Tip sorgulaması yaparken `type(nesne) == aranan_tip` veya daha çok tercih edilen `type(nesne) is aranan_tip` mantığını kurabilirsin.

```python
def tip_kontrolcusu(veri):
    if type(veri) is list:
        print(f"Bu bir liste! Tipi: {type(veri)}")
    elif type(veri) is str:
        print(f"Bana metin yolladın: {veri}")
    else:
        print("Bunun ne olduğunu bilmiyorum.")
    
    return 100 # Fonksiyon bittiğinde 100 döndür

```

<br></br>

## Not: Python'da `==` ve `is` Operatörleri Arasındaki Fark

Python'da mantıksal değerleri (`True`, `False`) veya boşluk durumunu (`None`) kontrol ederken **PEP 8 (Python Geliştirme Standartları)** kurallarına göre `==` yerine `is` operatörünün kullanılması tavsiye edilir.

<br>

### 1. `==` Operatörü (Değer Eşitliği / Equality)

`==` operatörü, iki nesnenin **taşıdığı değerin** aynı olup olmadığına bakar. Bellekteki yerleri farklı olsa bile, mantıksal karşılıkları aynıysa `True` dönebilir.

* Python'da sayısal `0` değeri ve mantıksal `False` değeri karşılaştırıldığında birbirine eşit kabul edilir.

    ```python
    0 == False  # Çıktı: True

    ```

<br>

### 2. `is` Operatörü (Kimlik Eşitliği / Identity)

`is` operatörü, iki değişkenin bellekte (RAM'de) **tamamen aynı nesne** olup olmadığına bakar. Arka planda nesnelerin kimlik numaralarını (`id(a) == id(b)`) karşılaştırır.

* `0` bir tamsayı (integer), `False` ise mantıksal (boolean) bir nesnedir. Değerleri benzese de bellekteki konumları ve tipleri tamamen farklıdır.

    ```python
    0 is False  # Çıktı: False

    ```

<br>

### Neden `is` Kullanmalıyız? (Singleton Mimarisi)

Python çalıştığında bellekte sadece **bir tane** `True`, **bir tane** `False` ve **bir tane** `None` nesnesi yaratılır. Buna "Singleton" (tekil) mimari denir.

Eğer bir değişken `False` ise, aslında bellekteki o yegane `False` nesnesini işaret ediyordur. Bu tarz değişmez ve tekil yapıları kontrol ederken değer kontrolü (`==`) yerine bellek/kimlik kontrolü (`is`) yapmak hem daha performanslıdır hem de `0 == False` gibi istenmeyen mantık hatalarının önüne geçer.

<br>

### Kod Üzerinde Örnek Karşılaştırma

**❌ Hatalı / Riskli Kullanım:**
Sadece değerleri kontrol ettiği için gelen veri `0` olduğunda da şartı sağlar ve hatalı mantığa yol açar.

```python
if object == False:

```

<br>

**⚠️ Kabul Edilebilir (Ancak İdeal Değil):**
Tip kontrolü yapılarak risk ortadan kaldırılmış. Kod doğru çalışır ancak evrensel Python (PEP 8) yazım kurallarına göre `==` kullanımı "Pythonic" (şık) değildir.

```python
if type(object) is bool and object == False:

```

<br>

**✅ Best Practice (En İyi Kullanım - PEP 8 Uyumlu):**
Hem güvenli hem de performanslıdır. Gelen veri `0` olsa bile `0 is False` durumu `False` döneceği için ekstra tip kontrolüne bile gerek kalmaz.

```python
if object is False:

```

<br></br>

## Lambda Fonksiyonları

Python'da `lambda`, en basit tabirle **isimsiz (anonim), tek satırlık ve "kullan-at"** fonksiyonlar oluşturmamızı sağlayan bir yapıdır. Normalde bir fonksiyon tanımlamak için `def` anahtar kelimesini kullanırız ve ona bir isim veririz. Ancak bazen bir fonksiyonu sadece tek bir yerde, kısa bir işlem için kullanmamız gerekir. İşte `lambda` tam bu noktada sahneye çıkar.

<br>

### Temel Sözdizimi (Syntax)

Bir lambda fonksiyonunun yapısı şu şekildedir:

`lambda parametreler: döndürülecek_ifade`

* **`lambda`**: Bu kelimeyle başlar (tıpkı `def` gibi).
* **parametreler**: Fonksiyonun alacağı girdilerdir. Birden fazla ise virgülle ayrılır.
* **`:`**: Parametreler ile yapılacak işlemi ayırır.
* **ifade**: Tek satırlık bir işlemdir. Bu işlemin sonucu **otomatik olarak `return` edilir** (Yani `return` kelimesini yazmanıza gerek yoktur, yazarsanız hata alırsınız).

#### `def` ve `lambda` Karşılaştırması

İkisinin arka planda yaptığı iş aynıdır ama yazılışları farklıdır:

```python
# Klasik yöntem (def ile)
def kare_al(x):
    return x ** 2

# Lambda yöntemi
kare_al_lambda = lambda x: x ** 2

print(kare_al(5))        # Çıktı: 25
print(kare_al_lambda(5)) # Çıktı: 25

```

<br></br>

### Lambda'nın Gerçek Gücü: Yüksek Mertebeden Fonksiyonlar

Lambda'yı yukarıdaki örnekteki gibi bir değişkene atamak aslında pek mantıklı değildir (nedenini aşağıda "Kurallar" bölümünde açıklayacağım). Lambda'nın asıl gücü, **başka fonksiyonlara parametre olarak gönderildiğinde** ortaya çıkar.

Özellikle `map()`, `filter()` ve `sorted()` gibi yerleşik fonksiyonlarla mükemmel bir uyum içinde çalışır.

<br>

#### 1. `filter()` ile Kullanımı

Önceki test dosyanızda yazdığınız `ft_filter` mantığıyla aynıdır (ex06 part 1). Bir listedeki elemanları belirli bir şarta göre süzmek için kullanılır.

```python
sayilar = [1, 2, 3, 4, 5, 6, 7, 8]

# Sadece çift sayıları filtreleyelim
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))

print(ciftler)
# Çıktı: [2, 4, 6, 8]

```

<br>

#### 2. `map()` ile Kullanımı

Bir listedeki her bir elemana aynı işlemi uygulamak (dönüştürmek) için kullanılır.

```python
fiyatlar = [100, 200, 300]

# Her fiyata %20 KDV ekleyelim
kdvli_fiyatlar = list(map(lambda x: x * 1.20, fiyatlar))

print(kdvli_fiyatlar)
# Çıktı: [120.0, 240.0, 360.0]

```

<br>

#### 3. `sorted()` (veya `.sort()`) ile Kullanımı

Karmaşık veri yapılarını belirli bir kurala göre sıralamak için hayat kurtarır. Örneğin, içinde sözlükler olan bir listeyi sıralamak isteyelim:

```python
ogrenciler = [
    {"isim": "Ayşe", "not": 90},
    {"isim": "Ali", "not": 70},
    {"isim": "Veli", "not": 85}
]

# Öğrencileri notlarına göre (küçükten büyüğe) sıralayalım
sirali_ogrenciler = sorted(ogrenciler, key=lambda ogrenci: ogrenci["not"])

print(sirali_ogrenciler)
# Çıktı: [{'isim': 'Ali', 'not': 70}, {'isim': 'Veli', 'not': 85}, {'isim': 'Ayşe', 'not': 90}]

```

<br></br>

### İleri Seviye: Lambda'nın Sınırları ve PEP 8 Standartları

Lambda kullanırken bilmeniz gereken bazı katı kurallar ve yazılım standartları vardır.

| Sınır / Kural | Açıklaması |
| --- | --- |
| **Tek Satır Sınırı** | Lambda içinde `if-elif-else` blokları, döngüler (`for`, `while`) veya değişken atamaları kullanamazsınız. Sadece tek bir "expression" (ifade) içerebilir. |
| **Ternary (Tek Satır İf)** | `if-else` kullanılabilir ama tek satır formatında olmak zorundadır: `lambda x: "Çift" if x % 2 == 0 else "Tek"` |
| **İsimlendirme (PEP 8)** | Python'ın resmi yazım kuralı rehberi PEP 8, **lambda fonksiyonlarını değişkenlere atamayı kesinlikle yasaklar.** |

#### Neden Değişkene Atamamalıyız? (Hata Ayıklama Sorunu)

Savunma odaklı programlama ve `AssertionError` konularında gördüğümüz gibi, hataların izlenebilirliği (traceback) çok önemlidir.

Eğer lambda'yı bir değişkene atarsanız (`topla = lambda x, y: x + y` gibi) ve bu fonksiyonda bir hata çıkarsa, Python terminalde fonksiyonun adını `topla` olarak değil, `<lambda>` olarak gösterir. Bu da binlerce satırlık bir kodda hatanın hangi lambda'dan geldiğini bulmanızı imkansızlaştırır. Bu yüzden isimlendirilmiş bir fonksiyona ihtiyacınız varsa **daima `def` kullanmalısınız.** Lambda sadece `map`, `filter` veya `key` parametreleri içinde anonim kalmalıdır.

<br></br>
