from ultralytics import YOLO

def main():
    # Modeli yükle
    model = YOLO("yolov8n.pt")

    # Eğitim başlat
    model.train(
        data="D:/Sigara/dataset2/data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        device=0
    )

if __name__ == "__main__":
    main()
