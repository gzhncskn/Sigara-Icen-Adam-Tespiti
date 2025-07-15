import torch
print("GPU kullanılabilir mi?", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Kullanılan GPU:", torch.cuda.get_device_name(0))
else:
    print("⚠️ GPU kullanılmıyor, CPU üzerinden çalışacak.")
