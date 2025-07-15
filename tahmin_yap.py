import cv2
from ultralytics import YOLO

# Modeli yükle
model = YOLO("D:/Model/runs/detect/train3/weights/best.pt")  # Model yolunu kendine göre düzenle

# Kamera başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Kamera açılamadı.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Model ile tahmin yap (tek kare için)
    results = model(frame, verbose=False)

    # Tahmin edilen görseli al
    annotated_frame = results[0].plot()

    # Pencereye yazdır
    cv2.imshow("Sigara Tespiti - YOLOv8", annotated_frame)

    # ESC ile çık
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Temizle
cap.release()
cv2.destroyAllWindows()
