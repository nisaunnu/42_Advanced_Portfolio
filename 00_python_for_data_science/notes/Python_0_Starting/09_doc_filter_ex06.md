# `__doc__` & `filter` & ex06

- [`__doc__` Nedir?](#__doc__-nedir)
- [`filter` Fonksiyonunda `function is None` Durumu (ex06 part 1)](#filter-fonksiyonunda-function-is-none-durumu)
- [Orijinal `filter` ile `ft_filter` Farkı (ex06 part 1)](#orijinal-filter-ile-ft_filter-farkı)
- [Argüman Doğrulama Mantığı (ex06 part 2)](#argüman-doğrulama-mantığı)
- [Kelime Filtreleme: List Comprehension + Lambda (ex06 part 2)](#kelime-filtreleme-list-comprehension-lambda)
- [`ValueError` ile `AssertionError` Arasındaki İlişki (ex06 part 2)](#valueerror-ile-assertionerror-arasındaki-ilişki)
- [Genel Özet](#genel-özet)

<br></br>

## `__doc__` Nedir?

Python'da her fonksiyon/sınıf/modülün, tanımlandığı yerin hemen
altındaki üç tırnaklı (`"""..."""`) string'i otomatik olarak
`__doc__` özniteliğine (attribute) kaydedilir:

```python
def topla(a, b):
    """İki sayıyı toplar."""
    return a + b

print(topla.__doc__)   # İki sayıyı toplar.
```

`filter` built-in fonksiyonunun kendi docstring'i şudur:

```python
>>> print(filter.__doc__)
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
```

Bizim görevimiz `ft_filter` fonksiyonuna **tam olarak bu metni**
docstring olarak vermek. Bunu doğrularken:

```python
ft_filter.__doc__ == filter.__doc__   # True olmalı
```

**Dikkat edilmesi gereken incelik:** Docstring'i normal Python
alışkanlığıyla (satırları girintileyerek, güzelce biçimlendirerek)
yazarsan metin birebir eşleşmez — çünkü girinti boşlukları ve satır
kırılımları string'in **parçasıdır**. Bu yüzden docstring'i,
orijinal metnin satır düzenini bozmadan (soldan hizalamayı takip
ederek) aynen kopyalamak gerekiyor:

```python
def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
```

<br></br>

## `filter` Fonksiyonunda `function is None` Durumu (ex06 part 1)

Orijinal `filter`'ın docstring'i şunu söylüyor: *"If function is
None, return the items that are true."* Yani `filter(None, iterable)`
çağrıldığında, fonksiyon yerine **her elemanın kendi truthy/falsy
değerine** bakılır (`if item` gibi). Örnek:

```python
filter(None, [0, 1, "", "a", None, 5])
# sonuç: [1, 'a', 5]  (0, "", None gibi "falsy" değerler elenir)
```

Bu yüzden `ft_filter` içinde iki ayrı davranış var:

```python
def ft_filter(function, iterable):
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
```

- `function is None` → elemanın kendisi truthy mi diye bakılır
  (`if item`).
- `function` bir fonksiyonsa → `function(item)` çağrılıp sonucu
  truthy mi diye bakılır (`if function(item)`).

**Neden `is None`, `== None` değil?**
`None`, Python'da **tekil (singleton)** bir nesnedir — bellekte tek
bir kopyası vardır. Bir değişkenin `None` olup olmadığını kontrol
ederken `==` yerine `is` kullanmak Python'ın önerdiği (PEP8) ve daha
doğru yoldur, çünkü `==` bir nesnenin özel `__eq__` metodunu
çağırabilir ve beklenmedik sonuçlar verebilir; `is` ise doğrudan
**bellek adresi (identity)** karşılaştırması yapar, bu yüzden `None`
kontrolünde her zaman güvenilirdir.

<br></br>

## Orijinal `filter` ile `ft_filter` Farkı (ex06 part 1)

Gerçek `filter()` **lazy bir iterator** (filter object) döner —
yani elemanları anında hesaplamaz, sen `list()` ile sardığında ya da
`for` ile gezdiğinde hesaplanır. Bizim `ft_filter`'ımız ise list
comprehension kullandığı için doğrudan bir **liste (list)** döner —
"eager" (anında hesaplanan) bir yapı. Subject bunu bilerek istiyor
("you should use list comprehensions to recode your ft_filter"),
yani davranış tam birebir aynı olmasa da (iterator vs. list), doküman
eşitliği ve filtreleme mantığı aynı kalıyor.

<br></br>

## Argüman Doğrulama Mantığı (ex06 part 2)

```python
def get_arguments():
    assert len(sys.argv) == 3, "the arguments are bad"
    text = sys.argv[1]
    try:
        limit = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    return text, limit
```

- `sys.argv` her zaman string listesi döndürür — komut satırından
  gelen hiçbir şey otomatik olarak `int`'e çevrilmez. Bu yüzden
  ikinci argümanı **biz manuel olarak** `int(...)` ile çevirmemiz
  gerekiyor.
- Eğer `sys.argv[2]` sayıya çevrilemeyen bir string ise (örneğin
  `"Hello the World"`), `int(...)` bir `ValueError` fırlatır. Biz
  bunu yakalayıp, subject'in istediği mesajla birlikte
  `AssertionError`'a çeviriyoruz (`raise AssertionError(...)`).
- `len(sys.argv) == 3` kontrolü: `sys.argv[0]` dosya adı olduğu için,
  gerçek argüman sayısı 2 olduğunda `len(sys.argv)` 3 olur.

**Neden `assert` ve `raise AssertionError` birlikte kullanılıyor?**
`assert` ifadesi sadece **boolean bir koşulu** test edip
`AssertionError` fırlatabilir; ama `int()` çağrısının içeride
fırlattığı hata zaten bir `ValueError`'dur, `assert` ile
yakalanamaz. Bu yüzden `try/except ValueError` ile yakalayıp, elle
`raise AssertionError("the arguments are bad")` yaparak subject'in
istediği hata tipine "çeviriyoruz".

<br></br>

## Neden `python filterstring.py 3 'Hello the World'` Hata Veriyor? (ex06 part 2)

Subject'teki örnekte argüman sırası **tersine çevrilmiş**:
ilk argüman `"3"` (aslında `N` olması gereken), ikinci argüman
`"Hello the World"` (aslında `S` olması gereken). Bizim kodumuz
her zaman **ilk argümanı `S`, ikinciyi `N`** olarak okuduğu için:

- `text = "3"` (sorun yok, her string geçerli bir `S`'dir)
- `limit = int("Hello the World")` → `ValueError` → `AssertionError:
  the arguments are bad`

Yani hata, argümanların **yanlış tipte/yanlış sırada** verilmesinden
kaynaklanıyor — programın bunu tespit edip düzgün bir hata mesajı
vermesi bekleniyor.

<br></br>

## Kelime Filtreleme: List Comprehension + Lambda (ex06 part 2)

```python
def filter_words(text, limit):
    return [word for word in text.split(" ")
            if (lambda w: len(w) > limit)(word)]
```

Burada iki ayrı zorunluluk **aynı satırda** birleştirilmiş:

1. **List comprehension:** `[word for word in text.split(" ") if ...]`
2. **Lambda:** `(lambda w: len(w) > limit)`

**`text.split(" ")` ne yapar?**
String'i, verilen ayraca (burada boşluk `" "`) göre parçalara ayırıp
bir liste döner:

```python
"Hello the World".split(" ")
# ['Hello', 'the', 'World']
```

**Neden lambda'yı bir değişkene atamadık (`is_long_enough = lambda ...`)
değil de doğrudan çağırdık?**

```python
# Kaçınılan yöntem (flake8 E731 uyarısı verir):
is_long_enough = lambda word: len(word) > limit
...

# Kullanılan yöntem (norm'a uygun, anında çağrılan lambda):
(lambda w: len(w) > limit)(word)
```

PEP8/flake8 kuralı (E731), bir lambda'yı bir isme **atamayı**
önermez — çünkü "eğer bir fonksiyona isim veriyorsan, zaten
`def` kullanmalısın, lambda'nın amacı isimsiz/anlık kullanım
sağlamaktır" mantığı vardır. Biz de bu yüzden lambda'yı tanımladığımız
anda parantezle **hemen çağırıyoruz**: `(lambda w: ...)(word)`. Bu,
"IIFE" (Immediately Invoked Function Expression) deseninin
Python'daki karşılığıdır — lambda tanımlanır tanımlanmaz, hemen
`word` argümanıyla çalıştırılır ve sonucu (`True`/`False`) döner.

<br></br>

## Genel Özet

| Kavram                      | Nerede Kullanıldı                                            |
| --------------------------- | ------------------------------------------------------------ |
| `__doc__` özniteliği        | `ft_filter`'ın docstring'ini `filter.__doc__` ile eşitlemek  |
| `is None` vs `== None`      | `function is None` kontrolü                                  |
| List comprehension          | Her iki dosyada da filtreleme mantığı                        |
| `lambda`                    | `filterstring.py`'de anlık (inline) çağrılan fonksiyon       |
| `sys.argv`                  | Komut satırı argümanlarını okumak                            |
| `assert` / `AssertionError` | Argüman sayısı ve tip doğrulama                              |
| `try/except` + `raise`      | `ValueError`'ı `AssertionError`'a çevirmek                   |
| `str.split(" ")`            | Cümleyi kelimelere ayırmak                                   |
| flake8 E731 kuralı          | Lambda'yı isme atamak yerine anında çağırmak                 |


<br></br>
