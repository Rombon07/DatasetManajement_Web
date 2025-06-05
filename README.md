# 📊 Dataset Management Web App

Web aplikasi manajemen dataset berbasis Django + Bootstrap 5 yang memungkinkan pengguna untuk:
- Mengunggah dataset (CSV/XLSX) beserta deskripsi dan gambar cover
- Melihat pratinjau isi dataset secara langsung
- Melakukan pengelolaan dataset (edit, hapus, lihat detail)
- Melacak histori unduhan dataset
- Menyediakan visualisasi data langsung dari file yang diunggah

---

## ✨ Fitur Utama

✅ **Autentikasi Pengguna**  
- Sistem login & register sederhana  
- Dataset terikat pada pemilik akun  

✅ **CRUD Dataset**  
- Unggah nama, deskripsi, file CSV/XLSX, dan gambar cover  
- Edit dan hapus dataset milik sendiri  
- Validasi dan pratinjau sebelum menyimpan  

✅ **Pratinjau & Visualisasi**  
- Tampilkan isi file dataset (5–10 baris pertama) dalam bentuk tabel  
- Visualisasi otomatis: Bar Chart & Boxplot dari data numerik  

✅ **Tracking Aktivitas**  
- Log pengguna yang mendownload dataset  
- Statistik unduhan per dataset  

✅ **API Publik (optional)**  
- Endpoint sederhana untuk akses dataset oleh aplikasi eksternal  

---

## 🛠️ Teknologi

- **Backend**: Django 5  
- **Frontend**: Bootstrap 5 + Django Template  
- **Database**: SQLite (bisa diganti PostgreSQL)  
- **Visualisasi**: Matplotlib, Pandas  
- **Media Storage**: File lokal (cover image dan data file)  

---

## 🚀 Cara Menjalankan

1. **Clone Repo**
   ```bash
   git clone https://github.com/username/dataset-management.git
   cd dataset-management
   pip install pandas
   pip install matplotlib
   pip install pyplot
   pip install xhtml2pdf

