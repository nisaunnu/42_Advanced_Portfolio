# `main()` ve `__name__` Üzerine Notlar

- [`main()` Fonksiyonu](#main-fonksiyonu)
   - [Nedir?](#nedir)
   - [Neden Kullanılır?](#neden-kullanılır)
   - [Özellikleri](#özellikleri-bu-piscine-bağlamında)
- [`if __name__ == "__main__":` Bloğu](#if-__name__--__main__-bloğu)
   - [Anlamı](#anlamı)
   - [Neden bu şekilde isimlendiriliyor / kullanılıyor?](#neden-bu-şekilde-isimlendiriliyor--kullanılıyor)
   - [Özellikleri](#özellikleri)
- [Özet Şablon](#özet-şablon)

<br></br>

## `main()` Fonksiyonu

### Nedir?
`main()`, bir Python programının **giriş noktası (entry point)** olarak
kullanılan, kendi adını taşıyan sıradan bir fonksiyondur. C, Java gibi
dillerde `main` dilin kendisi tarafından zorunlu tutulur; Python'da ise
bu bir zorunluluk değil, bir **kural/gelenektir** (convention). Biz bu
piscine'de bunu zorunlu kılıyoruz çünkü disiplin kazandırıyor.

<br>

### Neden kullanılır?

- **Global değişken sorununu çözer.** Kodun en üst seviyesinde
  (module/global scope) tanımlanan her değişken "global" sayılır ve
  tüm dosya boyunca her yerden erişilebilir/değiştirilebilir olur. Bu,
  büyük programlarda hangi değişkenin nerede değiştiğini takip etmeyi
  zorlaştırır, hataya açık hale getirir. Kodu `main()` içine almak,
  tüm değişkenleri o fonksiyonun **local (yerel) scope**'una hapseder.

- **Import edilebilirlik sağlar.** Eğer kodun global scope'ta
  (fonksiyon dışında) çalışan satırlar varsa, bu dosya başka bir
  dosyadan `import` edildiği anda o satırlar **otomatik olarak
  çalışır**. Bu genelde istenmeyen bir durumdur — örneğin ex02'de
  `find_ft_type.py` dosyasını `import` ettiğinde sadece fonksiyonu
  kullanmak istiyorsun, dosyanın kendi test kodunun çalışmasını değil.
  `main()` kullanmak buna engel olur (bkz. aşağıdaki bölüm).

- **Test edilebilirlik ve okunabilirlik.** Kodun "ne zaman, nasıl
  çalıştığı" tek bir yerde, açıkça görülür. Fonksiyonun kendi
  docstring'i (`__doc__`) olabilir, böylece `main.__doc__` ile ne işe
  yaradığı da belgelenmiş olur.

<br>

### Özellikleri (bu piscine bağlamında)

1. İçinde **tüm test kodların ve hata yönetimin (error handling)**
   bulunur.
2. Argümansız çağrılır: `def main():` — parametre almasına gerek yok,
   çünkü zaten programın başlangıç noktasıdır.
3. Genellikle bir şey **return etmez** (döndürmez); işini `print()`
   ile ya da başka fonksiyonları çağırarak yapar. Ama zorunlu değil,
   istersen bir exit code da döndürebilirsin.
4. Dosyanın **en altında** tanımlanmaz, üstte tanımlanır; sadece
   *çağrılması* en altta, `if __name__ == "__main__":` bloğunun
   içinde yapılır.
5. Fonksiyon olduğu için, docstring kuralına tabidir —
   `"""Bu fonksiyon şunu yapar."""` şeklinde açıklanmalıdır.

<br></br>

## `if __name__ == "__main__":` Bloğu

### Anlamı

Python, çalıştırdığı her dosyaya (module) otomatik olarak bir
`__name__` adlı özel/dahili (built-in) değişken atar:

- Eğer dosya **doğrudan çalıştırılıyorsa** (`python dosya.py` gibi),
  Python o dosyanın `__name__` değişkenine `"__main__"` string'ini
  atar.
- Eğer dosya **başka bir dosya tarafından import ediliyorsa**
  (`import dosya` gibi), `__name__` değişkenine dosyanın **kendi
  adı** atanır (örneğin `"dosya"`).

Yani `if __name__ == "__main__":` satırı aslında şunu sorar:

> "Bu dosya şu an *doğrudan* mı çalıştırılıyor, yoksa başka bir
> dosyaya *import mu* edildi?"

Eğer cevap "doğrudan çalıştırılıyor" ise, blok içindeki kod
(genellikle sadece `main()` çağrısı) çalışır. Import edilmişse,
çalışmaz.

<br>

### Neden bu şekilde isimlendiriliyor / kullanılıyor?

Bu deyim (idiom) Python'a özgü, çok yaygın bir tasarım desenidir.
Mantığı şudur:

- Bir `.py` dosyası hem **bağımsız bir script** hem de **başka
  kodların import ettiği bir modül** olarak kullanılabilir olmalı.
- Eğer dosyanın en üst seviyesinde (`if` bloğu olmadan) direkt
  `main()` çağrısı olsaydı, o dosya her `import` edildiğinde bu
  çağrı da **istemeden** tetiklenirdi. Bu, özellikle test dosyaları
  (`tester.py`) fonksiyonları import ettiğinde ciddi bir soruna yol
  açar — nitekim subject'te tam olarak bunu görüyoruz:

  > "Running your function alone does nothing." (ex02, ex03)
  >
  > ```
  > $>python find_ft_type.py | cat -e
  > $>
  > ```

  Yani `find_ft_type.py` doğrudan çalıştırıldığında **hiçbir çıktı
  vermemeli** — çünkü test kodu `main()` içinde ve `main()` sadece
  `__name__ == "__main__"` olduğunda çağrılıyor, ama bu dosyanın
  kendi `__name__` değeri de `"__main__"` olduğu için normalde
  çalışırdı... Burada incelik şu: `find_ft_type.py`'nin kendi
  `main()`'i muhtemelen boş ya da hiçbir test çağırmıyor; asıl
  testler `tester.py` içinde, oradan `import find_ft_type` yapılıyor.
  `tester.py` çalıştırıldığında `find_ft_type`'ın `__name__`'i
  `"__main__"` DEĞİL, `"find_ft_type"` olur — dolayısıyla
  `find_ft_type.py`'nin kendi `if __name__ == "__main__":` bloğu
  **tetiklenmez**, sadece `all_thing_is_obj` fonksiyonu kullanılır.

<br>

### Özellikleri

1. Her zaman dosyanın **en altında** yer alır.
2. İçinde genellikle sadece `main()` çağrısı bulunur — başka kod
   konması önerilmez (fazla mantık koymak yerine, o mantığı `main()`
   içine ya da başka fonksiyonlara taşımak daha temizdir).
3. Bu blok olmadan da kod çalışabilir, ama o zaman dosya
   **import edildiğinde de** en alttaki kod tetiklenir — bu genelde
   istenmez.
4. `__name__` bir string olduğu için karşılaştırma `==` ile yapılır,
   `is` ile değil (string identity garantisi olmadığından `==`
   doğru pratik).
5. Bu desen sayesinde bir dosya **hem çalıştırılabilir script hem de
   import edilebilir kütüphane/modül** olabilir — bu piscine'deki
   her `ex0X` dosyasının tam olarak yapması gereken şey budur (bkz.
   Chapter VII: *"Each program must have its main and not be a
   simple script"*).

<br></br>

## Özet Şablon

```python
def main():
    """Programın giriş noktası; testleri ve hata yönetimini içerir."""
    # ... kodun burada ...
    pass


if __name__ == "__main__":
    main()
```