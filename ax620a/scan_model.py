import os
import sys
import math

# no RuntimeError , not TypeError, has scp 
def analyze(fullpath, filename):

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
            if 'RuntimeError' in line or 'TypeError' in line or 'AttributeError' in line:
                return (filename), line
            # AttributeError: module 'neuwizard.operators' has no attribute 'onnx.TopK'
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
    data = [filename, qps, mac, mac_utils, neu, efficiency]
    return data, None


miss_map = {}
with open('model_test.md', 'w') as f:
    succe_list = []
    error_list = []
    for _root, _dirs, _files in os.walk(sys.argv[1]):
        for _file in _files:
            # data = (opr, inputshape, mac, mac util, NEU took)
            data, error = analyze(os.path.join(_root, _file), _file)

            if error is None:
                succe_list.append(data)
            else:
                if "module 'neuwizard.operators' has no attribute " in error:
                    missed_opr = error.split("'neuwizard.operators' has no attribute '")[1].split("'")[0]
                    if missed_opr not in miss_map:
                        miss_map[missed_opr] = 1
                    else:
                        miss_map[missed_opr] += 1
                # print(error)
    

    # succe_list.sort(key=byEfficiency, reverse=True)
    head = "| model | qps | mac | mac_utils | NEU timecost | efficiency |\n"
    middle = "| :-: " * 6 + "|\n"
    f.write(head)
    f.write(middle) 
    for succ in succe_list:
        text = "| {} |\n".format(' | '.join(succ))
        f.write(text)

    f.write('\n\n')

    head = "| model | qps | mac | mac_utils | NEU timecost | efficiency |"
    middle = "| :-: " * 5 + "|"
    f.write(head + "\n")
    f.write(middle + "\n") 
    for succ in succe_list:
        if 'resnet' in succ[0] and 'in1k' in succ[0]:
            text = "| {} |\n".format(' | '.join(succ))
            f.write(text)

    opr_list = []
    for k,v in miss_map.items():
        opr_list.append((k, v))

    def byRef(elem):
        eff = elem[-1]
        if eff == '':
            eff = 0
        else:
            eff = int(eff)
        return eff
    
    opr_list.sort(key=byRef, reverse=True)

    f.write('\n\n')
    head = "| opr | ref |\n"
    middle = "| :-: " * 2 + "|\n"
    f.write(head)
    f.write(middle)
    for err in opr_list:
        text = "| {} | {} |\n".format(err[0], err[1])
        f.write(text)
