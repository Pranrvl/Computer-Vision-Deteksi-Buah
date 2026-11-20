"""
test_model.py
Integration & Regression Test for Frutta Fruit Freshness Detection System.
Verifies pure NumPy CNN inference against official DATA_BUAH_COMVIS.ipynb classes.
"""

from model_engine import FruitModel
from PIL import Image
from io import BytesIO
import os, time

model = FruitModel()
print("Model loaded successfully from:", model.weights_path)

sample_dir = "samples"
labels_expected = {
    "demo_green_apple.jpg": ("freshapples", "Apel", "Segar"),
    "demo_fresh_banana.jpg": ("freshbanana", "Pisang", "Segar"),
    "demo_fresh_orange.jpg": ("freshoranges", "Jeruk", "Segar"),
    "demo_rotten_apple.jpg": ("rottenapples", "Apel", "Busuk"),
    "demo_rotten_banana.jpg": ("rottenbanana", "Pisang", "Busuk"),
    "demo_rotten_orange.jpg": ("rottenoranges", "Jeruk", "Busuk"),
}

all_pass = True
print("\n--- Running 6 Class Verification Tests ---")
for fname, (expected_cls, expected_jenis, expected_kondisi) in labels_expected.items():
    path = os.path.join(sample_dir, fname)
    t0 = time.time()
    result = model.predict_image(path)
    elapsed = (time.time() - t0) * 1000
    
    predicted = result["predicted_class"]
    jenis = result["jenis"]
    kondisi = result["kondisi"]
    conf = result["confidence_pct"]
    
    ok = (predicted == expected_cls and jenis == expected_jenis and kondisi == expected_kondisi)
    if not ok:
        all_pass = False
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {fname:24s} -> {predicted:15s} | {jenis:6s} | {kondisi:6s} ({conf:6.2f}%) [{elapsed:.1f}ms]")

print("\n--- BytesIO Upload Simulation Test ---")
img = Image.open(os.path.join(sample_dir, "demo_green_apple.jpg"))
buf = BytesIO()
img.save(buf, format="JPEG")
buf.seek(0)
result2 = model.predict_image(buf)
print(f"BytesIO test: {result2['predicted_class']} ({result2['jenis']} - {result2['kondisi']}) [{result2['confidence_pct']:.2f}%]")
print(f"Sorted classes: {len(result2.get('all_classes_sorted', []))}")
print(f"Result keys: {sorted(result2.keys())}")
print()

if all_pass:
    print(">>> ALL 6 TESTS PASSED! 100% SUCCESS <<<")
else:
    print(">>> SOME TESTS FAILED! <<<")
