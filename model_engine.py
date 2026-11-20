"""
model_engine.py
Inference engine for Frutta Fruit Freshness AI.
Faithfully implements the exact CNN classification algorithm and classes from DATA_BUAH_COMVIS.ipynb,
equipped with morphological validation to correctly identify out-of-dataset fruit shapes like pears (Pir).
Pure NumPy CNN implementation (fast, zero-dependency, exact Keras weights).
"""

import os
import numpy as np
from PIL import Image
import h5py

# 6 Kelas resmi sesuai DATA_BUAH_COMVIS.ipynb
CLASS_NAMES = [
    'freshapples',
    'freshbanana',
    'freshoranges',
    'rottenapples',
    'rottenbanana',
    'rottenoranges'
]

# Metadata pendukung untuk penyajian hasil yang informatif
CLASS_META = {
    'freshapples': {
        'jenis': 'Apel',
        'kondisi': 'Segar',
        'emoji': '🍎',
        'label_resmi': 'freshapples',
        'nama_lengkap': 'Apel Segar (Fresh Apple)',
        'deskripsi': 'Apel dalam kondisi segar dengan tekstur padat, kulit cerah alami tanpa bintik nekrosis, dan kadar air optimal.',
        'rekomendasi_penyimpanan': 'Simpan pada laci sayur kulkas (suhu 1°C - 4°C) dengan kelembapan 90-95% agar kesegaran dan kerenyahan bertahan 2-3 minggu.',
        'estimasi_simpan': '14 - 21 Hari (Kulkas)'
    },
    'freshbanana': {
        'jenis': 'Pisang',
        'kondisi': 'Segar',
        'emoji': '🍌',
        'label_resmi': 'freshbanana',
        'nama_lengkap': 'Pisang Segar (Fresh Banana)',
        'deskripsi': 'Pisang pada tingkat kematangan optimal, kulit kuning bersih, aroma manis alami, dan daging buah masih kenyal.',
        'rekomendasi_penyimpanan': 'Simpan pada suhu ruang berventilasi (18°C - 22°C). Hindari pendinginan langsung di bawah 12°C agar kulit tidak menghitam dini.',
        'estimasi_simpan': '4 - 7 Hari (Suhu Ruang)'
    },
    'freshoranges': {
        'jenis': 'Jeruk',
        'kondisi': 'Segar',
        'emoji': '🍊',
        'label_resmi': 'freshoranges',
        'nama_lengkap': 'Jeruk Segar (Fresh Orange)',
        'deskripsi': 'Jeruk berkulit kencang, pori-pori flavedo sehat, kadar air tinggi, dan tidak ada indikasi infeksi jamur kapang.',
        'rekomendasi_penyimpanan': 'Simpan pada tempat sejuk berventilasi atau di dalam kulkas (suhu 4°C - 7°C) untuk kesegaran tahan hingga 3-4 minggu.',
        'estimasi_simpan': '14 - 28 Hari (Kulkas)'
    },
    'rottenapples': {
        'jenis': 'Apel',
        'kondisi': 'Busuk',
        'emoji': '🍎',
        'label_resmi': 'rottenapples',
        'nama_lengkap': 'Apel Busuk (Rotten Apple)',
        'deskripsi': 'Terjadi kerusakan jaringan seluler, pencokelatan enzimatik luas (browning), pelunakan daging buah, dan potensi toksin jamur.',
        'rekomendasi_penyimpanan': 'Tidak layak dikonsumsi mentah. Segera pisahkan dari buah lain agar tidak mempercepat pembusukan dan memicu penularan spora.',
        'estimasi_simpan': 'Kadaluarsa / Tidak Layak Konsumsi'
    },
    'rottenbanana': {
        'jenis': 'Pisang',
        'kondisi': 'Busuk',
        'emoji': '🍌',
        'label_resmi': 'rottenbanana',
        'nama_lengkap': 'Pisang Busuk (Rotten Banana)',
        'deskripsi': 'Dinding sel selulosa telah terdegradasi total menjadi lembek. Terjadi fermentasi gula lanjut disertai bau asam menyengat.',
        'rekomendasi_penyimpanan': 'Tidak aman dikonsumsi langsung. Sebaiknya dibuang ke wadah kompos organik.',
        'estimasi_simpan': 'Kadaluarsa / Tidak Layak Konsumsi'
    },
    'rottenoranges': {
        'jenis': 'Jeruk',
        'kondisi': 'Busuk',
        'emoji': '🍊',
        'label_resmi': 'rottenoranges',
        'nama_lengkap': 'Jeruk Busuk (Rotten Orange)',
        'deskripsi': 'Terindikasi penetrasi miselium jamur kapang (Penicillium) atau pembusukan asam basah. Spora jamur aktif menyebar melalui udara.',
        'rekomendasi_penyimpanan': 'Segera buang dalam wadah tertutup rapat. Bersihkan area penyimpanan dengan lap kering desinfektan.',
        'estimasi_simpan': 'Kadaluarsa / Tidak Layak Konsumsi'
    }
}


def analyze_fruit_morphology(pil_img):
    """
    Analisis morfologi bentuk dan deteksi cacat permukaan buah menggunakan Computer Vision.
    Mendeteksi siluet piriformis khas buah Pir (Pear) vs buah bulat (Jeruk/Apel) dan panjang (Pisang).
    """
    img = pil_img.convert('RGB')
    arr = np.array(img)
    
    # Deteksi latar belakang (putih/terang)
    is_white_bg = (arr[:, :, 0] > 230) & (arr[:, :, 1] > 230) & (arr[:, :, 2] > 230)
    if is_white_bg.sum() > (arr.shape[0] * arr.shape[1] * 0.1):
        mask = ~is_white_bg
    else:
        # Fallback jika background gelap
        is_dark_bg = (arr[:, :, 0] < 35) & (arr[:, :, 1] < 35) & (arr[:, :, 2] < 35)
        if is_dark_bg.sum() > (arr.shape[0] * arr.shape[1] * 0.1):
            mask = ~is_dark_bg
        else:
            mask = np.ones(arr.shape[:2], dtype=bool)

    row_widths = mask.sum(axis=1)
    col_heights = mask.sum(axis=0)
    active_rows = np.where(row_widths > 0)[0]
    active_cols = np.where(col_heights > 0)[0]

    if len(active_rows) == 0 or len(active_cols) == 0:
        return {'is_pear': False, 'aspect_ratio': 1.0, 'pyriform_ratio': 1.0, 'blemish_pct': 0.0}

    top, bottom = int(active_rows[0]), int(active_rows[-1])
    left, right = int(active_cols[0]), int(active_cols[-1])
    h = bottom - top + 1
    w = right - left + 1
    aspect_ratio = float(h / max(w, 1))

    # Lebar pada 25% tinggi (bagian leher atas) vs lebar pada 75% tinggi (dasar bawah)
    w_upper = float(row_widths[top + int(h * 0.25)]) if h > 4 else float(w)
    w_lower = float(row_widths[top + int(h * 0.75)]) if h > 4 else float(w)
    pyriform_ratio = float((w_lower + 1) / (w_upper + 1))

    # Analisis bercak nekrosis/pembusukan gelap pada permukaan buah
    fruit_pixels = arr[mask]
    if len(fruit_pixels) > 0:
        r, g, b = fruit_pixels[:, 0], fruit_pixels[:, 1], fruit_pixels[:, 2]
        dark_necrosis = (r < 75) & (g < 55) & (b < 45)
        blemish_pct = float((dark_necrosis.sum() / len(fruit_pixels)) * 100)
    else:
        blemish_pct = 0.0

    # Ciri khas buah Pir (Pyrus): bentuk piriformis vertikal, leher sempit dan dasar melebar.
    # Jeruk selalu bundar (rasio 0.90 - 1.10). Apel biasanya 0.95 - 1.25. Pir >= 1.40.
    is_pear = (aspect_ratio >= 1.12) and (aspect_ratio <= 1.85) and (pyriform_ratio >= 1.40)

    return {
        'is_pear': is_pear,
        'aspect_ratio': round(aspect_ratio, 2),
        'pyriform_ratio': round(pyriform_ratio, 2),
        'blemish_pct': round(blemish_pct, 2)
    }


class FruitModel:
    def __init__(self, weights_path=None):
        if weights_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            candidates = [
                os.path.join(base_dir, 'model.weights.h5'),
                os.path.join(base_dir, 'best_model.keras (1)', 'model.weights.h5'),
                r'C:\Users\pranr\Downloads\best_model.keras\model.weights.h5',
                r'C:\Users\pranr\Downloads\best_model.keras (1)\model.weights.h5'
            ]
            for c in candidates:
                if os.path.exists(c):
                    weights_path = c
                    break

        if weights_path is None or not os.path.exists(weights_path):
            raise FileNotFoundError(f"model.weights.h5 tidak ditemukan pada path: {weights_path}")

        self.weights_path = weights_path
        self._load_weights()

    def _load_weights(self):
        """Memuat seluruh bobot dan bias hasil training dari model.weights.h5."""
        with h5py.File(self.weights_path, 'r') as f:
            self.w_conv1 = f['layers/conv2d/vars/0'][:]
            self.b_conv1 = f['layers/conv2d/vars/1'][:]

            self.w_conv2 = f['layers/conv2d_1/vars/0'][:]
            self.b_conv2 = f['layers/conv2d_1/vars/1'][:]

            self.w_conv3 = f['layers/conv2d_2/vars/0'][:]
            self.b_conv3 = f['layers/conv2d_2/vars/1'][:]

            self.w_dense1 = f['layers/dense/vars/0'][:]
            self.b_dense1 = f['layers/dense/vars/1'][:]

            self.w_dense2 = f['layers/dense_1/vars/0'][:]
            self.b_dense2 = f['layers/dense_1/vars/1'][:]

    @staticmethod
    def _im2col(x, k_h, k_w, stride=1):
        """Optimasi perkalian matriks untuk konvolusi 2D cepat berbasis NumPy."""
        h, w, c = x.shape
        out_h = (h - k_h) // stride + 1
        out_w = (w - k_w) // stride + 1
        shape = (out_h, out_w, k_h, k_w, c)
        strides = (x.strides[0] * stride, x.strides[1] * stride, x.strides[0], x.strides[1], x.strides[2])
        cols = np.lib.stride_tricks.as_strided(x, shape=shape, strides=strides)
        return cols.reshape(out_h * out_w, k_h * k_w * c), out_h, out_w

    def _conv2d(self, x, w, b):
        """Layer Konvolusi 2D + Aktivasi ReLU."""
        k_h, k_w, c_in, c_out = w.shape
        cols, out_h, out_w = self._im2col(x, k_h, k_w)
        w_flat = w.reshape(k_h * k_w * c_in, c_out)
        out = np.dot(cols, w_flat) + b
        out = np.maximum(0, out)  # ReLU
        return out.reshape(out_h, out_w, c_out)

    @staticmethod
    def _maxpool2d(x):
        """Layer MaxPooling 2x2 dengan stride 2."""
        h, w, c = x.shape
        out_h = h // 2
        out_w = w // 2
        x_reshaped = x[:out_h * 2, :out_w * 2, :].reshape(out_h, 2, out_w, 2, c)
        return x_reshaped.max(axis=(1, 3))

    def predict_image(self, image_input):
        """
        Menjalankan inferensi CNN murni NumPy + validasi morfologi Computer Vision.
        Args:
            image_input: file path (str), PIL.Image, atau BytesIO.
        Returns:
            dict hasil klasifikasi lengkap.
        """
        if isinstance(image_input, str):
            pil_img = Image.open(image_input)
        elif isinstance(image_input, Image.Image):
            pil_img = image_input
        else:
            pil_img = Image.open(image_input)

        orig_w, orig_h = pil_img.size

        # Preprocessing sesuai DATA_BUAH_COMVIS.ipynb:
        # 1. Konversi ke RGB
        # 2. Resize ke 128x128
        # 3. Rescaling intensitas piksel 1./255.0
        rgb_img = pil_img.convert('RGB')
        resized_img = rgb_img.resize((128, 128), Image.Resampling.BILINEAR)
        arr = np.asarray(resized_img, dtype=np.float32) * (1.0 / 255.0)

        # -------------------------------------------------------------
        # 1. FORWARD PASS CNN (Persis Arsitektur Keras di Notebook)
        # -------------------------------------------------------------
        x = self._conv2d(arr, self.w_conv1, self.b_conv1)      # Conv 32 (126x126x32)
        x = self._maxpool2d(x)                                 # Pool (63x63x32)

        x = self._conv2d(x, self.w_conv2, self.b_conv2)        # Conv 64 (61x61x64)
        x = self._maxpool2d(x)                                 # Pool (30x30x64)

        x = self._conv2d(x, self.w_conv3, self.b_conv3)        # Conv 128 (28x28x128)
        x = self._maxpool2d(x)                                 # Pool (14x14x128)

        # Flatten (14 * 14 * 128 = 25088)
        x_flat = x.reshape(-1)

        # Dense 128 + ReLU
        dense1 = np.maximum(0, np.dot(x_flat, self.w_dense1) + self.b_dense1)

        # Dense 6 + Softmax
        logits = np.dot(dense1, self.w_dense2) + self.b_dense2
        exp_logits = np.exp(logits - np.max(logits))
        predictions = exp_logits / np.sum(exp_logits)

        # -------------------------------------------------------------
        # 2. ANALISIS MORFOLOGI BENTUK CITRA
        # -------------------------------------------------------------
        morph = analyze_fruit_morphology(pil_img)

        # Output dasar dari CNN
        best_idx = int(np.argmax(predictions))
        predicted_class = CLASS_NAMES[best_idx]
        confidence = float(np.max(predictions) * 100)

        # Distribusi probabilitas seluruh 6 kelas
        all_classes_sorted = []
        for i, cls_name in enumerate(CLASS_NAMES):
            p = float(predictions[i])
            info = CLASS_META[cls_name]
            all_classes_sorted.append({
                'class_name': cls_name,
                'jenis': info['jenis'],
                'kondisi': info['kondisi'],
                'emoji': info['emoji'],
                'nama_lengkap': info['nama_lengkap'],
                'prob': p,
                'prob_pct': round(p * 100, 2),
                'is_fresh': info['kondisi'] == 'Segar',
                'bar_color': '#10b981' if info['kondisi'] == 'Segar' else '#ef4444'
            })
        all_classes_sorted.sort(key=lambda item: item['prob'], reverse=True)

        # -------------------------------------------------------------
        # 3. IDENTIFIKASI CERDAS (MENANGANI BUAH PIR / NON-TARGET)
        # -------------------------------------------------------------
        if morph['is_pear']:
            # Terdeteksi bentuk piriformis khas Pir
            is_pear = True
            jenis = "Pir"
            emoji = "🍐"

            # Kesegaran dinilai dari output CNN dan tingkat lesi permukaan
            if predicted_class.startswith("fresh") and morph['blemish_pct'] < 5.0:
                kondisi = "Segar"
                is_fresh = True
                quality_notes = "Permukaan kulit bersih dan cerah tanpa lesi pembusukan. Terdeteksi bentuk piriformis khas buah Pir."
                storage_tip = "Simpan buah pir pada suhu ruang hingga matang lembut, lalu simpan dalam kulkas (suhu 4°C) untuk kesegaran tahan 1-2 minggu."
                shelf_life = "7 - 14 Hari (Kulkas / Suhu Ruang)"
            else:
                kondisi = "Busuk"
                is_fresh = False
                quality_notes = "Terindikasi bercak nekrosis/pembusukan pada permukaan jaringan buah pir."
                storage_tip = "Buah pir mengalami pembusukan, segera buang dan jangan dikonsumsi."
                shelf_life = "Kadaluarsa / Tidak Layak Konsumsi"

            variety = f"Buah Pir ({'Segar' if is_fresh else 'Busuk'})"
            morphology_note = f"Terdeteksi siluet buah Pir (rasio kontur {morph['pyriform_ratio']:.2f}). Model CNN memetakan kemiripan fitur visual ke {CLASS_META[predicted_class]['nama_lengkap']} ({confidence:.2f}%)."

        else:
            is_pear = False
            # Menentukan jenis buah sesuai notebook
            if "apples" in predicted_class:
                jenis = "Apel"
            elif "banana" in predicted_class:
                jenis = "Pisang"
            else:
                jenis = "Jeruk"

            kondisi = "Segar" if predicted_class.startswith("fresh") else "Busuk"
            is_fresh = (kondisi == "Segar")
            meta = CLASS_META[predicted_class]

            emoji = meta['emoji']
            quality_notes = meta['deskripsi']
            storage_tip = meta['rekomendasi_penyimpanan']
            shelf_life = meta['estimasi_simpan']
            variety = meta['nama_lengkap']
            morphology_note = None

        # Deskriptor tingkat kepastian
        if confidence >= 90.0:
            confidence_level = "Sangat Tinggi (Very High)"
        elif confidence >= 70.0:
            confidence_level = "Tinggi (High)"
        elif confidence >= 50.0:
            confidence_level = "Sedang (Moderate)"
        else:
            confidence_level = "Rendah / Kurang Yakin (Low)"

        return {
            'predicted_class': predicted_class,
            'jenis': jenis,
            'kondisi': kondisi,
            'confidence': confidence,
            'confidence_pct': round(confidence, 2),
            'confidence_level': confidence_level,
            'is_fresh': is_fresh,
            'is_pear': is_pear,
            'morphology': morph,
            'morphology_note': morphology_note,
            'emoji': emoji,
            'fruit_emoji': emoji,
            'fruit': f"{jenis} ({'Apple' if jenis == 'Apel' else ('Banana' if jenis == 'Pisang' else ('Orange' if jenis == 'Jeruk' else 'Pear'))})",
            'condition': kondisi,
            'condition_title': f"{kondisi} ({'Fresh' if is_fresh else 'Rotten'})",
            'condition_sub': "Kualitas Baik • Layak Konsumsi" if is_fresh else "Terkontaminasi • Jangan Dikonsumsi",
            'status_pill': f"{kondisi} / {'Layak Konsumsi' if is_fresh else 'Tidak Layak'}",
            'variety': variety,
            'shelf_life': shelf_life,
            'quality_notes': quality_notes,
            'storage_tip': storage_tip,
            'all_classes_sorted': all_classes_sorted,
            'image_resolution': f"{orig_w} × {orig_h} px",
            'all_probs': {cls: round(float(p) * 100, 2) for cls, p in zip(CLASS_NAMES, predictions)}
        }
