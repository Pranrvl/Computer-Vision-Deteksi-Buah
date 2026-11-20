"""
Frutta Vision - Executive Quality Inspection Dashboard
Sistem Klasifikasi Kesegaran dan Mutu Komoditas Buah Berbasis Deep Learning CNN.
Tampilan Fullscreen modern, profesional, dan elegan.
"""

import os
import base64
from io import BytesIO
from PIL import Image
import streamlit as st
from model_engine import FruitModel

# Path Berkas Logo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_ICON_PATH = os.path.join(BASE_DIR, "logo_icon.png")
LOGO_FULL_LIGHT_PATH = os.path.join(BASE_DIR, "logo_full_light.png")

def get_file_base64(filepath):
    """Membaca berkas gambar lokal dan mengonversinya ke Base64."""
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

logo_icon_b64 = get_file_base64(LOGO_ICON_PATH)
logo_full_b64 = get_file_base64(LOGO_FULL_LIGHT_PATH)

# Favicon Tab Browser (menggunakan ikon logo resmi)
favicon = Image.open(LOGO_ICON_PATH) if os.path.exists(LOGO_ICON_PATH) else "🔬"

# Konfigurasi Halaman Streamlit (Full Wide Layout)
st.set_page_config(
    page_title="Frutta Vision | Inspeksi Mutu Buah",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Model AI (di-cache agar cepat dan hemat memori)
@st.cache_resource(show_spinner=False)
def load_fruit_model():
    return FruitModel()

try:
    model = load_fruit_model()
except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop()


def image_to_base64(pil_image):
    """Konversi citra PIL ke Base64 format JPEG untuk disematkan di HTML."""
    buffered = BytesIO()
    rgb_img = pil_image.convert('RGB')
    rgb_img.save(buffered, format="JPEG", quality=90)
    return base64.b64encode(buffered.getvalue()).decode()


# --------------------------------------------------------------------------------------
# CSS TAMPILAN FULLSCREEN & ENTERPRISE/DEWASA
# --------------------------------------------------------------------------------------
CUSTOM_CSS = """
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<style>
    /* Reset & Tipografi */
    * {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        box-sizing: border-box;
    }
    
    code, .mono-font {
        font-family: 'JetBrains Mono', monospace !important;
    }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }

    /* Sembunyikan elemen bawaan Streamlit yang mengganggu */
    header[data-testid="stHeader"] { display: none !important; }
    footer { display: none !important; }
    #MainMenu { visibility: hidden !important; }
    .stDeployButton { display: none !important; }

    /* Layout Fullscreen Luas & Nyaman */
    .block-container {
        max-width: 100% !important;
        padding-top: 1.25rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 2.5rem !important;
        padding-right: 2.5rem !important;
        margin: 0 !important;
    }

    @media (max-width: 768px) {
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            padding-top: 1rem !important;
        }
    }

    /* Desain Tombol Profesional */
    div[data-testid="stButton"] button {
        background-color: #0f172a !important;
        color: #ffffff !important;
        border: 1px solid #0f172a !important;
        border-radius: 0.5rem !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        padding: 0.6rem 1rem !important;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.08) !important;
        transition: all 0.2s ease !important;
    }
    div[data-testid="stButton"] button:hover {
        background-color: #1e293b !important;
        border-color: #1e293b !important;
        color: #ffffff !important;
        box-shadow: 0 4px 6px -1px rgba(15, 23, 42, 0.12) !important;
    }

    /* Desain Dropzone Upload */
    div[data-testid="stFileUploader"] {
        padding: 0 !important;
        margin-bottom: 0.25rem !important;
    }
    div[data-testid="stFileUploader"] section {
        background-color: #ffffff !important;
        border: 1px dashed #cbd5e1 !important;
        border-radius: 0.75rem !important;
        padding: 1.5rem 1rem !important;
        transition: border-color 0.2s ease;
    }
    div[data-testid="stFileUploader"] section:hover {
        border-color: #0f172a !important;
    }
</style>
"""
st.html(CUSTOM_CSS)

# --------------------------------------------------------------------------------------
# 1. TOP NAVBAR / HEADER ENTERPRISE
# --------------------------------------------------------------------------------------
NAVBAR_HTML = f"""
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e2e8f0; padding-bottom: 1rem; margin-bottom: 1.5rem;">
  <div style="display: flex; align-items: center; gap: 14px;">
    <img src="data:image/png;base64,{logo_icon_b64}" style="width: 40px; height: 40px; object-fit: contain; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.06));" alt="Frutta Logo" />
    <div>
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 19px; font-weight: 800; letter-spacing: -0.02em; color: #0f172a;">FRUTTA VISION</span>
        <span style="font-size: 10.5px; background: #e2e8f0; color: #334155; padding: 2px 7px; border-radius: 9999px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em;">Quality Inspection</span>
      </div>
      <p style="font-size: 12px; color: #64748b; margin: 2px 0 0 0;">Sistem Deteksi Otomatis Mutu & Kesegaran Komoditas Buah Berbasis Deep Learning CNN</p>
    </div>
  </div>
  <div style="display: flex; align-items: center; gap: 16px;">
    <div style="display: flex; align-items: center; gap: 6px; background: #ffffff; border: 1px solid #e2e8f0; padding: 4px 10px; border-radius: 9999px; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">
      <span style="width: 7px; height: 7px; border-radius: 9999px; background: #10b981; display: inline-block;"></span>
      <span style="font-size: 11.5px; font-weight: 600; color: #334155;">Model Online</span>
    </div>
    <div style="font-size: 11.5px; color: #94a3b8; font-weight: 500;">
      Input: 128×128 RGB
    </div>
  </div>
</div>
"""
st.html(NAVBAR_HTML)

# --------------------------------------------------------------------------------------
# 2. INISIALISASI SESI STATE
# --------------------------------------------------------------------------------------
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0
if "last_uploaded_id" not in st.session_state:
    st.session_state.last_uploaded_id = None
if "active_image" not in st.session_state:
    st.session_state.active_image = None
if "image_name" not in st.session_state:
    st.session_state.image_name = None
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

# --------------------------------------------------------------------------------------
# 3. KONDISI TAMPILAN: STATE KOSONG VS HASIL PEMERIKSAAN
# --------------------------------------------------------------------------------------
if st.session_state.active_image is None:
    # TAMPILAN AWAL FULLSCREEN: INPUT DI KIRI, SPESIFIKASI DI KANAN
    col_input, col_info = st.columns([1.1, 1], gap="large")

    with col_input:
        st.html("<div style='font-size: 13px; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;'>Unggah Citra Sampel Buah</div>")
        
        uploaded_file = st.file_uploader(
            label="Pilih atau tarik citra buah ke area ini",
            type=["jpg", "jpeg", "png"],
            key=f"uploader_{st.session_state.uploader_key}",
            help="Format yang didukung: JPG, JPEG, PNG."
        )

        if uploaded_file is not None:
            current_file_id = f"{uploaded_file.name}_{uploaded_file.size}"
            if st.session_state.last_uploaded_id != current_file_id:
                try:
                    loaded_img = Image.open(uploaded_file)
                    st.session_state.last_uploaded_id = current_file_id
                    st.session_state.active_image = loaded_img
                    st.session_state.image_name = uploaded_file.name
                    st.session_state.prediction_result = model.predict_image(loaded_img)
                    st.rerun()
                except Exception as e:
                    st.error(f"Gagal memproses citra: {e}")

        st.html("""
        <div style="margin-top: 0.75rem; font-size: 12px; color: #64748b; line-height: 1.5;">
          <strong>Petunjuk Pengujian:</strong> Pastikan objek buah terlihat jelas dengan pencahayaan yang cukup. Model akan menganalisis fitur morfologi dan tekstur permukaan secara otomatis.
        </div>
        """)

    with col_info:
        INFO_PANEL_HTML = f"""
        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 0.75rem; padding: 1.35rem; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.85rem; padding-bottom: 0.75rem; border-bottom: 1px solid #f1f5f9;">
            <img src="data:image/png;base64,{logo_full_b64}" style="height: 36px; width: auto; object-fit: contain;" alt="Frutta Logo" />
            <span style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em;">Standar Inspeksi</span>
          </div>
          
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.65rem; margin-bottom: 1rem;">
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 0.65rem 0.75rem;">
              <span style="font-size: 10px; font-weight: 700; color: #64748b; text-transform: uppercase; display: block;">Target 1</span>
              <strong style="font-size: 13.5px; color: #0f172a; display: block; margin-top: 2px;">Apel (Apple)</strong>
              <span style="font-size: 11px; color: #64748b;">Segar / Busuk</span>
            </div>
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 0.65rem 0.75rem;">
              <span style="font-size: 10px; font-weight: 700; color: #64748b; text-transform: uppercase; display: block;">Target 2</span>
              <strong style="font-size: 13.5px; color: #0f172a; display: block; margin-top: 2px;">Pisang (Banana)</strong>
              <span style="font-size: 11px; color: #64748b;">Segar / Busuk</span>
            </div>
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 0.65rem 0.75rem;">
              <span style="font-size: 10px; font-weight: 700; color: #64748b; text-transform: uppercase; display: block;">Target 3</span>
              <strong style="font-size: 13.5px; color: #0f172a; display: block; margin-top: 2px;">Jeruk (Orange)</strong>
              <span style="font-size: 11px; color: #64748b;">Segar / Busuk</span>
            </div>
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 0.65rem 0.75rem;">
              <span style="font-size: 10px; font-weight: 700; color: #64748b; text-transform: uppercase; display: block;">Validasi Tambahan</span>
              <strong style="font-size: 13.5px; color: #0f172a; display: block; margin-top: 2px;">Pir (Pear)</strong>
              <span style="font-size: 11px; color: #64748b;">Morfologi Piriformis</span>
            </div>
          </div>

          <div style="border-top: 1px solid #f1f5f9; padding-top: 0.75rem; font-size: 11.5px; color: #475569; line-height: 1.6;">
            <strong>Spesifikasi Engine:</strong> Convolutional Neural Network Sequential (Input 128×128 RGB, 3 Blok Konvolusi, Dropout 0.5, Dense 6 Softmax). Akurasi pengujian 97.41% pada dataset benchmark.
          </div>
        </div>
        """
        st.html(INFO_PANEL_HTML)

else:
    # TAMPILAN DASHBOARD PENUH SAAT CITRA SUDAH TERSEDIA
    pred = st.session_state.prediction_result
    if pred is None or not isinstance(pred, dict) or 'all_classes_sorted' not in pred:
        pred = model.predict_image(st.session_state.active_image)
        st.session_state.prediction_result = pred

    b64_img = image_to_base64(st.session_state.active_image)
    w, h = st.session_state.active_image.size

    col_visual, col_analytics = st.columns([1, 1.45], gap="large")

    # =========================================================================
    # KOLOM KIRI: DOKUMENTASI CITRA & KONTROL
    # =========================================================================
    with col_visual:
        visual_html = f"""
        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 0.75rem; padding: 1.15rem; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <span style="font-size: 12px; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 0.05em;">Dokumentasi Citra Inspeksi</span>
            <span style="font-size: 11px; font-family: monospace; background: #f1f5f9; color: #475569; padding: 2px 6px; border-radius: 4px;">{w}×{h} px</span>
          </div>

          <div style="width: 100%; height: 350px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; padding: 10px; overflow: hidden;">
            <img src="data:image/jpeg;base64,{b64_img}" style="max-width: 100%; max-height: 100%; object-fit: contain; border-radius: 4px;" alt="Citra Buah" />
          </div>

          <div style="margin-top: 0.75rem; display: flex; justify-content: space-between; align-items: center; font-size: 11.5px; color: #64748b;">
            <span>Berkas: <strong>{st.session_state.image_name}</strong></span>
            <span>Rasio Aspek: <strong>{w/max(h,1):.2f}</strong></span>
          </div>
        </div>
        """
        st.html(visual_html)

        # Tombol Ganti Citra
        st.html("<div style='height: 0.5rem;'></div>")
        if st.button("✕ Unggah Citra Lain", key="btn_reset_full", use_container_width=True):
            st.session_state.uploader_key += 1
            st.session_state.last_uploaded_id = None
            st.session_state.active_image = None
            st.session_state.image_name = None
            st.session_state.prediction_result = None
            st.rerun()

    # =========================================================================
    # KOLOM KANAN: TELEMETRI & HASIL EVALUASI DEWASA/PROFESIONAL
    # =========================================================================
    with col_analytics:
        is_fresh = pred.get('is_fresh', True)
        is_pear = pred.get('is_pear', False)
        jenis = pred.get('jenis', 'Apel')
        kondisi = pred.get('kondisi', 'Segar')
        confidence = pred.get('confidence_pct', 0.0)
        predicted_class = pred.get('predicted_class', '-')
        saran = pred.get('storage_tip', '-')
        shelf_life = pred.get('shelf_life', '-')
        morph_note = pred.get('morphology_note')

        # Banner Status Eksekutif (Tema Segar vs Defect)
        if is_fresh:
            status_bg = "#ecfdf5"
            status_border = "#a7f3d0"
            status_text_color = "#065f46"
            status_title = f"● STATUS MUTU: SEGAR (PRIMA) — {jenis.upper()}" if is_pear else f"● STATUS MUTU: SEGAR (PRIMA)"
            status_sub = "Karakteristik visual memenuhi standar kelayakan konsumsi dan distribusi. Tidak terdeteksi dekomposisi biologis."
        else:
            status_bg = "#fef2f2"
            status_border = "#fecdd3"
            status_text_color = "#991b1b"
            status_title = f"● STATUS MUTU: DEFECT (BUSUK) — {jenis.upper()}" if is_pear else f"● STATUS MUTU: DEFECT (BUSUK)"
            status_sub = "Terdeteksi nekrosis jaringan seluler atau pembusukan aktif. Komoditas tidak direkomendasikan untuk konsumsi."

        # Rincian probabilitas 6 kelas (Sleek Spectrum Progress Bars)
        prob_bars_html = ""
        for item in pred.get('all_classes_sorted', []):
            is_winner = item['class_name'] == predicted_class
            f_weight = "700" if is_winner else "500"
            t_color = "#0f172a" if is_winner else "#64748b"
            bar_w = max(item['prob_pct'], 1.0)
            
            prob_bars_html += f"""
            <div style="margin-bottom: 7px;">
              <div style="display: flex; justify-content: space-between; font-size: 11.5px; font-weight: {f_weight}; color: {t_color}; margin-bottom: 2px;">
                <span>{item['nama_lengkap']}</span>
                <span class="mono-font" style="font-weight: 600;">{item['prob_pct']:.2f}%</span>
              </div>
              <div style="width: 100%; height: 5px; background: #e2e8f0; border-radius: 9999px; overflow: hidden;">
                <div style="width: {bar_w}%; height: 100%; background: {item['bar_color']}; border-radius: 9999px;"></div>
              </div>
            </div>
            """

        # Callout Catatan Morfologi Khusus Pir
        morph_box_html = ""
        if morph_note:
            morph_box_html = f"""
            <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 0.5rem; padding: 0.65rem 0.85rem; font-size: 11.5px; color: #166534; line-height: 1.5;">
              <strong>ℹ️ Catatan Validasi Morfologi:</strong> {morph_note}
            </div>
            """

        dashboard_html = f"""
        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 0.75rem; padding: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 0.95rem;">
          
          <!-- Executive Status Banner -->
          <div style="background: {status_bg}; border: 1px solid {status_border}; border-radius: 0.5rem; padding: 0.85rem 1.15rem;">
            <div style="font-size: 15px; font-weight: 800; color: {status_text_color}; letter-spacing: -0.01em;">
              {status_title}
            </div>
            <div style="font-size: 12px; color: {status_text_color}; margin-top: 3px; line-height: 1.4;">
              {status_sub}
            </div>
          </div>

          <!-- 4 KPI Parameter Grid -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.65rem;">
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 0.65rem 0.75rem;">
              <span style="font-size: 10px; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; display: block;">Komoditas</span>
              <strong style="font-size: 14.5px; color: #0f172a; display: block; margin-top: 2px;">{jenis}</strong>
            </div>
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 0.65rem 0.75rem;">
              <span style="font-size: 10px; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; display: block;">Kondisi Mutu</span>
              <strong style="font-size: 14.5px; color: {'#166534' if is_fresh else '#991b1b'}; display: block; margin-top: 2px;">{kondisi}</strong>
            </div>
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 0.65rem 0.75rem;">
              <span style="font-size: 10px; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; display: block;">Confidence</span>
              <strong class="mono-font" style="font-size: 14.5px; color: #0f172a; display: block; margin-top: 2px;">{confidence:.2f}%</strong>
            </div>
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 0.65rem 0.75rem;">
              <span style="font-size: 10px; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; display: block;">Masa Simpan</span>
              <strong style="font-size: 12.5px; color: #0f172a; display: block; margin-top: 3px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{shelf_life}</strong>
            </div>
          </div>

          <!-- Callout Morfologi (Bila Ada) -->
          {morph_box_html}

          <!-- Spektrum Probabilitas 6 Kelas -->
          <div style="border-top: 1px solid #f1f5f9; padding-top: 0.75rem;">
            <div style="font-size: 11px; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;">
              Spektrum Probabilitas Kelas (CNN Softmax Distribution)
            </div>
            {prob_bars_html}
          </div>

          <!-- Rekomendasi Penanganan -->
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 0.75rem 0.95rem; font-size: 12px; color: #334155; line-height: 1.5;">
            <strong style="color: #0f172a;">Rekomendasi Penanganan:</strong> {saran}
          </div>

        </div>
        """
        st.html(dashboard_html)
