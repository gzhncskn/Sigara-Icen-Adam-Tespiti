import os
import shutil

# Kaynak klasör: ZIP'lerden çıkartılan tüm veri setlerinin bulunduğu yer
source_root = r"D:\Sigara\TOPLU"

# Hedef klasör: Tüm veriler buraya toplanacak
output_images = r"D:\Sigara\dataset2\images\merged"
output_labels = r"D:\Sigara\dataset2\labels\merged"
os.makedirs(output_images, exist_ok=True)
os.makedirs(output_labels, exist_ok=True)

# Desteklenen dosya uzantıları
img_exts = ['.jpg', '.jpeg', '.png']
label_ext = '.txt'

# Tüm görsel ve etiket yollarını topla
image_paths = []
label_paths = {}

for root, dirs, files in os.walk(source_root):
    for file in files:
        name, ext = os.path.splitext(file.lower())
        full_path = os.path.join(root, file)

        if ext in img_exts:
            image_paths.append((name, full_path))

        elif ext == label_ext:
            label_paths[name] = full_path

# Eşleşenleri dataset2'ye kopyala
moved = 0
skipped = 0

for name, img_path in image_paths:
    if name in label_paths:
        try:
            shutil.copy2(img_path, os.path.join(output_images, os.path.basename(img_path)))
            shutil.copy2(label_paths[name], os.path.join(output_labels, os.path.basename(label_paths[name])))
            moved += 1
        except Exception as e:
            print(f"⚠️ Atlandı (Hata): {img_path}\nSebep: {e}")
            skipped += 1
    else:
        skipped += 1

# Rapor
print(f"\n✅ {moved} etiketli görüntü dataset2 klasörüne başarıyla kopyalandı.")
print(f"🚫 {skipped} dosya eşleşmedi veya hata verdi.")
