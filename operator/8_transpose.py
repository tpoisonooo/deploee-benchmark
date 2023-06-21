import torch
from torch.nn import Conv2d, Module, functional
from torchvision import transforms
from utils import input_spatials, format_list
import pdb
import os

class Model(Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x):
        return torch.transpose(x, 2, 3)

def work(workdir: str):
    channels = [3]
    ret = []
    for c in channels:
        for spatial in input_spatials():
            m = Model()
            input_ = torch.rand(1, c, spatial[0], spatial[1])
            out = m(input_)
            
            key = 'transpose_{}'.format(format_list(input_.shape))
            filename = os.path.join(workdir, '{}.onnx'.format(key))
            
            torch.onnx.export(model=m, args=(input_), f=filename, verbose=False, input_names=['input'], output_names=['output'])
            print('{} input={} output={}'.format(key, format_list(input_.shape), format_list(out.shape)))
            ret.append((key, filename))

    return ret

if __name__ == '__main__':
    ret = work('onnx/transpose/')
    print(len(ret))
