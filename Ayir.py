import os
import random
import shutil

# Kaynak klasör
image_dir = r"D:\Sigara\dataset2\images\merged"
label_dir = r"D:\Sigara\dataset2\labels\merged"

# Hedef klasörler
base_output = r"D:\Sigara\dataset2"
splits = ['train', 'val', 'test']
split_ratio = {'train': 0.8, 'val': 0.1, 'test': 0.1}

# Hedef klasörleri oluştur
for split in splits:
    os.makedirs(os.path.join(base_output, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(base_output, 'labels', split), exist_ok=True)

# Tüm görselleri listele
all_images = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(all_images)

# Ayır
total = len(all_images)
train_cut = int(total * split_ratio['train'])
val_cut = train_cut + int(total * split_ratio['val'])

datasets = {
    'train': all_images[:train_cut],
    'val': all_images[train_cut:val_cut],
    'test': all_images[val_cut:]
}

# Kopyalama işlemi
for split, files in datasets.items():
    for file in files:
        name, _ = os.path.splitext(file)
        src_img = os.path.join(image_dir, file)
        src_lbl = os.path.join(label_dir, name + ".txt")
        dst_img = os.path.join(base_output, 'images', split, file)
        dst_lbl = os.path.join(base_output, 'labels', split, name + ".txt")

        shutil.copy2(src_img, dst_img)
        if os.path.exists(src_lbl):
            shutil.copy2(src_lbl, dst_lbl)

print("✅ train/val/test klasörleri başarıyla oluşturuldu.")
