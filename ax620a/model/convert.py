import hashlib
import math
import os
import random
import string
import sys
import time
import wget
from loguru import logger
from urllib import request
from urllib.parse import quote


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
    basename = os.path.basename(model)
    jointdir = '/data/model/joint/'

    targetpath = jointdir + basename.split('.')[0] + '.joint'
    os_run('rm -rf {}'.format(targetpath))

    logs = []
    logs.append('========== model-convert ==========')
    logs.extend(['ax620_virtual_npu: AX620_VIRTUAL_NPU_MODE_111'])
    cmd = 'pulsar build --input {} --output {} --config /data/base/config/config.prototxt'.format(model, targetpath)
    stdout, stderr = os_run(cmd)
    logs.extend([cmd, stdout, stderr])

    if not os.path.exists(targetpath):
        print('crash')
        return logs

    return logs


def oss_download(directory, url, use_cache=False):
    localpath = os.path.join(directory, url[url.rfind('/') + 1:])
    if not os.path.exists(directory):
        os.makedirs(directory)

    error = None

    if use_cache:
        cache_url = 'http://10.1.52.36:10009/getFile?url={}'.format(url)
        try:
            with request.urlopen(cache_url) as f:
                if f.status == 200:
                    # use cache
                    os.system(
                        'wget -N --quiet --show-progress {} -O {}'.format(
                            cache_url, localpath))

                    if not os.path.exists(localpath):
                        error = 'cache url download failed {}'.format(
                            cache_url)

                    return localpath, error
        except Exception:
            pass

    try:
        with request.urlopen(url) as f:
            pass
    except Exception:
        logger.error('{} not exist'.format(url))
        return localpath, '下载异常'

    try:
        localpath = wget.download(url, out=directory)

        if not os.path.exists(localpath):
            error = 'url download failed {}'.format(url)
    except Exception as e:
        logger.error('download faild{}'.format(e))
        error = 'download failed'
    finally:
        return localpath, error


def main(model_list):
    with open(model_list) as f:
        lines = f.readlines()
        for line in lines:
            splited = line.split('\t')
            _name = splited[0].strip()
            _url = splited[1].strip()

            reportpath = os.path.join('/data/report_model', _name)
            if os.path.exists(reportpath):
                continue

            modelpath, error = oss_download(directory='/data/model/onnx', url=_url)

            if error is not None:
                print(error)
                break

            print('processing {}..'.format(modelpath))
            
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