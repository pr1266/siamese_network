
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

class PrintLayer(nn.Module):

    def __init__(self):
        super(PrintLayer, self).__init__()

    def forward(self, x):
        #! baraye didan joziat e shape ha ino uncomment konid:
        # print('out_size : ', x.size())
        return x

def imshow(img, text=None):
    npimg = img.numpy()
    plt.axis("off")
    if text:
        plt.text(75, 8, text, style='italic',fontweight='bold',
            bbox={'facecolor':'white', 'alpha':0.8, 'pad':10})
        
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()    