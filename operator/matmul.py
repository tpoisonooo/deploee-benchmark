import torch
from torch.nn import Conv2d, Module
from utils import input_spatials, format_list
import pdb
import os

class SimpleGemm(Module):
    def __init__(self, width):
        super().__init__()
        self.w = torch.rand(width, width)
        
    def forward(self, x):
        return x @ self.w

def work(workdir: str):
    channels = [1, 64, 1024]
    ret = []
    for c in channels:
        for spatial in input_spatials():
            width = spatial[-1]  
            m = SimpleGemm(width)
            input_ = torch.rand(1, c, spatial[0], spatial[1])
            out = m(input_)
            
            key = 'gemm_{}'.format(format_list(input_.shape))
            filename = os.path.join(workdir, '{}.onnx'.format(key))
            
            torch.onnx.export(model=m, args=(input_), f=filename, verbose=False, input_names=['input'], output_names=['output'])
            print('{} input={} output={}'.format(key, format_list(input_.shape), format_list(out.shape)))
            ret.append((key, filename))

    return ret

if __name__ == '__main__':
    ret = work('onnx/gemm/')
    print(len(ret))
