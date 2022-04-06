# Karma Sürü Simülasyon Projesi

Öncelikle gerekli paketleri yükleyin

```sh
$ pip install -r requirements.txt
```

### Çalıştırmak için

`src` klasörünün içindeki main.py yi çalıştırmanız yeterli. Oyun kendiliğinden başlayacak

### Yeni simülasyon ortamı versyona geçerken

- sim klasörünü silip yerine yeni versyonu koyun
- Sdk klasörünün içine boş bir \_\_init\_\_.py dosyası oluşturun. (Bu bir paket olarak görmemizi ve farklı klasörlerden erişmemizi sağlayacak)
- Sdk klasörü içindeki python dosyalarındaki relative importları

```py
import cmd_interop
```

relatif modül importuna dönüştürün

```py
from . import cmd_interop
```
