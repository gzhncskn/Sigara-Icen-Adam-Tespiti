import cv2
from ultralytics import YOLO

# 📦 Eğittiğin modeli yükle
model = YOLO("best.pt")  # model adını gerektiği gibi değiştir

# 📸 Kamerayı başlat
cap = cv2.VideoCapture(0)  # 0: varsayılan kamera

# ➖ Sarı çizginin x koordinatını sabit tanımla (kamera görüntüsüne göre ayarla)
yellow_line_x = 400

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 🧠 Model ile tahmin yap
    results = model(frame)[0]

    # 🟨 Sarı çizgiyi çiz (görsel referans için)
    cv2.line(frame, (yellow_line_x, 0), (yellow_line_x, frame.shape[0]), (0, 255, 255), 2)

    # 🧱 Her bir tespit edilen nesne için kutu çiz
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # bounding box koordinatları
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])

        # 💡 Kutu merkezini hesapla
        center_x = (x1 + x2) // 2

        # 🎨 Renk belirle (sarı çizginin içinde: kırmızı, dışında: mavi)
        color = (0, 0, 255) if center_x < yellow_line_x else (255, 0, 0)

        # 📦 Kutuyu çiz
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        # 🏷 Sınıf adını ve güveni yaz (isteğe bağlı)
        label = f"{model.names[cls_id]} {conf:.2f}"
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # 🎥 Görüntüyü göster
    cv2.imshow("Sigara Tespiti", frame)

    # Çıkmak için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 🔚 Temizlik
cap.release()
cv2.destroyAllWindows()
