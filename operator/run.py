import os
import sys


def os_run(cmd: str, redirect_error=True):
    errfile = '/tmp/deploee_converter_err'
    if os.path.exists(errfile):
        os.popen('rm {}'.format(errfile))

    if redirect_error:
        cmd = '{} 2>{}'.format(cmd, errfile)

    ret = os.popen(cmd)
    ret = ret.read().rstrip().lstrip()

    error = None
    if os.path.exists(errfile):
        with open(errfile, 'r') as f:
            text = f.read()
            if text is not None and len(text) > 0:
                error = text

    return ret, error


def convert_profile(model):
    # model conversion
    os_run('rm -rf /tmp/model.joint')

    logs = []
    logs.append('========== model-convert ==========')
    logs.extend(['ax620_virtual_npu: AX620_VIRTUAL_NPU_MODE_111'])
    cmd = 'pulsar build --input {} --output /tmp/model.joint --config /data/base/config/config.prototxt'.format(model)
    stdout, stderr = os_run(cmd)
    logs.extend([cmd, stdout, stderr])

    if not os.path.exists('/tmp/model.joint'):
        print('crash')
        return logs

    logs.append('========== copy-to-device ==========')
    cmd = 'scp /tmp/model.joint root@192.168.233.1:/root/model.joint'
    stdout, stderr = os_run(cmd)
    logs.extend([cmd, stdout, stderr])

    logs.append('========== profiling ==========')
    run_joint = '/opt/bin/run_joint /root/model.joint --repeat 100 --warmup 10'
    cmd = 'ssh root@192.168.233.1 "{}"'.format(run_joint)
    stdout, stderr = os_run(cmd)
    logs.extend([cmd, stdout, stderr])

    return logs


def main(base):
    for root, dirs, files in os.walk(base):
        for file in files:
            print('processing {}..'.format(file))
            reportpath = os.path.join('report', file)
            modelpath = os.path.join(root, file)

            if os.path.exists(reportpath):
                continue
                
            logs = convert_profile(modelpath)
            logs = list(filter(lambda x: x is not None and len(x) > 0, logs))
            logs = list(
                map(
                    lambda x: x.replace('\x1b[0m', '').replace('\x1b[32m', '').
                    replace('\x1b[36m', '').replace('\x1b[0;32m', '').replace(
                        '\x1b[0;36m', ''), logs))
            logstr = '\n'.join(logs)
            with open(reportpath, 'w') as f:
                f.write(logstr)

main(sys.argv[1])
