# Data Structures
- [Temel Veri Yapıları](#temel-veri-yapıları)
    - [List (Liste)](#1-list-liste)
    - [Tuple (Demet)](#2-tuple-demet)
    - [Set (Küme)](#3-set-küme)
    - [Dictionary (Sözlük / Dict)](#4-dictionary-sözlük--dict)
    - [Özet ve Karşılaştırma](#5-özet-ve-karşılaştırma)


<br></br>

## Temel Veri Yapıları

### 1. List (Liste)

Listeler, birden fazla öğeyi tek bir değişkende sıralı olarak saklamak için kullanılır. Python'da en sık kullanılan veri yapılarından biridir. İndeksleme mantığıyla çalıştığı için tam kontrol sağlar ve veri manipülasyonu için çok sayıda yerleşik metoda (built-in methods) sahiptir.

* **Sıralıdır (Ordered):** Elemanların belirli bir sırası vardır ve bu sıra değişmez. Yeni eklenen elemanlar dinamiğe göre listeye yerleşir.
* **Değiştirilebilirdir (Mutable):** Liste oluşturulduktan sonra elemanlar eklenebilir, çıkarılabilir veya güncellenebilir.
* **Yinelenen Eleman Barındırabilir (Allows Duplicates):** Aynı değere sahip birden fazla eleman bulunabilir.
* **Tanımlama:** Köşeli parantez `[]` ile tanımlanır.

<br>

#### Yerleşik Liste Metotları (Built-in Methods)
---

**1. Ekleme İşlemleri:**


* `append(eleman)`: Listenin **en sonuna** tek bir eleman ekler.
* `insert(indeks, eleman)`: Belirtilen **indeks konumuna** eleman ekler. Mevcut elemanları sağa kaydırarak araya girer.
* `extend(iterable)`: Başka bir listenin (veya yinelenebilir bir yapının) tüm elemanlarını tek tek mevcut listenin sonuna ekler.

    ```python
    liste = [10, 20]
    liste.append(30)         # [10, 20, 30]
    liste.insert(1, 15)      # [10, 15, 20, 30]
    liste.extend([40, 50])   # [10, 15, 20, 30, 40, 50]

    ```

<br>

**2. Silme İşlemleri:**

* `pop(indeks)`: Belirtilen indeksteki elemanı siler ve sildiği bu elemanı döndürür. İndeks verilmezse (`pop()`) varsayılan olarak **en sondaki** elemanı siler.
* `remove(değer)`: Liste içinde belirtilen değere sahip **ilk** elemanı bulur ve siler. Aranan değer listede yoksa hata fırlatır.
* `clear()`: Listenin içindeki tüm elemanları silerek listeyi tamamen boşaltır (`[]`).

    ```python
    liste = [10, 20, 30, 20, 40]
    silinen = liste.pop()    # Son elemanı (40) siler ve 'silinen' değişkenine atar.
    liste.pop(0)             # İlk elemanı (10) siler. Liste: [20, 30, 20]
    liste.remove(20)         # Gördüğü ilk 20 değerini siler. Liste: [30, 20]
    liste.clear()            # Listeyi tamamen boşaltır: []

    ```

<br>

**3. Arama ve Sayma İşlemleri:**

* `index(değer)`: Belirtilen değere sahip ilk elemanın **indeks numarasını** döndürür. Aranan değer listede yoksa hata fırlatır.
* `count(değer)`: Belirtilen değerin liste içinde **kaç defa** geçtiğini sayar.

    ```python
    liste = ["a", "b", "c", "b", "d"]
    print(liste.index("c"))  # Çıktı: 2 (c elemanı 2. indekste)
    print(liste.count("b"))  # Çıktı: 2 (Listede iki tane "b" var)

    ```

<br>

**4. Düzenleme ve Kopyalama İşlemleri:**

* `sort()`: Listeyi küçükten büyüğe (veya alfabetik olarak) sıralar. `reverse=True` parametresi ile büyükten küçüğe sıralayabilir. (Orijinal listeyi kalıcı olarak değiştirir).
* `reverse()`: Listenin mevcut sırasını (büyüklük/küçüklük fark etmeksizin) baştan sona tam tersine çevirir. (Orijinal listeyi kalıcı olarak değiştirir).
* `copy()`: Listenin sığ bir kopyasını (shallow copy) oluşturur. Orijinal listeyi bozmadan yedek almak veya üzerinde bağımsız işlemler yapmak için kullanılır.

    ```python
    sayilar = [5, 2, 9, 1]
    sayilar.sort()             # [1, 2, 5, 9]
    sayilar.sort(reverse=True) # [9, 5, 2, 1]

    harfler = ["x", "y", "z"]
    harfler.reverse()          # ["z", "y", "x"]

    # Kopyalama Örneği
    yedek_liste = harfler.copy() # Orijinal harfler listesinden bağımsız yeni bir liste

    ```

#### Yazdırma ve Erişim İşlemleri
---

```python
meyveler = ["elma", "armut", "muz", "çilek"]

# 1. Belirli Bir Elemanı Yazdırma (İndeks ile)
print(meyveler[0])     # Baştaki eleman: 'elma'
print(meyveler[-1])    # Sondaki eleman: 'çilek'

# 2. Toplu Yazdırma
print(meyveler)        # Liste formatında: ['elma', 'armut', 'muz', 'çilek']
print(*meyveler)       # Yan yana parantezsiz: elma armut muz çilek

# Döngü ile alt alta toplu yazdırma
for meyve in meyveler:
    print(meyve)

# 3. Tersten Yazdırma Alternatifi (Orijinali Bozmadan)
print(meyveler[::-1])  # Dilimleme (Slicing) ile tersten yeni liste döndürür

```

<br></br>

### 2. Tuple (Demet)

Tuple'lar, listelere çok benzer ancak en büyük farkları **değiştirilemez** olmalarıdır. Genellikle verilerin güvenli kalması ve kazara değiştirilmemesi istendiğinde tercih edilir.

* **Sıralıdır (Ordered):** Elemanlar belirli bir sıraya göre dizilir.
* **Değiştirilemezdir (Immutable):** Oluşturulduktan sonra eleman eklenemez, silinemez veya mevcut bir elemanın değeri değiştirilemez.
* **Yinelenen Eleman Barındırabilir (Allows Duplicates):** Aynı elemandan birden fazla içerebilir.
* **Tanımlama:** Normal parantez `()` ile tanımlanır. Tek elemanlı oluştururken virgül şarttır: `(5,)`

<br>

#### Yerleşik Tuple Metotları (Built-in Methods)
---

Tuple'lar değiştirilemez oldukları için listelerdeki gibi yapıyı bozan veya güncelleyen metotlara sahip değillerdir. Veri aramak ve bilgi almak için sadece **iki adet** yerleşik metodu vardır:

* **`count(değer)`**: Belirtilen değerin tuple içinde kaç defa geçtiğini sayar.
* **`index(değer)`**: Belirtilen değere sahip ilk elemanın indeks numarasını döndürür. Aranan değer tuple içinde yoksa hata fırlatır.

    ```python
    notlar = (85, 90, 75, 90, 100)

    print(notlar.count(90))  # Çıktı: 2 (Listede iki tane 90 var)
    print(notlar.index(75))  # Çıktı: 2 (75 değeri 2. indekste)

    ```

#### Ekleme ve Silme İşlemleri (Geçici Çözüm)
---

Tuple'lara doğrudan eleman eklenemez veya silinemez (`append`, `remove` yoktur). Değiştirmek zorundaysanız listeye çevirip işlemleri yapar, ardından geri dönüştürürsünüz:

```python
tup = (1, 2, 4)

gecici = list(tup)
gecici.insert(2, 3)    # Araya 3 eklendi
tup = tuple(gecici)    # Tekrar tuple yapıldı -> (1, 2, 3, 4)

```

#### Yazdırma ve Erişim İşlemleri
---

İndeksleme mantığı listelerle birebir aynıdır.

```python
harfler = ("a", "b", "c", "d")

# 1. Belirli Bir Elemanı Yazdırma
print(harfler[1])      # 1. indeksteki eleman: 'b'

# 2. Toplu Yazdırma
print(harfler)         # ('a', 'b', 'c', 'd')

# 3. Tersten Yazdırma
print(harfler[::-1])           # Dilimleme ile tersten döndürür
print(tuple(reversed(harfler)))# reversed() ile tersten döndürür

```

<br></br>

### 3. Set (Küme)

Matematikteki kümelerle aynı mantıkta çalışır. Benzersiz elemanları saklamak ve küme işlemlerini (kesişim, birleşim, fark vb.) hızlıca ve çok verimli bir şekilde yapmak için idealdir. "Baş, son veya orta" kavramı yoktur.

* **Sırasızdır (Unordered):** Elemanların belirli bir sırası yoktur. Bu nedenle indeksleme (`set[0]`) veya dilimleme yapılamaz.
* **Benzersizdir (Unique):** Aynı elemandan sadece bir tane barındırabilir. Yinelenen elemanlar otomatik olarak temizlenir.
* **Değiştirilebilirdir (Mutable):** Kümeye yeni eleman eklenebilir veya silinebilir. Ancak mevcut bir eleman doğrudan güncellenemez.
* **Tanımlama:** Süslü parantez `{}` ile tanımlanır (Boş set oluştururken `set()` kullanılmalıdır, çünkü boş `{}` bir sözlük belirtir).

<br>

> #### 💡 Önemli Detay: Set Çıktılarında Sıralama Neden Değişir? (Hash Randomization)
> 
> 
> Python'da `set`'ler sırasız (unordered) yapılar olduğu için ekrana yazdırıldıklarında elemanların sırası tahmin edilemez.
> **Neden Oluyor?**
> `list` ve `dict` sıralı yapılardır (Python 3.7+'dan itibaren `dict` de eklenme sırasını korur), ama `set` hiçbir zaman sıra garantisi vermez. Bir set'in elemanları, senin eklediğin sıraya göre değil, elemanların **hash değerine** göre iç belleğe yerleştirilir. Yani `{'Hello', 'Kocaeli!'}` ve `{'Kocaeli!', 'Hello'}` aslında *tamamen aynı set'tir* — sadece `print()` onu ekrana basarken hangi eleman önce gelirse onu yazıyor ve bu senin kontrolünde değil.
> **Neden Bazen Değişiyor, Bazen Değişmiyor?**
> Python'da string'lerin hash değeri, güvenlik amacıyla (hash collision saldırılarını önlemek için) her process başlatıldığında rastgele bir tuzla (salt) hesaplanır — buna **hash randomization** denir (`PYTHONHASHSEED`). Bu yüzden:
> * Aynı programı iki farklı çalıştırmada (örneğin `python3 Hello.py` komutunu iki kez çalıştırdığında), string'lerin hash değerleri değişebilir.
> * Hash değeri değişince, set içindeki elemanların iç sıralaması da değişebilir.
> * Bu da `print()` çıktısındaki eleman sırasının çalıştırmadan çalıştırmaya farklı görünmesine yol açar.
> 
> 
> **Bunun Projeyle/Ödevle İlgisi Var Mı?**
> Hayır, bu bir hata değil, tamamen beklenen ve doğru davranıştır. Proje (Subject) yönergelerindeki beklenen çıktıda örneğin `{'Hello', 'Paris!'}` şeklinde gösterilmiş olabilir ama bu sadece bir örnektir. Değerlendirici/hoca da senin çıktında sıra `{'Kocaeli!', 'Hello'}` çıksa bile bunu yanlış saymaz, çünkü set'in matematiksel olarak elemanları aynıdır (`{'Hello', 'Kocaeli!'} == {'Kocaeli!', 'Hello'}` → `True`).
> Eğer sırayı sabitlemek isteseydin `list` veya `tuple` kullanman gerekirdi, ama subject zaten burada özellikle `set` istediği için bu davranışı tamamen kabul ediyor.

#### Yerleşik Set Metotları (Built-in Methods)
---

Kümelerdeki metotları kullanım amaçlarına göre dört ana kategoriye ayırabiliriz:

**1. Temel Ekleme, Silme ve Kopyalama İşlemleri:**

* **`add(eleman)`**: Kümeye tek bir eleman ekler. Eleman zaten varsa hiçbir şey yapmaz.
* **`remove(eleman)`**: Belirtilen elemanı kümeden siler. Eğer eleman kümede **yoksa `KeyError` hatası fırlatır.**
* **`discard(eleman)`**: Belirtilen elemanı kümeden siler. `remove`'dan farkı; eleman kümede **yoksa hata vermez**, sessizce çalışmaya devam eder.
* **`pop()`**: Kümeden **rastgele** bir elemanı siler ve bu sildiği elemanı döndürür. (Kümeler sırasız olduğu için hangisinin silineceği bilinemez).
* **`clear()`**: Kümenin içini tamamen boşaltır (`set()`).
* **`copy()`**: Orijinal kümeyi bozmadan üzerinde bağımsız işlemler yapabilmek için kümenin sığ bir kopyasını (shallow copy) oluşturur.

**2. Matematiksel Küme İşlemleri (Yeni Küme Döndürenler):**
Bu metotlar orijinal kümeleri değiştirmez, işlemin sonucunu **yeni bir küme** olarak verir.

* **`union(*others)`**: Birleşim. İki veya daha fazla kümedeki tüm benzersiz elemanları birleştirip yeni bir küme verir. (Matematikteki $A \cup B$)
* **`intersection(*others)`**: Kesişim. Kümelerin sadece ortak olan elemanlarından oluşan yeni bir küme verir. (Matematikteki $A \cap B$)
* **`difference(*others)`**: Fark. Birinci kümede olup, diğer küme(ler)de olmayan elemanları verir. (Matematikteki $A \setminus B$)
* **`symmetric_difference(other)`**: Simetrik Fark. İki kümenin kesişimleri (ortak elemanları) dışındaki tüm farklı elemanlarını birleştirip verir.

    ```python
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    print(A.union(B))                # Çıktı: {1, 2, 3, 4, 5, 6}
    print(A.intersection(B))         # Çıktı: {3, 4}
    print(A.difference(B))           # Çıktı: {1, 2} (A'da olup B'de olmayanlar)
    print(A.symmetric_difference(B)) # Çıktı: {1, 2, 5, 6} (Ortak olan 3 ve 4 hariç hepsi)

    ```

**3. Güncelleme Metotları (Yerinde Değiştirenler):**
Sonunda `_update` yazan metotlar yeni bir küme oluşturmaz, işlemi yapar ve **orijinal kümeyi kalıcı olarak günceller**. Ayrıca `update` metodu da bu gruptadır.

* **`update(*others)`**: `union` işleminin yerinde yapılan halidir. Diğer kümedeki (veya yinelenebilirdeki) elemanları doğrudan mevcut kümeye ekler.
* **`intersection_update(*others)`**: Orijinal kümeyi, sadece diğer küme ile ortak olan elemanları kalacak şekilde günceller.
* **`difference_update(*others)`**: Diğer kümede de bulunan ortak elemanları, orijinal kümenin içinden kalıcı olarak siler.
* **`symmetric_difference_update(other)`**: Orijinal kümeyi sadece iki kümenin birbirinde olmayan elemanlarını içerecek şekilde günceller.

    ```python
    A = {1, 2, 3}
    B = {3, 4, 5}

    A.update(B)             # A kümesini kalıcı olarak günceller. 
    print(A)                # Çıktı: {1, 2, 3, 4, 5}

    C = {10, 20, 30}
    D = {20, 30, 40}
    C.difference_update(D)  # C'nin içinden D'de de olanları (20, 30) siler.
    print(C)                # Çıktı: {10}

    ```

**4. Mantıksal Sorgu İşlemleri (True / False Döndürenler):**
İki küme arasındaki ilişkiyi sorgulamak için kullanılırlar.

* **`isdisjoint(other)`**: İki kümenin kesişimi boş mu? (Yani hiç ortak elemanları yok mu?) Eğer hiç ortak eleman yoksa `True`, en az 1 ortak eleman varsa `False` döner.
* **`issubset(other)`**: Alt kümesi mi? Mevcut kümenin tüm elemanları, diğer kümenin de içinde var mı diye bakar.
* **`issuperset(other)`**: Kapsayan küme mi? (Üst küme mi?). Mevcut küme, diğer kümenin tüm elemanlarını kendi içinde barındırıyor mu diye bakar.

    ```python
    x = {1, 2}
    y = {1, 2, 3, 4}
    z = {5, 6}

    print(x.issubset(y))   # True (x, y'nin alt kümesidir)
    print(y.issuperset(x)) # True (y, x'i kapsar)
    print(x.isdisjoint(z)) # True (x ve z'nin hiç ortak noktası, yani kesişimi yoktur)

    ```

<br></br>

### 4. Dictionary (Sözlük / Dict)

Verileri **Anahtar-Değer (Key-Value)** çiftleri halinde saklamak için kullanılır. Gerçek hayattaki sözlükler gibi, bir kelimeyi (Key) aratıp karşılığındaki tanımı (Value) bulma mantığıyla çalışır. Veritabanı işlemleri, API'ler (JSON formatı) ve hızlı veri erişimi için Python'daki en önemli yapılardan biridir.

* **Anahtarlar Benzersizdir (Unique Keys):** Bir sözlükte aynı anahtar isminden iki tane bulunamaz. (Eklerseniz eskisinin üzerine yazar). Anahtarlar değiştirilemez veri tiplerinden (string, integer, tuple) olmalıdır. Değerler (Values) ise her şey olabilir.
* **Değiştirilebilirdir (Mutable):** Yeni anahtar-değer çiftleri eklenebilir, mevcut değerler güncellenebilir veya silinebilir.
* **Sıralıdır (Ordered):** Python 3.7 ve sonrası için sözlükler elemanların eklenme sırasını korur.
* **Tanımlama:** Süslü parantez `{}` içinde `anahtar: değer` biçiminde tanımlanır.

#### Yerleşik Sözlük Metotları (Built-in Methods)

Sözlük metotlarını ne işe yaradıklarına göre 4 temel gruba ayırabiliriz:

**1. Veri Okuma ve Erişim İşlemleri:**

* **`get(anahtar, varsayılan)`**: Sözlükten güvenli bir şekilde değer okumak için kullanılır. Köşeli parantez `sozluk["olmayan_anahtar"]` kullanımında anahtar yoksa program `KeyError` verip çöker. Ancak `get()` kullanırsanız hata vermez, anahtar yoksa `None` (veya sizin belirlediğiniz varsayılan değeri) döndürür.
* **`keys()`**: Sözlükteki sadece **anahtarları** (keys) bir liste benzeri yapı halinde döndürür.
* **`values()`**: Sözlükteki sadece **değerleri** (values) döndürür.
* **`items()`**: Sözlükteki verileri **(anahtar, değer) ikilileri** (tuple) halinde döndürür. Döngülerde çok işe yarar.

    ```python
    kisi = {"ad": "Ali", "yas": 25, "meslek": "Mühendis"}

    print(kisi.get("yas"))               # Çıktı: 25
    print(kisi.get("maas", "Bilinmiyor"))# Çıktı: Bilinmiyor (Hata vermez!)

    print(kisi.keys())   # dict_keys(['ad', 'yas', 'meslek'])
    print(kisi.values()) # dict_values(['Ali', 25, 'Mühendis'])
    print(kisi.items())  # dict_items([('ad', 'Ali'), ('yas', 25), ...])

    ```

**2. Ekleme ve Güncelleme İşlemleri:**

* **`update(diger_sozluk)`**: Orijinal sözlüğü, içine verdiğiniz başka bir sözlükteki (veya key-value ikililerindeki) verilerle günceller. Aynı anahtarlar varsa değerlerini yeniler, olmayan anahtarları sona ekler.
* **`setdefault(anahtar, varsayılan)`**: Çok pratik bir metottur. Eğer belirttiğiniz anahtar sözlükte **varsa**, mevcut değere hiç dokunmaz ve o değeri döndürür. Eğer **yoksa**, belirttiğiniz varsayılan değerle birlikte sözlüğe yeni bir kayıt olarak ekler.

    ```python
    ayarlar = {"tema": "koyu", "ses": 50}

    # update kullanımı
    ayarlar.update({"ses": 100, "dil": "TR"}) 
    print(ayarlar) # Çıktı: {'tema': 'koyu', 'ses': 100, 'dil': 'TR'}

    # setdefault kullanımı
    ayarlar.setdefault("tema", "açık") # 'tema' zaten var, değiştirmeyecek.
    ayarlar.setdefault("bildirim", True) # 'bildirim' yoktu, sözlüğe ekledi!

    ```

**3. Silme İşlemleri:**

* **`pop(anahtar, varsayılan)`**: Belirtilen anahtarı ve onun değerini sözlükten **siler** ve sildiği değeri geri döndürür. Anahtar yoksa hata verir (ancak 2. bir parametre olarak varsayılan mesaj yazarsanız hata vermez).
* **`popitem()`**: Sözlüğe **en son eklenen** anahtar-değer çiftini (LIFO mantığıyla) siler ve bunu bir tuple (demet) olarak döndürür.
* **`clear()`**: Sözlüğün içindeki tüm verileri silerek tamamen boşaltır (`{}`).

    ```python
    sepet = {"elma": 5, "armut": 3, "muz": 2}

    silinen_elma = sepet.pop("elma")     # 'elma'yı siler. (silinen_elma = 5 olur)
    son_eklenen = sepet.popitem()        # En son giren 'muz'u siler. -> ('muz', 2)
    sepet.clear()                        # Sepeti boşaltır -> {}

    ```

**4. Kopyalama ve Oluşturma İşlemleri:**

* **`copy()`**: Orijinal sözlüğü bozmadan üzerinde çalışabilmek için sığ bir kopyasını (shallow copy) oluşturur.
* **`fromkeys(yinelenebilir, deger)`**: Belirli anahtarlardan oluşan ve hepsinin başlangıç değeri aynı olan yeni bir sözlük yaratmak için kullanılır. (Toplu sözlük iskeleti oluşturmaya yarar).

    ```python
    orijinal = {"a": 1, "b": 2}
    yedek = orijinal.copy() # Bağımsız bir kopya

    # fromkeys kullanımı (Hepsinin notu baştan 0 olarak ayarlandı)
    ogrenciler = ["Ali", "Ayşe", "Mehmet"]
    not_defteri = dict.fromkeys(ogrenciler, 0)
    print(not_defteri) # Çıktı: {'Ali': 0, 'Ayşe': 0, 'Mehmet': 0}

    ```

#### Yazdırma ve Erişim İşlemleri (Özet)

```python
araba = {"marka": "Ford", "model": "Mustang", "yil": 1964}

# 1. Belirli Bir Elemanı Yazdırma
print(araba["marka"])          # Çıktı: Ford (Ama anahtar yoksa KeyError verir)
print(araba.get("renk", "Yok"))# Güvenli yazdırma (Yoksa 'Yok' yazar)

# 2. Döngü ile Estetik Toplu Yazdırma (items kullanarak)
for anahtar, deger in araba.items():
    print(f"{anahtar.capitalize()}: {deger}")
    
# 3. Tersten Yazdırma (Python 3.8+ destekler)
# Sözlüklerin eklenme sırasını tersine çevirmek için reversed() kullanılabilir:
for anahtar in reversed(araba):
    print(anahtar, araba[anahtar])

```

<br></br>

### Özet Karşılaştırma Tabloları

**Temel Özellikler**

| Veri Yapısı | Sıralı mı? (Ordered) | Değiştirilebilir mi? (Mutable) | Yinelenen Eleman? (Duplicates) | Temel Kullanım Amacı |
| ----------- | -------------------- | ------------------------------ | ------------------------------ | -------------------- |
| **List**    | Evet        | Evet  | İzin Verir           | Genel amaçlı veri saklama, dinamik listeler.        |
| **Tuple**   | Evet        | Hayır | İzin Verir           | Sabit veriler, veri güvenliği, performans avantajı. |
| **Set**     | Hayır       | Evet  | İzin Vermez          | Benzersiz eleman yönetimi, küme matematiği.         |
| **Dict**    | Evet (3.7+) | Evet  | Sadece Değerler İçin | İlişkisel veriler, hızlı erişim (Key-Value).        |

<br></br>

**İşlem Karşılaştırmaları**

| İşlem                       | List                    | Tuple                  | Set                   | Dict                    |
| --------------------------- | ----------------------- | ---------------------- | --------------------- | ----------------------- |
| **Başa / Ortaya Ekleme**    | `insert(indeks, veri)`  | Yok (Listeye çevir)    | Yok (Sırasız)         | Yok (Anahtar bazlı)     |
| **Sona Ekleme**             | `append(veri)`          | Yok (Listeye çevir)    | `add(veri)`           | `dict[key] = value`     |
| **Belirli Eleman Silme**    | `pop(indeks)`, `remove` | Yok                    | `remove`, `discard`   | `pop(key)`              |
| **Belirli Eleman Yazdırma** | `liste[indeks]`         | `tup[indeks]`          | Yok (`in` ile aranır) | `dict[key]`, `get(key)` |
| **Tersten Yazdırma**        | `[::-1]`, `reverse()`   | `[::-1]`, `reversed()` | Yok (Sırasız)         | `reversed()` (v3.8+)    |

<br></br>

