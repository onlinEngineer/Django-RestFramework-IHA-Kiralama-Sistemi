
# Django-RestFramework-IHA-Kiralama-Sistemi

Django ile İHA Kiralama Projesi




 


## Kullanılan Teknolojiler

- Python
- Django
- Postgresql
- Rest Framework
- PgAdmin4


  
## Özellikler

- Üyelik ve Giriş Ekranları
- Kiralanacak İHA için; Ekleme, Silme, Güncelleme, Listeleme, Kiralama
   + İHA Özellikleri: Marka, Model, Ağırlık, Kategori vb.
-Üyelerin İHA kiralama kayıtları
- Kiralanan İHA için; Kiralamayı Silme, Güncelleme, Listeleme
   + Kiralama Özellikleri: İHA, Tarih ve Saat Aralıkları, Kiralayan Üye vb.
- Tüm Listeleme sayfaları için tabloda filtreleme ve arama özellikleri
- Admin sayfası bulunmaktadır.
- Login olmak zorunluluğu bulunmaktadır.
- Kullanıcı izinleri bulunmaktadır. Normal bir kullanıcı admin sayfalarına erişememektedir.
## Bilgisayarınızda Çalıştırın

Projeyi klonlayın (Windows)

```bash
git clone https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi.git
.\.venv\Scripts\activate
cd ApiProject

```
Projeyi başlat

```bash
python manage.py runserver
```

Kullanıcılar (SuperUser)
Eğer ihakiralama.sql kullanacaksanız aşağıdaki admin ile login olabilirsiniz.

```bash

Admin kullanıcı username: admin
Şifre: admin123

```


API Linkleri
```bash
http://127.0.0.1:8000/api/iha/
http://127.0.0.1:8000/api/kirala/
http://127.0.0.1:8000/api/users/

```




Sayfa Linkleri
```bash
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/register/
http://127.0.0.1:8000/login/
http://127.0.0.1:8000/home/
http://127.0.0.1:8000/iha-list/
http://127.0.0.1:8000/kira-list/
http://127.0.0.1:8000/user-list/
http://127.0.0.1:8000/user-kiralama/
```

Database Bilgileri
```bash

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ihakiralama',
        'USER':'postgres',
        'PASSWORD':'admin',
        'HOST':'localhost',
        'PORT':'5432'
    }
}

```


## Ekran Görüntüleri
### Register Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/603a24ca-b858-4811-8101-78b4f5ae73aa">

### Login Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/287df9d0-3ed3-4d73-96f6-15c125bd284b">

### Admin User Management
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/afeccfcd-fef0-43b8-bbc7-23973732dc2f">

### Admin Home Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/8ec47096-d967-4a71-8f11-ff7f584e2827">

### Admin İha CRUD Management
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/8d2f7b47-427c-4a93-b0d9-ac00cb1466fa">

### Admin Kiralama CRUD Management
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/5358b2d8-5acb-4274-ab90-0cebda32d84d">

### Admin Kiralama Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/278faa79-c167-42c2-af5e-6f2af03b7228">

### Admin Users Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/763415df-9b36-4494-bebf-92b31ddd6df1">

### User Home Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/67aa4611-807c-40ef-bb8e-bb36fffe1ac3">

### User Kiralama Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/d246727d-48d9-45d2-896f-ecb2fa7abf5c">

  
## Ekler

- Listeleme sayfaları için datatable kullanıldı
- İlişkisel tabloların ayrı ayrı tutulmaktadır.
- Django için ekstra kütüphaneler kullanıldı.
- Ön yüzde (Front-End) Bootstrap, Jquery, Ajax vs. kullanılmıştır.
