# Error Handling

- [AssertionError & try-except](#assertionerror--try-except)
    - [assert Kullanımı ve Mantığı](#assert-kullanımı-ve-mantığı)
    - [Hata Fırlatma (`raise`) ve Yakalama (`try/except`) Mekanizması](#hata-fırlatma-raise-ve-yakalama-tryexcept-mekanizması)
    - [Örnek Uygulama](#örnek-uygulama)
    - [Özetle Neden `if` Yerine `assert`?](#özetle-neden-if-yerine-assert)

<br></br>

## `AssertionError` & `try-except`

Kodun belirli bir noktasında bir şartın kesinlikle doğru olması gerektiği varsayımıdır. Eğer o şart doğru değilse, program "Burada beklenmedik bir durum var" diyerek güvenli bir şekilde durdurulur.

Bu yaklaşım, kodun sessizce yanlış çalışmasını engeller ve sorunların kaynağında tespit edilmesini sağlar.

<br>

### `assert` Kullanımı ve Mantığı

Python'da bir koşulun doğruluğunu iddia etmek için `assert` anahtar kelimesi kullanılır. `assert` ifadesi özünde şu anlama gelir: *"Bu koşulun her zaman doğru olmasını bekliyorum, eğer değilse bir şeyler ciddi anlamda yanlıştır."*

**Kullanım Şablonu:**
`assert koşul, "Hata Mesajı"`

Eğer belirttiğiniz koşul `False` olursa, Python otomatik olarak bir `AssertionError` fırlatır ve yazdığınız mesajı hatanın içine yerleştirir.

<br>

### Hata Fırlatma (`raise`) ve Yakalama (`try/except`) Mekanizması

Yazılım standartlarında ve katı değerlendirme sistemlerinde (örneğin *moulinette* gibi test araçlarında) kural şudur: **Hiçbir exception (istisna) yakalanmadan kalmamalı, hepsi kontrol altında olmalıdır.**

Eğer bir `AssertionError` fırlatılır ve siz bunu yakalamazsanız, program terminale kırmızı ve karmaşık sistem hata izleme (traceback) mesajları basarak çöker. İstenen şey programın çökmesi değil, hatanın şablona uygun ve temiz bir şekilde ekrana yazdırılmasıdır.

Bunu yapmak için `AssertionError` hatasını ya `assert` ile otomatik olarak ya da `if` koşulu ve `raise` anahtar kelimesi ile manuel olarak fırlatıp, `try/except` bloğu ile yakalamalıyız.

<br>

#### Örnek Uygulama

Aşağıdaki kod, komut satırından birden fazla argüman girilmesini engelleyen senaryoyu her iki yöntemi de göstererek ele alır:

```python
import sys

def main():
    try:
        # Senaryo: Kullanıcı birden fazla argüman girdi (program adı hariç)
        
        # YÖNTEM 1: assert kullanarak (Kısa ve okunaklı)
        assert len(sys.argv) <= 2, "more than one argument is provided"
        
        # YÖNTEM 2: raise kullanarak (Manuel kontrol alternatifi)
        # if len(sys.argv) > 2:
        #     raise AssertionError("more than one argument is provided")

    except AssertionError as error:
        # Fırlatılan hata nesnesi 'error' takma adıyla yakalanır.
        # Sistem çökme mesajları yerine sadece hata mesajı temizce ekrana basılır.
        print(f"AssertionError: {error}")

if __name__ == "__main__":
    main()

```

<br>

### Özetle Neden `if` Yerine `assert`?

* **Niyetin Belli Olması:** `if` genellikle programın normal akışındaki farklı senaryoları (dallanmaları) yönetmek için kullanılır. `assert` ise doğrudan "bu kesinlikle böyle olmalı, yoksa devam edemeyiz" mesajı verir.
* **İstenen Çıktı:** Görev yönergeleri açıkça *"print an AssertionError"* istiyorsa, bu mekanizmayı doğrudan `assert` (veya `raise AssertionError`) kullanarak kurmak, beklentiyi eksiksiz karşılamanın en doğru yoludur.