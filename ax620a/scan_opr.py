import os
import sys
import math

# no RuntimeError , not TypeError, has scp 
def analyze(fullpath, filename):
    if '_' in filename:
        opr = filename.split('_')[0]
        input_shape = filename.split('_')[1].split('.')[0]
    else:
        opr = filename.split('.onnx')[0]
        input_shape = '224x224'
    
    mac = ""
    mac_utils = ""
    neu = ""
    qps = ""
    efficiency = ""
    with open(fullpath) as f:
        
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            if 'RuntimeError' in line or 'TypeError' in line:
                return (opr, input_shape), line
            
            if 'qps = fps * batch_size =' in line:
                qps = line.split('qps = fps * batch_size =')[1]
                
            if 'MAC per inference' in line:
                mac = line.split('MAC per inference: ')[1].split(' ')[0]
            
            if 'MAC utils: ' in line:
                mac_utils = line.split('MAC utils: ')[1].split(' ')[0]
            
            if 'Run NEU took an average of ' in line:
                neu = line.split('Run NEU took an average of ')[1].split(' (')[0]
    
    if mac != "" and neu != "":
        time_us = neu.split(' ')[0]
        efficiency = str(round(float(mac) / float(time_us)))
    data = [opr, input_shape, qps, mac, mac_utils, neu, efficiency]
    return data, None



with open('opr_test.md', 'w') as f:
    succe_list = []
    error_list = []
    for _root, _dirs, _files in os.walk(sys.argv[1]):
        for _file in _files:
            # data = (opr, inputshape, mac, mac util, NEU took)
            data, error = analyze(os.path.join(_root, _file), _file)

            if error is None:
                succe_list.append(data)
            else:
                # print(error)
                error_list.append(data)
    
    def byEfficiency(elem):
        eff = elem[-1]
        if eff == '':
            eff = 0
        else:
            eff = int(eff)
        return eff
    succe_list.sort(key=byEfficiency, reverse=True)
    head = "| opr | shape | qps | mac | mac_utils | NEU timecost | efficiency |\n"
    middle = "| :-: " * 7 + "|\n"
    f.write(head)
    f.write(middle) 
    for succ in succe_list:
        text = "| {} |\n".format(' | '.join(succ))
        f.write(text)

    f.write('\n\n')
    head = "| opr | shape |\n"
    middle = "| :-: " * 2 + "|\n"
    f.write(head)
    f.write(middle)
    for err in error_list:
        text = "| {} | {} |\n".format(err[0], err[1])
        f.write(text)
    