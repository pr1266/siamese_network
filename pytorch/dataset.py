import torch
from torch.utils.data import Dataset
from PIL import Image
import numpy as np
import random

class SiameseDataset(Dataset):

    def __init__(self, path, transform=None):
        super(SiameseDataset, self).__init__()
        self.path = path
        self.transform = transform

    def __getitem__(self,index):
        img0_tuple = random.choice(self.path.imgs)

        should_get_same_class = random.randint(0,1) 
        if should_get_same_class:
            while True:
                img1_tuple = random.choice(self.path.imgs) 
                if img0_tuple[1] == img1_tuple[1]:
                    break
        else:
            while True:
                img1_tuple = random.choice(self.path.imgs) 
                if img0_tuple[1] != img1_tuple[1]:
                    break

        img0 = Image.open(img0_tuple[0])
        img1 = Image.open(img1_tuple[0])

        img0 = img0.convert("L")
        img1 = img1.convert("L")

        if self.transform is not None:
            img0 = self.transform(img0)
            img1 = self.transform(img1)
        
        return img0, img1, torch.from_numpy(np.array([int(img1_tuple[1] != img0_tuple[1])], dtype=np.float32))
    
    def __len__(self):
        return len(self.path.imgs)