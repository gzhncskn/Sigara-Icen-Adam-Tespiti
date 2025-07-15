import torch

if torch.cuda.is_available():
    print("CUDA kullanılabilir! GPU adı:", torch.cuda.get_device_name(0))
else:
    print("CUDA kullanılabilir değil.")
