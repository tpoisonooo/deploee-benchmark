import torch
from torch.nn import Conv2d, Module, functional
from utils import input_spatials, format_list
import pdb
import os

class Model(Module):
    def __init__(self, width):
        super().__init__()
        self.w = torch.rand(width, width)
        
    def forward(self, x, y):
        return torch.cat([x, y], -1)

def work(workdir: str):
    channels = [3]
    ret = []
    for c in channels:
        for spatial in input_spatials():
            width = spatial[-1]  
            m = Model(width)
            input1 = torch.rand(1, c, spatial[0], spatial[1])
            input2 = torch.rand(1, c, spatial[0], spatial[1])

            out = m(input1, input2)
            
            key = 'concat_{}'.format(format_list(input1.shape))
            filename = os.path.join(workdir, '{}.onnx'.format(key))
            
            torch.onnx.export(model=m, args=(input1, input2), f=filename, verbose=False, input_names=['input1', 'input2'], output_names=['output'])
            print('{} input={} output={}'.format(key, format_list(input1.shape), format_list(out.shape)))
            ret.append((key, filename))

    return ret

if __name__ == '__main__':
    ret = work('onnx/concat/')
    print(len(ret))
