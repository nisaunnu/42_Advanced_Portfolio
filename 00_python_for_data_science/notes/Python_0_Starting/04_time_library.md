# Time Library & f-string

- [Time Kütüphanesi](#time-kütüphanesi)
    - [Temel Kavramlar: Bilgisayarlar Zamanı Nasıl Görür?](#1-temel-kavramlar-bilgisayarlar-zamanı-nasıl-görür)
        - [`time.struct_time`](#timestruct_time-yapısının-bileşenleri)
    - [Temel Fonksiyonlar](#2-temel-fonksiyonlar)
        - [`time.time()`](#timetime)
        - [`time.sleep(secs)`](#timesleepsecs)
    - [Zaman Dönüşüm Fonksiyonları](#3-zaman-dönüşüm-fonksiyonları)
        - [`time.localtime([secs])`](#timelocaltimesecs)
        - [`time.gmtime([secs])`](#timegmtimesecs)
        - [`time.mktime(t)`](#timemktimet)
    - [Zamanı Metne Dönüştürme ve Biçimlendirme](#4-zamanı-metne-dönüştürme-ve-biçimlendirme)
        - [`time.ctime([secs])`](#timectimesecs)
        - [`time.asctime([t])`](#timeasctimet)
        - [`time.strftime(format[, t])`](#timestrftimeformat-t)
        - [`time.strptime(string, format)`](#timestrptimestring-format)
    - [Hassas Performans ve Kod Çalışma Süresi Ölçümü](#5-hassas-performans-ve-kod-çalışma-süresi-ölçümü)
        - [`time.perf_counter()`](#timeperf_counter)
        - [`time.process_time()`](#timeprocess_time)
    - [f-string ile Sayı Biçimlendirme](#6-f-string-ile-sayı-biçimlendirme-string-formatting)


<br></br>

## Time Kütüphanesi

Python'ın yerleşik `time` modülü, zamanla ilgili işlevleri yönetmek, kodun çalışma performansını ölçmek, programları duraklatmak ve zaman verilerini farklı formatlara dönüştürmek için kullanılır.

<br>

### 1. Temel Kavramlar: Bilgisayarlar Zamanı Nasıl Görür?

`time` kütüphanesini tam olarak anlayabilmek için zamanın Python'da temsil edildiği 3 ana biçimi bilmek gerekir:

1. **Epoch Zamanı (Timestamp / Float):** 1 Ocak 1970 saat 00:00:00 (UTC) anından itibaren geçen toplam saniye miktarıdır. Kesirli bir sayı (`float`) olarak tutulur.
2. **Zaman Yapısı (`struct_time`):** Zamanın saniye cinsinden değil; yıl, ay, gün, saat, dakika gibi bileşenlerine ayrılmış halidir. Python'da özel bir adlandırılmış demet (named tuple) yapısındadır.
3. **Okunabilir Metin (String):** `"Sat Jun 13 12:05:00 2026"` veya `"2026-06-13"` gibi insanların doğrudan okuyabildiği metin biçimidir.

Bu üç yapı arasındaki dönüşüm ilişkisi kütüphanenin temelini oluşturur:

#### `time.struct_time` Yapısının Bileşenleri

Bir zaman nesnesi `struct_time` biçimine dönüştürüldüğünde şu 9 indekse/nitelik değerine sahip olur:

| İndeks | Nitelik (Attribute) | Değer Aralığı | Açıklama |
| --- | --- | --- | --- |
| `0` | `tm_year` | Örn: `2026` | 4 haneli yıl bilgisi |
| `1` | `tm_mon` | `1 - 12` | Ay bilgisi |
| `2` | `tm_mday` | `1 - 31` | Ayın günü |
| `3` | `tm_hour` | `0 - 23` | Saat bilgisi |
| `4` | `tm_min` | `0 - 59` | Dakika bilgisi |
| `5` | `tm_sec` | `0 - 61` | Saniye bilgisi (Artık saniyeler dahil) |
| `6` | `tm_wday` | `0 - 6` | Haftanın günü (`0` Pazartesi'dir) |
| `7` | `tm_yday` | `1 - 366` | Yılın kaçıncı günü olduğu |
| `8` | `tm_isdst` | `0, 1, -1` | Gün ışığından yararlanma bilgisi (DST) |

<br></br>

### 2. Temel Fonksiyonlar

#### `time.time()`

Kodun çalıştığı o anki Epoch zamanını saniye cinsinden `float` olarak döndürür.

```python
import time

simdi = time.time()
print(simdi)  # Çıktı örn: 1778663100.4562

```

#### `time.sleep(secs)`

Belirtilen saniye kadar programın çalışmasını askıya alır (durdurur). İçine kesirli sayılar da alabilir.

```python
print("Başladı")
time.sleep(2.5)  # Programı 2.5 saniye duraklatır
print("2.5 saniye sonra devam etti")

```

<br></br>

### 3. Zaman Dönüşüm Fonksiyonları

#### `time.localtime([secs])`

Saniye cinsinden verilen zamanı, **yerel saat dilimine** uygun bir `struct_time` nesnesine dönüştürür. Eğer içine saniye verilmezse, o anki zamanı (`time.time()`) baz alır.

```python
yerel_zaman = time.localtime()
print(yerel_zaman)
# Erişim yöntemi:
print("Yıl:", yerel_zaman.tm_year)
print("Ayın kaçıncı günü:", yerel_zaman.tm_mday)

```

#### `time.gmtime([secs])`

Saniye cinsinden verilen zamanı, Greenwich ortalama saatine (**UTC/GMT saat dilimine**) göre `struct_time` nesnesine dönüştürür. Türkiye yerel saati UTC+3 olduğu için, `gmtime` çıktısı yerel saatten 3 saat geride olacaktır.

```python
gmt_zaman = time.gmtime()
print(gmt_zaman.tm_hour)  # UTC saatini verir

```

#### `time.mktime(t)`

Yerel saatteki bir `struct_time` nesnesini veya 9 elemanlı bir zaman demetini alır, bunu saniye cinsinden Epoch zamanına (`float`) geri dönüştürür. `localtime()` fonksiyonunun tam tersidir.

```python
zaman_demeti = (2026, 6, 13, 12, 5, 0, 5, 164, 0)
saniye_hali = time.mktime(zaman_demeti)
print(saniye_hali)

```

<br></br>

### 4. Zamanı Metne Dönüştürme ve Biçimlendirme

#### `time.ctime([secs])`

Saniye cinsinden zamanı alır ve doğrudan okunabilir, standart bir metne dönüştürür. Parametre verilmezse o anı dönüştürür.

```python
print(time.ctime())  # Çıktı örn: "Sat Jun 13 12:05:00 2026"

```

#### `time.asctime([t])`

Bir `struct_time` nesnesini alır ve tıpkı `ctime` gibi standart bir metne dönüştürür.

```python
zaman_yapisi = time.localtime()
print(time.asctime(zaman_yapisi))  # Çıktı örn: "Sat Jun 13 12:05:00 2026"

```

#### `time.strftime(format[, t])`

Zamanı kendi belirleyeceğimiz şablonlara göre çok esnek bir şekilde biçimlendirmemizi sağlar. Bir `struct_time` nesnesi kabul eder.

| Kod | Açıklama | Örnek |
| --- | --- | --- |
| `%Y` | 4 haneli yıl | `2026` |
| `%m` | 2 haneli ay | `06` |
| `%B` | Ayın tam ismi | `June` |
| `%b` | Ayın kısaltılmış ismi | `Jun` |
| `%d` | Ayın günü | `13` |
| `%H` | 24'lük sistemde saat | `12` |
| `%M` | Dakika | `05` |
| `%S` | Saniye | `00` |
| `%A` | Günün tam ismi | `Saturday` |
| `%a` | Günün kısaltılmış ismi | `Sat` |

```python
su_an = time.localtime()

# Örnek 1: GG/AA/YYYY Formatı
formatli_1 = time.strftime("%d/%m/%Y", su_an)
print(formatli_1)  # Çıktı: "13/06/2026"

# Örnek 2: Saat:Dakika:Saniye ve Gün ismi
formatli_2 = time.strftime("%H:%M:%S - %A", su_an)
print(formatli_2)  # Çıktı: "12:05:00 - Saturday"

```

#### `time.strptime(string, format)`

`strftime` fonksiyonunun tam tersidir. Belirli bir formattaki metni okur (parse eder) ve onu bir Python `struct_time` nesnesine dönüştürür.

```python
tarih_metni = "30-12-2025"
sablon = "%d-%m-%Y"

olusan_zaman = time.strptime(tarih_metni, sablon)
print(olusan_zaman.tm_year)  # Çıktı: 2025

```

<br></br>

### 5. Hassas Performans ve Kod Çalışma Süresi Ölçümü

Kod bloklarının ne kadar sürede çalıştığını ölçmek için asla `time.time()` kullanılmamalıdır; çünkü sistem saati güncellemelerden veya internet senkronizasyonlarından etkilenip ileri/geri zıplayabilir. Bunun yerine dökümantasyonun önerdiği iki özel fonksiyon vardır:

#### `time.perf_counter()`

Sistem genelindeki en yüksek çözünürlüğe sahip kronometreyi (monotonik saat) döndürür. Zaman asla geri gitmez. Kod parçalarının çalışma sürelerini kıyaslamak için ideal yöntemdir.

```python
baslangic = time.perf_counter()

# Ölçülmek istenen kod bloğu
toplam = 0
for i in range(1_000_000):
    toplam += i

bitis = time.perf_counter()
gecen_sure = bitis - baslangic
print(f"Kodun çalışma süresi: {gecen_sure:.6f} saniye.")

```

#### `time.process_time()`

Mevcut programın (prosesin) **CPU üzerinde harcadığı** toplam süreyi saniye cinsinden verir. Kod çalışırken araya giren uyku (`time.sleep`) sürelerini hesaba katmaz; sadece işlemcinin o kod için ne kadar yorulduğunu ölçer.

```python
b_cpu = time.process_time()

time.sleep(2)  # Bu 2 saniyelik durma süresi hesaplamaya dahil edilmez

bit_cpu = time.process_time()
print(f"Harcanan saf CPU süresi: {bit_cpu - b_cpu} saniye.")

```

<br></br>

### 6. f-string ile Sayı Biçimlendirme (String Formatting)

Python'da `f-string` (Formatlı Metinler), sadece değişkenleri metin içine gömmekle kalmaz; sayıların ekranda nasıl görüneceğini (basamak sayılarını, virgüllerini veya bilimsel formatlarını) çok hassas bir şekilde kontrol etmemizi sağlar.

Biçimlendirme mantığı her zaman şu şablonu takip eder: `{değişken:format_kodu}`

<br>

#### 1. Ondalık Basamak Hassasiyeti (`f` Kodu)

Bir `float` (kesirli) sayının virgülden sonra kaç basamağının ekrana yazdırılacağını belirlemek için `.basamak_sayısıf` kalıbı kullanılır. `f` harfi "Fixed-point notation" (Sabit noktalı gösterim) anlamına gelir.

```python
sayi = 123.456789

# Virgülden sonra 2 basamak göster (Sayıyı yuvarlar)
print(f"{sayi:.2f}")  # Çıktı: 123.46

# Virgülden sonra 4 basamak göster
print(f"{sayi:.4f}")  # Çıktı: 123.4568

```

<br>

#### 2. Binlik Taban Ayracı (Virgül `,` Kodu)

Büyük sayıların okunmasını kolaylaştırmak amacıyla binlik basamakların arasına virgül koymak için format kodunun başına `,` eklenir.

```python
buyuk_sayi = 1000000

print(f"{buyuk_sayi:,}")  # Çıktı: 1,000,000

```

<br>

#### 3. Binlik Ayracı ve Ondalık Basamağı Birlikte Kullanma

Hem binlik basamakları virgülle ayırmak hem de virgülden sonra net bir basamak sayısı belirtmek için iki kod birleştirilir: `:, .basamak_sayısıf`

```python
zaman_saniye = 1666355857.362218

# Binlikleri ayır ve virgülden sonra tam 4 basamak göster
print(f"{zaman_saniye:,.4f}")  # Çıktı: 1,666,355,857.3622

```

<br>

#### 4. Bilimsel Gösterim (`e` Kodu)

Çok büyük veya çok küçük sayıları $10$ tabanındaki üslü sayılar şeklinde (Scientific Notation) göstermek için `e` veya `E` harfi kullanılır. Mantık yine aynıdır: `.basamak_sayısıe` kalıbı, katsayının virgülden sonra kaç basamak alacağını belirler.

```python
sayi = 1666355857.3622

# Bilimsel gösterim (Virgülden sonra 2 basamak katsayı ile)
print(f"{sayi:.2e}")  # Çıktı: 1.67e+09
# (Açılımı: 1.67 * 10^9)

# Bilimsel gösterim (Virgülden sonra 4 basamak katsayı ile)
print(f"{sayi:.4e}")  # Çıktı: 1.6664e+09

```

<br></br>