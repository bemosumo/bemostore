# Bemostore
[Toko Topup Azur Lane BEMOSTORE](http://muhammad-fawwaz35-bemostore.pbp.cs.ui.ac.id)

sebuah web topup oleh Muhammad Fawwaz E.F.S dengan NPM 2306275582

<details>
<summary> <b> Tugas 2: Implementasi Model-View-Template (MVT) pada Django </b> </summary>
    
# Penjelasan Implementasi
### 1. Membuat Proyek Django Baru
Saya memulai dengan membuat repositori baru di github dengan nama bemostore, kemudian saya menduplikat repositori tersebut ke dalam file lokal. Selanjutnya saya membuat proyek django baru yang kemudian menghasilkan struktur folder utama Django, yaitu `bemostore/`. Di sini, Django secara otomatis menghasilkan file konfigurasi dasar seperti `settings.py`, `urls.py`, dan lainnya.

Perintah yang digunakan:  
```
django-admin startproject myproject
```
### 2. Membuat Aplikasi Dengan Nama `Main`
Setelah proyek utama dibuat, saya menambahkan aplikasi baru bernama `main`. Aplikasi ini akan menjadi tempat utama untuk menyimpan logika bisnis, model, views, dan template.

Perintah yang digunakan:
```bash
python manage.py startapp main
```

Selanjutnya, saya menambahkan aplikasi main ke daftar aplikasi yang terinstall (INSTALLED_APPS) di dalam settings.py, sehingga Django mengenali aplikasi ini.
### 3. Routing Proyek untuk Menjalankan Aplikasi `main`
Pada langkah ini, saya mengatur `urls.py` untuk memetakan permintaan (request) ke aplikasi `main`. Saya memodifikasi `bemostore/urls.py` agar menggunakan routing dari aplikasi `main`.

Perintah yang digunakan:
```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```
### 4. Membuat Model Product
Di aplikasi main, saya mendefinisikan sebuah model Product di `models.py` yang memiliki atribut `name`, `price`, dan `description`. Model ini akan merepresentasikan tabel di database yang menyimpan produk dengan detail lengkap.

Model `Product`:
```bash
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()  
```
Setelah mendefinisikan model, saya melakukan migrasi untuk membuat tabel di database menggunakan perintah:
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Membuat Fungsi View dan Template HTML
Di dalam `views.py`, saya membuat fungsi bernama `show_main` yang akan dikembalikan ke template HTML. Fungsi ini mengirimkan context berupa nama aplikasi, nama, npm, dan kelas saya. Template HTML ini dirender untuk menampilkan informasi tersebut di browser.

`views.py`:
```bash
from django.shortcuts import render

def show_main(request):
    context = {
        'name_aplikasi': 'bemostore',
        'name': 'Muhammad Fawwaz Edsa Fatin Setiawan',
        'npm' : '2306275582',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
```
Di direktori `main/templates`, saya membuat file `main.html` yang akan menerima context dari `views` dan menampilkan data tersebut dalam format HTML.

main.html:
```bash
<h1>{{name_aplikasi}}</h1>

<h5>Name: </h5>
<p>Muhammad Fawwaz Edsa Fatin Setiawan</p> <!--Ubah sesuai dengan nama kamu -->
<h5>NPM: </h5>
<p>2306275582</p> <!-- Ubah sesuai dengan npm kamu -->
<h5>Class: </h5>
<p>PBP D</p> <!-- Ubah sesuai dengan kelas kamu -->
```
### 6. Routing untuk View home
Selanjutnya saya membuat routing di `main/urls.py` untuk memetakan URL ke fungsi `main`. Di sini saya memastikan bahwa URL root ('/') diarahkan ke fungsi `main` di `views.py`.

Routing di main/urls.py:
```bash
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

### 7. Deployment ke Pacil Web Service (PWS)
Terakhir saya melakukan deployment aplikasi ke Pacil Web Service, platform yang memungkinkan untuk hosting aplikasi secara online.

Langkah-langkah deployment:
  1. Upload Proyek: Pertama buat repository baru di PWS. kemudian Proyek Django di upload ke PWS menggunakan Git untuk clone repositori.
  2. Konfigurasi Web App: Menambahkan URL `muhammad-fawwaz35-bemostore.pbp.cs.ui.ac.id` ke dalam `ALLOWED_HOST` pada `settings.py` agar pws dapat menunjuk ke proyek Django
  4. Tes Deployment: Saya memastikan bahwa aplikasi berjalan dengan baik di URL yang disediakan oleh Pacil Web Service.
### 8. Aplikasi Siap Dijalankan
Aplikasi dapat diakses melalui URL http://muhammad-fawwaz35-bemostore.pbp.cs.ui.ac.id

# Bagan Proses _Request Client_ ke Aplikasi
![bagan](images/bagan.png)
### Penjelasan 
Pertama, user akan mengirimkan HTTP request yang kemudian akan di-handle oleh View. Untuk mengetahui apa yang diminta dan bagaimana respon yang akan diberikan, hal ini diatur di dalam urls.py. Berdasarkan pola URL yang diminta, akan ditentukan function View mana di views.py yang akan dijalankan. View akan meminta data yang dibutuhkan dari model sesuai dengan yang sudah didefinisikan dalam function View tersebut, dengan mengambil data yang tersedia di models.py. Selanjutnya, View akan meminta berkas HTML untuk diisi dengan data yang diperoleh, dan pemilihan berkas HTML ini juga sudah ditentukan di dalam function View. Setelah itu, berkas HTML yang sudah diisi data akan dikirim kembali ke user dalam bentuk HTTP response.

# Fungsi `git` dalam Pengembangan Perangkat Lunak
`git` adalah sistem pengontrol versi yang berfungsi untuk melacak perubahan kode dalam pengembangan perangkat lunak, memfasilitasi kolaborasi antar pengembang, dan memungkinkan pengelolaan versi proyek dengan mudah. `git` mendukung pembuatan cabang (branch) untuk pengembangan fitur atau perbaikan bug secara terpisah, yang kemudian dapat digabungkan kembali tanpa risiko konflik. Selain itu, `git` memberikan backup otomatis melalui repositori pusat, memungkinkan rollback ke versi sebelumnya, serta mencatat riwayat perubahan dan kontribusi tiap pengembang, menjadikannya alat penting untuk produktivitas, kolaborasi, dan keamanan dalam pengembangan perangkat lunak.

# Mengapa Django Digunakan sebagai Permulaan Pembelajaran?
Karena framework ini mudah dipahami, memiliki dokumentasi lengkap, dan mengikuti prinsip "batteries included," di mana banyak fitur sudah tersedia tanpa perlu instalasi tambahan. Django menggunakan pola arsitektur yang jelas, yaitu Model-View-Template (MVT), yang memudahkan pemahaman tentang alur kerja aplikasi web. Selain itu, Django memberikan keamanan bawaan dan mendukung praktik terbaik dalam pengelolaan database, routing, dan rendering template.

# Mengapa Model di Django Disebut sebagai ORM?
Disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara objek Python dan tabel di database relasional. ORM memungkinkan pengembang bekerja dengan data dalam bentuk objek Python, sehingga mereka bisa melakukan operasi database seperti mengambil, menyimpan, atau menghapus data tanpa menulis kueri SQL secara langsung. ORM secara otomatis mengonversi operasi objek Python menjadi perintah SQL yang sesuai, memudahkan interaksi dengan database dan membuat kode lebih bersih serta mudah dipahami. 
</details>

<details>
<summary> <b> Tugas 3: Implementasi Form dan Data Delivery pada Django </b> </summary>

# Pentingnya Data Delivery dalam Platform

Data delivery penting dalam platform untuk memastikan komunikasi yang efektif antar komponen seperti server, klien, dan basis data. Proses ini memungkinkan pertukaran informasi yang tepat, misalnya dalam aplikasi web di mana server mengirimkan data (seperti JSON) ke klien. Tanpa mekanisme ini, interaksi antara komponen tidak akan berjalan optimal, menyebabkan kinerja platform menurun.

# Perbandingan XML dan JSON serta Popularitas JSON

JSON lebih populer daripada XML karena lebih sederhana, ringan, dan mudah diproses, terutama di JavaScript. JSON menggunakan sintaks yang lebih ringkas dibandingkan XML yang memakai tag panjang. Selain itu, JSON lebih cepat diparsing dan didukung secara luas oleh berbagai bahasa pemrograman. XML tetap berguna untuk struktur data kompleks, namun JSON lebih efisien untuk pertukaran data modern.

# Fungsi `is_valid()` pada Form Django

Method `is_valid()` di Django memvalidasi data yang diinput dalam form. Jika data valid, method ini mengembalikan `True`, memungkinkan data diproses lebih lanjut. Jika tidak, pesan kesalahan ditampilkan. Fungsi ini penting untuk menjaga data yang masuk tetap konsisten dan aman, serta menghindari input yang berbahaya atau salah.

# Pentingnya `csrf_token` pada Form di Django

`csrf_token` melindungi aplikasi Django dari serangan CSRF, di mana penyerang mencoba mengirim permintaan tidak sah atas nama pengguna. Token ini memastikan bahwa setiap permintaan form datang dari sumber yang tepercaya. Tanpa `csrf_token`, aplikasi rentan terhadap serangan yang bisa mengakibatkan perubahan data atau tindakan tidak diinginkan.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

### 1. Buat sebuah file `base.html` pada folder baru bernama `templates` pada direktori utama
```bash
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

### 2. Menambahkan baris pada variabel `TEMPLATES` di `settings.py` agar `base.html` terbaca
```bash
...
TEMPLATES :
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
...
```

### 3. Tambahkan import uuid di `models.py` dan Lakukan Migration
import uuid
Kemudian, buat model yang menggunakan UUID, misalnya:

```bash
from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()  
```
Setelah mengedit model, jalankan migrasi dengan perintah:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Buat file `forms.py` untuk Mengambil Data dari `models.py`
```bash
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```

### 5. Membuat file baru pada direktori `main/template` untuk tampilan dalam menambahkan item baru dengan nama `create_product_entry.html` 
```bash
{% extends 'base.html' %}
{% block content %}
<h1>Add New Product</h1>

<form method="post">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr> 
            <td>
                <input type="submit" value="Add Product" \>
            </td>
        </tr>
    </table>
</form>
{% endblock content %}
```

### 6. Menambahkan fungsi pada `views.py` dan memodifikasi fungsi di dalamnya
```bash
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    product_entries = Product.objects.all()

    context = {
        'name_aplikasi': 'bemostore',
        'name': 'Muhammad Fawwaz Edsa Fatin Setiawan',
        'npm' : '2306275582',
        'class': 'PBP D',
        'product_entries': product_entries
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### 7. Menambahkan routing url pada `urls.py` pada views yang telah ditambahkan
```bash
from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

# Mengakses keempat URL di poin 2 menggunakan Postman
### 1. XML 
![XML](images/XML.png)
### 2. JSON
![JSON](images/JSON.png)
### 3. HTML
![HTML](images/HTML.png)
### 4. XML by ID
![XML by ID](images/XML_by_ID.png)
### 5. JSON by ID
![JSON by ID](images/JSON_by_ID.png)

</details>

<details>
<summary> <b> Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django </b> </summary>
    
# Perbedaan antara `HttpResponseRedirect()` dan `redirect()` dalam Django:
- `HttpResponseRedirect()`: Sebuah kelas di Django yang mengirimkan respons HTTP dengan kode status 302 (redirect). Biasanya, kita harus memberikan URL secara manual ke `HttpResponseRedirect`. 

- `redirect()`: Fungsi ini adalah shortcut yang lebih nyaman daripada `HttpResponseRedirect`. Fungsi `redirect()` akan secara otomatis menangani URL, termasuk menerima nama tampilan (view name) atau objek model dan mengarahkan pengguna ke halaman yang tepat.

 Dengan kata lain, `redirect()` adalah pembungkus di atas `HttpResponseRedirect`, yang lebih fleksibel dan mudah digunakan karena tidak hanya menerima URL tetapi juga nama view atau objek.

# Cara kerja penghubungan model `Product` dengan `User`:
Untuk menghubungkan model `Product` dengan `User`, biasanya kita menggunakan `ForeignKey` atau `ManyToManyField` dalam model Django. Misalnya, kita dapat memiliki hubungan "satu ke banyak" (one-to-many) di mana satu pengguna bisa memiliki banyak produk, tetapi setiap produk hanya dimiliki oleh satu pengguna.

   Contoh model:

   ```python
    ...
       owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Hubungan dengan User
    ...
   ```

Dalam contoh ini:
- Model `Product` memiliki `ForeignKey` ke model `User`, yang artinya setiap produk dimiliki oleh seorang pengguna. Field `owner` menghubungkan produk dengan pengguna yang memiliki produk tersebut.
- Jika pengguna dihapus, maka produk-produk yang dimilikinya juga akan dihapus berkat opsi `on_delete=models.CASCADE`.

# Perbedaan antara authentication dan authorization:
- **Authentication**: Proses memverifikasi identitas pengguna, misalnya memeriksa apakah username dan password cocok dengan yang ada di database.
- **Authorization**: Proses memeriksa izin atau hak akses pengguna, yaitu menentukan apakah pengguna yang telah diotentikasi (authenticated) memiliki hak untuk melakukan tindakan tertentu (misalnya, mengakses halaman admin).

**Saat pengguna login**, yang dilakukan pertama kali adalah proses *authentication* (pemeriksaan kredensial). Jika berhasil, pengguna diizinkan untuk masuk ke aplikasi. Setelah itu, *authorization* terjadi saat aplikasi memeriksa hak akses pengguna untuk fitur atau halaman tertentu.

**Implementasi di Django**:
- *Authentication* di Django biasanya dilakukan dengan sistem login bawaan (`django.contrib.auth`) yang memverifikasi username dan password pengguna.
- *Authorization* dilakukan menggunakan mekanisme izin dan kelompok (permissions and groups) yang ada dalam model pengguna. Dengan cara ini, Django mengelola apa yang dapat diakses oleh setiap pengguna setelah mereka terotentikasi.

# **Bagaimana Django mengingat pengguna yang telah login?**
Django menggunakan **session** untuk mengingat pengguna yang telah login. Setelah pengguna berhasil login, Django akan menyimpan informasi sesi di server (biasanya dalam database) dan menambahkan cookie ke browser pengguna yang berisi ID sesi. Setiap kali pengguna melakukan permintaan baru, browser mengirimkan cookie ini, dan Django akan mencocokkannya dengan data sesi di server untuk mengidentifikasi pengguna yang telah login.

**Kegunaan lain dari cookies:**
- Cookies digunakan untuk melacak sesi pengguna (misalnya, di e-commerce, untuk keranjang belanja).
- Digunakan untuk menyimpan preferensi pengguna, seperti tema atau bahasa.
- Digunakan oleh layanan pihak ketiga (seperti Google Analytics) untuk pelacakan dan analisis.

**Apakah semua cookies aman digunakan?**
Tidak semua cookies aman. Cookies bisa saja digunakan untuk serangan seperti *session hijacking* atau *cross-site scripting (XSS)*. Oleh karena itu, penting untuk:
- Menggunakan **Secure Cookies** (hanya dikirim melalui HTTPS).
- Menggunakan **HttpOnly Cookies** (yang tidak dapat diakses oleh JavaScript, sehingga meminimalkan risiko XSS).
- Mengatur **SameSite Cookies** untuk membatasi pengiriman cookies lintas situs.

#  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
### 1. Membuat fungsi register 
Menambahkan fungsi `register` pada `views.py` dan membuat tampilannya dengan membuat `register.html` pada `\main\template`
fungsi register pada `views.py` :
``` bash
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
`regisster.html`
```bash
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
### 2. Membuat fungsi login 
Menambahkan fungsi `login_user` pada `views.py` untuk login user yang telah registrasi dan membuat tampilannya dengan membuat `login.html` pada `\main\template`
login pada `views.py`
```bash
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
`login.html`
```bash
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
### 3. Mmebuat fungsi logout
Menambahkan fungsi `logout_user` pada `views.py` untuk logout user yang sedang login dan membuat tampilan tombol logout pada `main.html`.
```bash
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
tombol logout pada `main.html`
```bash
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
### 4. Menambahkan URL untuk setiap fungsi yang telah dibuat
```bash
    ...
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    ...
```
### 5. Menghubungkan product dengan user
Menambahkan field baru berupa `user` pada `models.py` agar masing-masing user dapat melihat product yang telah dibuat.
``` bash
    ...
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    ...
```
Jalankan migrasi
```
python manage.py makemigrations
python manage.py migrate
```
### 6. Menampilkan detail pengguna yang sedang login dan waktu sesi terakhir login
menambahkan detail pengguna pada `views.py` yang menampilkan nama pengguna yang sudah login terlebih dahulu
```bash
    @login_required(login_url='/login')
    ...
    'name': request.user.username,
    'last_login': request.COOKIES['last_login'],
    ...
```
### 7. Menampilkan sesi login terakhir pengguna pada `main.html`
```bash
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

</details>
