import torch
device = torch.cuda.get_device_properties(0)
print(device.name)