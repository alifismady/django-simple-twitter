

Tahapan menjalankan aplikasi:
1. Buat virtual enviroment dengan command -> "python -m venv venv"
2. Run virtual enviroment pada terminal -> windows: "venv\Scripts\activate.bat"; mac/linux: "source venv/Scripts/activate"
3. Install dependencies yang diperlukan, diletakan pada "requirements.txt" command -> "pip install -r 'requirements.txt'" 
4. Migrate database schema ke SQlite dengan command -> "./manage.py migrate"
5. Jalankan server django dengan command -> "./manage.py runserver"
6. Buka url "localhost:8000" pada terminal untuk membuka server

Aplikasi:
1. Setelah aplikasi di run, visit url "localhost:8000" untuk tiba pada halaman pertama aplikasi, terdapat navbar dimana pengguna dapat login
2. Terdapat textfield yang dapat diisi dengan text untuk mengirim tweet, pengguna terlebih dahulu harus login ke akun sebelum dapat mengirim tweet
3. Tweet yang sudah dikirim dapat diedit atau dihapus oleh pembuat tweet tersebut dengan mengklik tombol yang terdapat pada tweet terkirim
4. Tweet dari setiap pengguna akan ditampilkan pada halaman utama, hanya pemilik tweet yang dapat mengedit atau menghapus tweet mereka
5. Visit url "localhost:8000/admin" untuk mengunjungi django admin site, gunakann command "./manage.py createsuperuser" untuk membuat super user yang dapat login ke site admin
