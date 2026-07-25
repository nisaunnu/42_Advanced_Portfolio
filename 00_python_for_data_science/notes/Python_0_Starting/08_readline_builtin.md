# `readline` & Building program

- [Kullanıcıdan Input Alma ve "Carriage Return" Detayı](#kullanıcıdan-input-alma-ve-carriage-return-detayı)
- [Karakter Kategorileri Nasıl Belirlenir?](#karakter-kategorileri-nasıl-belirlenir)

<br></br>

## Kullanıcıdan Input Alma ve "Carriage Return" Detayı

Subject'teki ex05 egzersizinde önemli bir not var:

> *"the carriage return counts as a space, if you don't want to
> return one use ctrl + D"*

Bunun anlamı: kullanıcı input yazıp **Enter**'a bastığında, o
**Enter tuşu bir `\n` (newline) karakteri üretir** ve bu karakter de
string'in bir parçası olarak sayılmalı — yani boşluk (`space`)
kategorisine dahil edilmeli.

Bu yüzden `input()` fonksiyonunu **kullanmıyoruz** — çünkü `input()`
otomatik olarak sondaki `\n` karakterini siler (strip eder). Onun
yerine `sys.stdin.readline()` kullanıyoruz; bu fonksiyon satırı
**newline dahil** okur.

Örnek:

```python
print("What is the text to count?")
text = sys.stdin.readline()
```

- Kullanıcı `Hello World!` yazıp Enter'a basarsa:
  `text = "Hello World!\n"` → 13 karakter (12 + 1 newline), 2 space
  (1 orijinal + 1 newline). Subject'teki beklenen çıktı **tam olarak
  bu**:

  ```
  The text contains 13 characters:
  2 upper letters
  8 lower letters
  1 punctuation marks
  2 spaces
  0 digits
  ```

- Kullanıcı **Ctrl+D** ile (hiç yazı yazmadan) direkt EOF (End Of
  File) sinyali gönderirse, `readline()` boş string (`""`) döner —
  newline eklenmez, çünkü Enter'a hiç basılmamıştır.

**Özet:** `\n` karaktere fiziksel olarak var olduğu için
`char.isspace()` onu `True` olarak görür ve boşluk sayacına dahil
eder — bu bilinçli bir tasarım tercihi, hata değil.

<br></br>

## Karakter Kategorileri Nasıl Belirlenir?

Python string'lerinin, her karakter için kategorisini sorgulamaya
yarayan hazır (built-in) metotları var:

| Metot            | Ne zaman `True` döner?                     |
| ---------------- | ------------------------------------------- |
| `char.isupper()` | Karakter büyük harfse (`A-Z` gibi)          |
| `char.islower()` | Karakter küçük harfse (`a-z` gibi)          |
| `char.isdigit()` | Karakter bir rakamsa (`0-9`)                |
| `char.isspace()` | Karakter boşluk karakteriyse (` `, `\n`, `\t` vb.) |

**Noktalama işaretleri için** hazır bir `.ispunctuation()` metodu
yoktur. Bunun yerine `string` modülündeki hazır sabiti kullanırız:

```python
import string
string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```

Bir karakterin noktalama işareti olup olmadığını şu şekilde
kontrol ederiz:

```python
if char in string.punctuation:
    punctuation += 1
```

**Önemli:** Kontrol sırası önemli — önce `isupper`, `islower`,
`isdigit`, `isspace` kontrol edilmeli, en son `in string.punctuation`
bakılmalı. Çünkü bazı karakterler (örneğin boşluk) birden fazla
kategoriye "yanlışlıkla" girebilir; `elif` zinciri kullanarak her
karakterin **sadece bir kategoriye** sayılmasını garanti ederiz.
