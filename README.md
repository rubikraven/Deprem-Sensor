# Deprem Tespit Uygulaması

Bu proje, kamera görüntülerini kullanarak anlık deprem tespiti yapan bir Python uygulamasıdır. Uygulama, görüntülerdeki hareketi ölçer ve belirli bir eşik değerinden yüksek hareket tespit ettiğinde "deprem oluyor" uyarısı verir.

## Kullanılan Kütüphaneler

- OpenCV (cv2): Görüntü işleme ve optik akış hesaplamaları için kullanılır.
- NumPy: Bilimsel hesaplamalar ve matematiksel işlemler için kullanılır.
- winsound: Sistem üzerinde ses çalma işlemleri için kullanılır.
- pyttsx3: Metinden sese dönüştürme işlemleri için kullanılır.
- yagmail: E-posta gönderme işlemleri için kullanılır.

## Kurulum

1. Projeyi GitHub'dan indirin veya kopyalayın.
2. Proje dizininde, tüm bağımlılıkları yüklemek için şu komutu çalıştırın: `pip install -r requirements.txt`
3. E-posta gönderme işlemleri için, `main.py` dosyasındaki ilgili satırları kendi e-posta bilgilerinizle ve alıcı e-posta adresiyle güncelleyin.

## Kullanım

1. Terminalde projenin ana dizinine gidin.
2. Uygulamayı şu komutla başlatın: `python main.py`
3. Kameradan alınan görüntülerde hareket tespit edildiğinde, uygulama sesli ve e-posta yoluyla uyarı verecektir.
4. 'q' tuşuna basarak uygulamayı durdurabilirsiniz.

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
