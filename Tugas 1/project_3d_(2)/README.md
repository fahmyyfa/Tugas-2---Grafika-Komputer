# 🚀 Proyek Roket 3D

## 🎯 Deskripsi

Model ini merupakan representasi **roket mainan 3D** yang dibangun dari bentuk dasar 3D dengan transformasi geometri dan ditampilkan menggunakan Plotly melalui Pyodide langsung di browser.

## 🧱 Komponen

1. **Kerucut (kepala roket)** – warna biru
2. **Silinder (badan roket)** – warna merah
3. **Balok (sayap roket)** – 3 buah, warna hijau
4. **Torus (hiasan donat)** – warna oranye
5. **Bola (jendela roket)** – warna cyan

## 🔄 Transformasi

Setiap objek mengalami translasi, rotasi, dan/atau skala untuk membentuk komposisi yang utuh.

## 🧩 Struktur Scene Graph

Objek disusun secara hierarkis:

- Roket (root)
  - Badan
  - Kepala
  - Sayap (3)
  - Torus dekoratif
  - Jendela (bola)

## 🚀 Menjalankan Proyek

1. Unggah folder ke itch.io (mode HTML).
2. Buka `index.html` di browser.
3. Visualisasi interaktif akan muncul.

## 📦 Dependencies

- Python 3 (via Pyodide)
- Plotly
- NumPy
