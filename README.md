# deploee-benchmark
硬件模型库芯片评测工具集

[onnx 算子导出](./operator/)
ax620a 算子支持列表 https://pulsar-docs.readthedocs.io/zh_CN/latest/appendix/op_support_list.html

1. 单算子 input shape 有 3 个尺寸，不自动 bcast
* 112x112
* h384w256
* 1080p

2. 算子不全部导出，合并同类项、只统计某一行为算子

| 动作 | 导出 opr | 同类项 | 结果 |
| :-: | :-: | :-: | :-: |
| 滑动窗口乘累加 | Conv | ConvTranspose | |
| 矩阵乘 | Matmul | Gemm | |
| binaryOp | Add | Div,Sub | |
| 和 Conv 融合 | ArgMin | ArgMax,Softplus,BatchNormalization,HardSigmoid | |
| 纯内存操作 | Concat | Clip,Pad,Slice,Tile |
| 仅计算 meta 不处理数据 | Flatten | Identity,Reshape,Shape,SpaceToDepth,DepthToSpace,Unsqueeze |
| 遍历 1 次tensor | Sigmoid | GlobalMaxPool,PRelu,ReLU,GlobalAvgPool,Tanh,PRelu,LeakyRelu,ReduceMax,ReduceMean,ReduceSum,Abs | |
| 遍历 2 次或分段成 1 次 | Softmax | ReduceL2 | 转换卡死 |
| 图像操作 | Transpose | Resize，AveragePool,MaxPool | |


* LSTM 应该是组合实现的

长时间不响应：

* shufflenet-v1-1x_16xb64_in1k    https://openmmlab-deploee.oss-cn-shanghai.aliyuncs.com/model/mmcls/shufflenet-v1-1x-b531c4.onnx  
* esrgan_psnr-x4c64b23g32_1xb16-1000k_div2k	https://openmmlab-deploee.oss-cn-shanghai.aliyuncs.com/model/mmedit/esrgan-5d7744.onnx
* srgan_x4c64b16_1xb16-1000k_div2k	https://openmmlab-deploee.oss-cn-shanghai.aliyuncs.com/model/mmedit/srgan-c767a0.onnx
* deeplabv3_r50-d8_4xb4-80k_ade20k-512x512	https://openmmlab-deploee.oss-cn-shanghai.aliyuncs.com/model/mmseg/deeplabv3-89cabe.onnx
* pspnet_r50-d8_4xb4-40k_coco-stuff10k-512x512	https://openmmlab-deploee.oss-cn-shanghai.aliyuncs.com/model/mmseg/pspnet-f667c1.onnx
* deeplabv3plus_r50-d8_4xb4-160k_ade20k-512x512	https://openmmlab-deploee.oss-cn-shanghai.aliyuncs.com/model/mmseg/deeplabv3plus-cdd5bd.onnx
* dbnetpp_resnet50_fpnc_1200e_icdar2015	https://openmmlab-deploee.oss-cn-shanghai.aliyuncs.com/model/mmocr/dbnetpp-f64ac8.onnx
* bisenetv2_fcn_4xb4-160k_cityscapes-1024x1024	https://openmmlab-deploee.oss-cn-shanghai.aliyuncs.com/model/mmseg/bisenetv2-01f169.onnx
* inception-v3_8xb32_in1k	https://openmmlab-deploee.oss-cn-shanghai.aliyuncs.com/model/mmcls/inception-v3-3e3e10.onnx
* stdc1_in1k-pre_4xb12-80k_cityscapes-512x1024	https://openmmlab-deploee.oss-cn-shanghai.aliyuncs.com/model/mmseg/stdc1-6c428d.onnx

8572
测试数据 1088x1920.h264
1088 x 1920  2m18.250s   62
720 x 1920   2m18.025s   62.1

测试数据 720x1280.h264
720 x 1280  2m13.096s    64.4

测试数据 480x640.h264  2m11.005s  65.4

不支持 h265
