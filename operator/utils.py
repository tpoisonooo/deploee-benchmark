import torch

def input_spatials():
    return [[112,112], [384,256], [1080,1920]]

def format_list(int_shape):
    str_shape = map(lambda x:str(x), int_shape)
    return 'x'.join(str_shape)
