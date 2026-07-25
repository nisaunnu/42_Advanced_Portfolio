# Python - 0 - Starting Not İçeriği

- [Python'da "Null" Kavramı ve Falsy Değerler](#pythonda-null-kavramı-ve-falsy-değerler)
- [`None` (NoneType) Nesnesi ve Güvenli Kontrol](#none-nonetype-nesnesi-ve-güvenli-kontrol)
    - [Kritik Detay: Neden `==` değil de `is`?](#kritik-detay-neden--değil-de-is)
- [Mantıksal `False` ve Sayısal `0` Arasındaki Gizli İlişki](#mantıksal-false-ve-sayısal-0-arasındaki-gizli-i̇lişki)
    - [Arka Plan Mekanizması](#arka-plan-mekanizması)
    - [Bu Tuzaktan Kaçınma Yöntemi](#bu-tuzaktan-kaçınma-yöntemi)
- [Bilgisayar Bilimlerinin Gizemli Değeri: `NaN` (Not a Number)](#bilgisayar-bilimlerinin-gizemli-değeri-nan-not-a-number)
    - [NaN Değerinin Eşsiz Tuzağı](#nan-değerinin-eşsiz-tuzağı)
    - [NaN Nasıl Yakalanır? (Hacker Taktiği)](#nan-nasıl-yakalanır-hacker-taktiği)
- [Boş Karakter Dizileri (`""`)](#boş-karakter-dizileri--)
- [Altın Kural: Tip ve Değerin Birlikte Sorgulanması (Strict Evaluation)](#altın-kural-tip-ve-değerin-birlikte-sorgulanması-strict-evaluation)
- [Fonksiyonlarda Çıkış Kodları (Exit Codes) Standartı](#fonksiyonlarda-çıkış-kodları-exit-codes-standartı)
- [None ve type(None) Farkı](#none-ve-typenone-farkı)
    - [Kalıp ile Ürün Arasındaki Fark](#i̇şin-sırrı-kalıp-ile-ürün-arasındaki-fark)
    - [Neden `if obj_type is None:` satırı başarısız oldu?](#1-durum-neden-if-obj_type-is-none-satırı-başarısız-oldu)
    - [Neden `if obj_type is type(None):` satırı çalıştı?](#2-durum-neden-if-obj_type-is-typenone-satırı-çalıştı)
    - [En Temiz Alternatif Neydi?](#en-temiz-alternatif-neydi)

<br></br>

## Python'da "Null" Kavramı ve Falsy Değerler

C tabanlı dillerdeki `null` veya JavaScript'teki `undefined` kavramlarının aksine Python, yerleşik bir `null` anahtar kelimesine sahip değildir. Bunun yerine bellekte tek bir örneği (singleton) bulunan **`None`** nesnesini kullanır.

Ancak programlama mantığında sadece `None` değil; içeriği boş, sıfır veya mantıksal olarak geçersiz olan değerler de geniş anlamda "Null/Boş" kabul edilir. Python'da bir `if` koşuluna sokulduğunda `False` gibi davranan bu değerlere **Falsy Değerler** denir. En sık karşılaşılanları şunlardır:

* `None` (Yokluk)
* `float("NaN")` (Tanımsız/Geçersiz sayı)
* `0` (Sayısal boşluk)
* `""` (Metinsel boşluk)
* `False` (Mantıksal yokluk)

Bu değerlerin hepsi mantıksal bir sorguda `False` üretse de, **veri tipleri birbirinden tamamen farklıdır**. Güvenli bir kod yazmak için bu tipleri birbirine karıştırmadan yakalamak gerekir.

<br></br>

## `None` (NoneType) Nesnesi ve Güvenli Kontrol

`None`, Python'da hiçbir değer taşımayan, kendine ait bir tipi (`NoneType`) olan özel bir nesnedir. Genelde bir fonksiyon geriye bilerek bir şey döndürmediğinde veya bir değişken henüz başlatılmadığında kullanılır.

### Kritik Detay: Neden `==` değil de `is`?

Python'da `None` kontrolü yaparken `if x == None:` yerine her zaman **`if x is None:`** kalıbı tercih edilmelidir.

* `==` operatörü nesnelerin **değerlerini** kıyaslar ve sınıflar içinde aşırı yüklenebilir (`__eq__` metodu ile değiştirilebilir). Bu da yanıltıcı sonuçlar doğurabilir.
* `is` operatörü ise nesnelerin **bellekteki adreslerini (identity)** kıyaslar. `None` bellekte benzersiz (singleton) olduğu için `is` kullanımı hem daha hızlıdır hem de kesin sonuç verir.

```python
x = None
if x is None:
    print("Değişken nesne olarak None'dır.")

```

<br></br>

## Mantıksal `False` ve Sayısal `0` Arasındaki Gizli İlişki

Python'ın en büyük tasarım tuzaklarından biri `False` ve `0` değerlerinin değer bazında birbirine eşit kabul edilmesidir.

### Arka Plan Mekanizması

Python'da `bool` (mantıksal) sınıfı, tarihsel ve mimari sebeplerle `int` (tam sayı) sınıfının bir **alt sınıfıdır (subclass)**. Yani `False` nesnesi arka planda aslında sayısal olarak `0` değerini taşır (`True` ise `1`'dir).

```python
print(issubclass(bool, int))  # Çıktı: True
print(False == 0)             # Çıktı: True (TUZAK!)

```

<br>

### Bu Tuzaktan Kaçınma Yöntemi

Sadece `if x == 0:` kontrolü yaparsak, gelen değer `False` olduğunda da bu blok çalışır. Bunu engellemek için **strict (kesin)** bir kontrol yapmalı, değerle birlikte **tip doğrulaması** da eklemeliyiz:

```python
x = False

# Yanlış yaklaşım (False geldiğinde de sıfır sanır)
if x == 0:
    print("Sayı sıfırdır.") 

# Doğru yaklaşım (Hem tip tam sayı olmalı hem de değer sıfır olmalı)
if type(x) is int and x == 0:
    print("Kesinlikle sayısal sıfır.")
elif type(x) is bool and x is False:
    print("Kesinlikle mantıksal False.")

```

<br></br>

## Bilgisayar Bilimlerinin Gizemli Değeri: `NaN` (Not a Number)

`NaN` (Sayı Değil), IEEE 754 yüzen nokta (floating-point) standartlarına göre tanımlanmış, matematiksel olarak tanımsız veya geçersiz işlemleri (örneğin sıfırın sıfıra bölünmesi veya sonsuzdan sonsuzun çıkarılması gibi) temsil eden özel bir `float` değeridir.

Python'da harici bir kütüphane (Numpy/Math vb.) kullanmadan `float("NaN")` veya `float("nan")` şeklinde üretilebilir.

### `NaN` Değerinin Eşsiz Tuzağı

`NaN` değerinin bilgisayar bilimlerindeki en ayırt edici özelliği, **kendisine eşit olmayan tek değer olmasıdır**.

```python
nan_degeri = float("NaN")
print(nan_degeri == float("NaN"))  # Çıktı: False!
print(nan_degeri == nan_degeri)      # Çıktı: False!

```

<br>

### `NaN` Nasıl Yakalanır? (Hacker Taktiği)

Dışarıdan bir kütüphane (`math.isnan`) kullanmamızın yasak olduğu senaryolarda, bir değişkenin `NaN` olup olmadığını anlamak için bu eşsiz tuzağı bir silaha dönüştürebiliriz: **Eğer bir nesnenin tipi `float` ise ve kendisi kendisine eşit değilse, o nesne kesinlikle `NaN`'dır.**

```python
x = float("NaN")

if type(x) is float and x != x:
    print("Bu değer bir NaN (Not a Number) değeridir.")

```

<br></br>

## Boş Karakter Dizileri (`""`) ve Metinsel Kontrol

Boş bir string (`""`), bellekte yer kaplayan ve tipi `str` olan geçerli bir nesnedir ancak karakter uzunluğu sıfırdır.

Kontrol edilirken yine diğer falsy değerlerle (özellikle `None` veya boş listelerle) karışmaması için tipinin `str` olduğundan emin olunmalıdır.

```python
metin = ""
if type(metin) is str and metin == "":
    print("Bu boş bir metindir.")

```

<br></br>

## Altın Kural: Tip ve Değerin Birlikte Sorgulanması (Strict Evaluation)

Görüldüğü üzere, Python'ın esnek yapısı "yokluk" ve "boşluk" durumlarında veri tiplerinin birbirinin yerine geçmesine (implicit type coercion) neden olabilir. Güvenli akış kontrolü (flow control) sağlamanın altın kuralı, her zaman **veri tipini sabitleyip ardından değer kontrolü yapmaktır.**

```python
# Tüm Null benzeri varyasyonları hatasız ayıran şablon mimari:
def veri_analiz_merkezi(veri):
    if veri is None:
        return "None Nesnesi"
    elif type(veri) is float and veri != veri:
        return "Geçersiz Sayı (NaN)"
    elif type(veri) is int and veri == 0:
        return "Sayısal Sıfır"
    elif type(veri) is str and veri == "":
        return "Boş Metin"
    elif type(veri) is bool and veri is False:
        return "Mantıksal Yanlış"
    else:
        return "Geçerli/Dolu Veri"

```

<br></br>

## Fonksiyonlarda Çıkış Kodları (Exit Codes) Standartı

Yazılım dünyasında (özellikle Unix mimarisinde ve alt seviye dillerde) bir fonksiyonun veya programın çalışma sonucunu numerik olarak döndürmek standart bir kurala bağlıdır:

* **`return 0` (Başarı / Success):** İşlemlerin tamamen yolunda gittiğini, hiçbir hata veya beklenmedik durumla karşılaşılmadığını belirtir.
* **`return 1` (veya sıfır dışı herhangi bir sayı - Hata / Error):** İşlem sırasında bir hata oluştuğunu, aranan durumun bulunamadığını veya geçersiz bir parametre gönderildiğini sistem süreçlerine (veya test araçlarına) bildirir.

Bu yaklaşım, yazdığımız fonksiyonların dış dünyadaki test araçları (`tester.py` gibi otomasyon scriptleri) tarafından doğru şekilde doğrulanabilmesini sağlar.

<br></br>

## None ve type(None) Farkı

### İşin Sırrı: "Kalıp" ile "Ürün" Arasındaki Fark

Python'da her şey bir nesnedir. Bir veri tipinin kendisi **Kalıptır (Class)**, o tipten üretilen veri ise **Üründür (Instance)**.

* `None`: Bir **üründür** (değerdir).
* `<class 'NoneType'>`: O ürünün **kalıbıdır** (tipidir).

Sen kodun başında `obj_type = type(object)` satırıyla, gelen nesnenin **kalıbını** `obj_type` isimli değişkene kilitledin. `Nothing = None` geldiğinde, `obj_type` değişkeninin içinde artık **`<class 'NoneType'>` kalıbı** var.

<br>

### 1. Durum: Neden `if obj_type is None:` satırı başarısız oldu?

Eğer kodu şu şekilde yazdıysan:

```python
if obj_type is None:  # Python bunu "Yanlış" kabul etti!

```

Arka planda Python şu sorguyu yaptı:

* `obj_type` içinde ne var? $\rightarrow$ `<class 'NoneType'>` (Kalıp)
* Karşılaştırılan şey ne? $\rightarrow$ `None` (Ürün/Değer)

Python'a *"Kalıbın kendisi, ürünün kendisine eşit midir?"* diye sordun. Biri sınıf, biri değer olduğu için Python buna `False` dedi. Şart sağlanmadığı için o bloku atladı ve en alttaki `Type not Found` kısmına düştü.

<br>

### 2. Durum: Neden `if obj_type is type(None):` satırı çalıştı?

Kodu şu şekle çevirdiğinde:

```python
if obj_type is type(None):  # Python bunu "Doğru" kabul etti!

```

Arka planda Python bu kez şu sorguyu yaptı:

* `obj_type` içinde ne var? $\rightarrow$ `<class 'NoneType'>` (Kalıp)
* `type(None)` ne üretiyor? $\rightarrow$ `<class 'NoneType'>` (Kalıp)

Bu sefer Python'a *"Elimdeki kalıp, None'ın orijinal kalıbıyla aynı mıdır?"* diye sordun. İki taraf da aynı sınıf/kalıp nesnesi olduğu için Python `True` döndürdü ve ekrana başarıyla `"Nothing"` yazdı.

<br>

### En Temiz Alternatif Neydi?

Eğer tipi kaydettiğin `obj_type` değişkeni üzerinden değil de, doğrudan gelen orijinal `object` değişkeni (ürünün kendisi) üzerinden gitmek isteseydin, kalıp çıkarmaya gerek kalmadan doğrudan şunu yazabilirdin:

```python
if object is None:  # Ürün, Ürünle kıyaslanıyor.
    print(f"Nothing: {object} {obj_type}")
    return 0

```

Bu durumda da ürün ürünle kıyaslandığı için (`None is None`) kodun yine kusursuz çalışırdı.