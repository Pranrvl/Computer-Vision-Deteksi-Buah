# 🍏 Frutta AI — Sistem Deteksi Kesegaran Buah

Aplikasi web klasifikasi kualitas dan kesegaran komoditas buah (Apel, Pisang, dan Jeruk) berbasis **Deep Learning Convolutional Neural Network (CNN)** dengan antarmuka dasbor **Streamlit**.

---

## 🛠️ Teknologi & Alat yang Digunakan (Tech Stack)

Aplikasi ini tidak hanya menggunakan Streamlit, tetapi merupakan integrasi dari berbagai teknologi pemrosesan data, citra digital, dan arsitektur *deep learning*:

| No | Komponen / Teknologi | Versi / Keterangan | Fungsi Utama dalam Sistem |
|---|---|---|---|
| 1 | **Python** | v3.12 | Bahasa pemrograman utama untuk seluruh backend, logika komputasi, dan integrasi modul. |
| 2 | **Streamlit** | v1.58+ | Framework web interaktif untuk membangun antarmuka pengguna (UI), *file uploader*, tombol interaksi, dan manajemen *session state*. |
| 3 | **NumPy** | v2.4+ | Mesin komputasi matriks/tensor untuk menjalankan inferensi CNN secara mandiri (*pure-NumPy engine* via `im2col`), operasi pooling, aljabar linier, dan analisis morfologi. |
| 4 | **Pillow (PIL)** | v12.2+ | Pustaka pengolahan citra digital untuk membaca berkas foto, standardisasi ruang warna ke 3-saluran RGB, dan *resize* citra ke ukuran 128×128 piksel. |
| 5 | **h5py** | v3.16+ | Pustaka pembaca struktur data biner HDF5 untuk mengekstrak bobot terlatih model (`model.weights.h5`) secara langsung tanpa dependensi runtime TensorFlow. |
| 6 | **HTML5 & CSS3** | Custom | Kustomisasi tampilan dasbor modern, tata letak kartu responsif, tipografi Google Fonts (*Plus Jakarta Sans*), serta penegakan tema terang (*strict light mode*). |
| 7 | **Base64 & BytesIO** | Bawaan Python | Modul konversi citra langsung dari memori RAM menjadi string data Base64 agar dapat dirender ke tag `<img>` tanpa membuat berkas sampah di penyimpanan disk. |
| 8 | **Arsitektur Model CNN (Keras)** | 11 Lapisan Sequential | Model jaringan saraf tiruan terlatih untuk mengekstrak pola visual buah dan mengklasifikasikan ke 6 kategori output. |

---

## 🔬 Spesifikasi Arsitektur Model AI

Model menggunakan arsitektur **Convolutional Neural Network (CNN) Sequential** dengan resolusi input $128 \times 128 \times 3$:

1. **Input Layer**: Citra RGB ukuran $128 \times 128 \times 3$.
2. **Rescaling Layer**: Normalisasi nilai intensitas piksel $[0, 255] \to [0.0, 1.0]$ dengan faktor $1/255.0$.
3. **Blok Konvolusi 1**: `Conv2D(32 filter, kernel 3x3)` + `ReLU` + `MaxPooling2D(2, 2)`.
4. **Blok Konvolusi 2**: `Conv2D(64 filter, kernel 3x3)` + `ReLU` + `MaxPooling2D(2, 2)`.
5. **Blok Konvolusi 3**: `Conv2D(128 filter, kernel 3x3)` + `ReLU` + `MaxPooling2D(2, 2)`.
6. **Flatten Layer**: Meratakan matriks fitur berdimensi $14 \times 14 \times 128$ menjadi vektor 25.088 elemen.
7. **Dense Layer 1**: 128 unit dengan aktivasi `ReLU` + regularisasi `Dropout(0.5)`.
8. **Dense Output Layer**: 6 unit dengan fungsi aktivasi `Softmax` untuk menghasilkan distribusi probabilitas absolut.

### 6 Kategori Kelas yang Didukung:
1. `Fresh Apple` 🍏 (Apel Segar)
2. `Fresh Banana` 🍌 (Pisang Segar)
3. `Fresh Orange` 🍊 (Jeruk Segar)
4. `Rotten Apple` 🍂 (Apel Busuk)
5. `Rotten Banana` 🍂 (Pisang Busuk)
6. `Rotten Orange` 🍂 (Jeruk Busuk)

---

## 📁 Struktur Berkas Proyek

```text
best_model.keras (1)/
├── app.py                  # PUSAT APLIKASI: Antarmuka Streamlit, routing, dan orkestrasi visual
├── model_engine.py         # MESIN INFERENSI: Eksekusi CNN murni NumPy & analisis mutu permukaan
├── model.weights.h5        # BOBOT TERLATIH: File biner HDF5 berisi parameter bobot CNN (39,7 MB)
├── config.json             # BLUEPRINT: Konfigurasi arsitektur resmi model Keras
├── run_app.bat             # PELUNCUR INSTAN: File batch Windows untuk menjalankan aplikasi sekali klik
├── test_model.py           # PENGUJIAN: Skrip otomatis validasi akurasi 6 kelas sampel
├── README.md               # DOKUMENTASI: Panduan lengkap dan ringkasan teknologi
├── .streamlit/
│   └── config.toml         # Konfigurasi server lokal Streamlit dan tema baku
├── .vscode/
│   └── settings.json       # Konfigurasi path interpreter Python untuk editor VS Code
└── samples/                # FOLDER SAMPEL: 6 citra uji standar untuk demonstrasi instan
    ├── demo_green_apple.jpg
    ├── demo_fresh_banana.jpg
    ├── demo_fresh_orange.jpg
    ├── demo_rotten_apple.jpg
    ├── demo_rotten_banana.jpg
    └── demo_rotten_orange.jpg
```

---

## 🚀 Cara Menjalankan Aplikasi

1. **Cara Praktis (Sekali Klik)**:
   Klik ganda berkas `run_app.bat` pada File Explorer Anda.

2. **Cara Manual (Terminal / Command Prompt)**:
   Buka terminal di dalam folder proyek, lalu jalankan:
   ```bash
   python -m streamlit run app.py
   ```
   Aplikasi akan otomatis terbuka pada peramban web di alamat: `http://localhost:8501`.
