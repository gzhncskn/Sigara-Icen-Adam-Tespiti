from ultralytics import YOLO

def main():
    model = YOLO("D:/Model/runs/detect/train3/weights/best.pt")
    metrics = model.val()
    print("mAP@0.5:", metrics.box.map50)
    print("mAP@0.5:0.95:", metrics.box.map)
    print("Precision:", metrics.box.precision)
    print("Recall:", metrics.box.recall)

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # Windows için gerekli
    main()
