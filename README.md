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
| 遍历 2 次或分段成 1 次 | Softmax | ReduceL2 | |
| 图像操作 | Transpose | Resize，AveragePool,MaxPool | |

* LSTM 应该是组合实现的
