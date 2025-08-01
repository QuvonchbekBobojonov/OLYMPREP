### 📂 Loyiha haqida

Bu loyiha Django asosida yaratilgan web ilovadir. Loyiha `Python`, `Django`, va boshqa zamonaviy kutubxonalar yordamida tuzilgan.

---

### 🚀 Talablar

Quyidagi dasturlar o‘rnatilgan bo‘lishi kerak:

* Python `3.10+`
* pip
* PostgreSQL (yoki boshqa DB, agar loyihada ishlatilgan bo‘lsa)
* Git (ixtiyoriy)

---

### 🛠 O‘rnatish bosqichlari

#### 1. Repository-ni klonlash

```bash
git clone https://github.com/QuvonchbekBobojonov/OLYMPREP.git
cd OLYMPREP
```

#### 2. Virtual muhit yaratish va faollashtirish

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

#### 3. Kerakli kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

#### 4. `.env` faylini yaratish (agar kerak bo‘lsa)

```env
DEBUG=True
SECRET_KEY=your_secret_key
```

#### 5. Ma'lumotlar bazasini tayyorlash

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6. Superuser yaratish

```bash
python manage.py createsuperuser
```

#### 7. Serverni ishga tushurish

```bash
python manage.py runserver
```

Brauzeringizda quyidagi manzilga o'ting:

```
http://127.0.0.1:8000/
```

---

### 📁 Muhim kataloglar

* `config/`: Asosiy Django konfiguratsiyasi
* `apps/`: Django ilovalari
---

### 📞 Bog‘lanish

Muallif: Quvonchbek Bobojonov
Email: [hi@moorfo.uz](mailto:hi@moorfo.uz)
Website: [moorfo.uz](https://moorfo.uz)
phone: [+998 77 404 0066 ](tel:+998774040066) 
