模型转换和测速结果：

| model | qps | mac | mac_utils | NEU timecost | efficiency |
| :-: | :-: | :-: | :-: | :-: | :-: |
| resnetv1c101_8xb32_in1k |  19.00 | 8339777536 | 17.19 | 29355 us | 284101 |
| bisenetv1_r18-d32-in1k-pre_4xb8-160k_cityscapes-1024x1024 |  13.82 | 19971137536 | 29.94 |  |  |
| repvgg-A0_8xb32_in1k |  147.30 | 1452830976 | 23.22 |  |  |
| unet-s5-d16_fcn_4xb4-160k_cityscapes-512x1024 |  13.72 | 11151640576 | 16.60 |  |  |
| panet_resnet18_fpem-ffm_600e_ctw1500 |  40.77 | 2229709824 | 9.86 |  |  |
| upernet_r50_4xb2-80k_cityscapes-512x1024 |  1.18 | 262344851456 | 33.54 |  |  |
| bisenetv1_r18-d32-in1k-pre_4xb4-160k_coco-stuff164k-512x512 |  4.36 | 20141006848 | 9.53 |  |  |
| pspnet_r50-d8_4xb4-40k_voc12aug-512x512 |  0.64 | 143465971712 | 10.03 |  |  |
| resnet34_8xb16_cifar10 |  62.51 | 1270637568 | 8.62 |  |  |
| densenet169_4xb256_in1k |  10.87 | 11251918336 | 13.27 | 42981 us | 261788 |
| repvgg-B2_8xb32_in1k |  14.12 | 20977170432 | 32.13 |  |  |
| resnet50_8xb256-rsb-a3-100e_in1k |  32.04 | 4654049280 | 16.18 | 17793 us | 261566 |
| fcn_r50-d8_4xb4-80k_ade20k-512x512 |  0.67 | 166704840704 | 12.05 |  |  |
| upernet_r50_4xb4-160k_ade20k-512x512 |  0.94 | 262479069184 | 26.77 |  |  |
| fcn_r50-d8_4xb4-20k_voc12aug-512x512 |  118.25 | 611214336 | 7.84 |  |  |
| repvgg-B1g2_8xb32_in1k |  30.83 | 9359124480 | 31.31 |  |  |
| wide-resnet50_8xb32_in1k |  13.72 | 11151640576 | 16.60 |  |  |
| resnetv1c152_8xb32_in1k |  13.96 | 12097759232 | 18.32 | 40156 us | 301269 |
| td-hm_4xmspn50_8xb32-210e_coco-256x192 |  5.64 | 23319330816 | 14.28 | 96462 us | 241746 |
| resnet101_8xb32_in1k |  18.99 | 8325326848 | 17.15 | 29384 us | 283329 |
| textsnake_resnet50-oclip_fpn-unet_1200e_ctw1500 |  1.09 | 164441948160 | 19.39 |  |  |
| resnetv1c50_8xb32_in1k |  32.06 | 4668499968 | 16.24 | 17789 us | 262437 |
| resnet50_8xb256-rsb-a2-300e_in1k |  32.04 | 4654049280 | 16.18 | 17789 us | 261625 |
| seresnet50_8xb32_in1k |  9.09 | 4949552128 | 4.88 | 47904 us | 103322 |
| pspnet_r50-d8_4xb2-80k_cityscapes-512x1024 |  0.64 | 143465971712 | 10.03 |  |  |
| resnet34_8xb32_in1k |  53.49 | 4502997504 | 26.14 | 8643 us | 520999 |
| repvgg-B3_8xb32_in1k |  10.58 | 29633132544 | 34.02 |  |  |
| repvgg-A2_8xb32_in1k |  47.90 | 5657755392 | 29.41 |  |  |
| densenet121_4xb256_in1k |  20.62 | 8503403520 | 19.02 | 24846 us | 342244 |
| resnetv1d50_8xb32_in1k |  33.06 | 4769654784 | 17.11 | 17002 us | 280535 |
| resnext50-32x4d_8xb32_in1k |  24.47 | 5667604480 | 15.05 | 27266 us | 207863 |
| resnext101-32x4d_8xb32_in1k |  13.68 | 6841321472 | 10.15 | 50006 us | 136810 |
| wide-resnet101_8xb32_in1k |  1.18 | 262344851456 | 33.54 |  |  |
| mobileone-s0_8xb32_in1k |  68.31 | 5276104704 | 39.11 |  |  |
| repvgg-B2g4_8xb32_in1k |  19.91 | 13943298048 | 30.12 |  |  |
| fast_scnn_8xb4-160k_cityscapes-512x1024 |  40.77 | 2229709824 | 9.86 |  |  |
| resnet18_8xb32_in1k |  92.90 | 2483513856 | 25.04 | 5390 us | 460763 |
| resnext101-32x8d_8xb32_in1k |  6.65 | 9930557440 | 7.17 | 106705 us | 93066 |
| resnet152_8xb16_cifar10 |  18.20 | 3745304576 | 7.40 |  |  |
| resnet50_8xb32_in1k |  32.04 | 4654049280 | 16.18 | 17793 us | 261566 |
| fcn_r50-d8_4xb2-40k_cityscapes-512x1024 |  20.31 | 9180571648 | 20.23 |  |  |
| resnet18_8xb16_cifar10 |  118.25 | 611214336 | 7.84 |  |  |
| resnet50_8xb16_cifar100 |  44.67 | 1319626752 | 6.40 |  |  |
| resnet152_8xb32_in1k |  13.93 | 12083308544 | 18.27 | 40188 us | 300670 |
| panet_resnet18_fpem-ffm_600e_icdar2015 |  0.67 | 166704840704 | 12.05 |  |  |
| resnet50_8xb16_cifar10 |  44.94 | 1319424000 | 6.43 |  |  |
| repvgg-A1_8xb32_in1k |  100.81 | 2480636160 | 27.13 |  |  |
| resnet101_8xb16_cifar10 |  24.97 | 2518208512 | 6.82 |  |  |
| repvgg-B1g4_8xb32_in1k |  35.47 | 7740647424 | 29.79 |  |  |
| resnext152-32x4d_8xb32_in1k |  9.76 | 9408727040 | 9.96 | 70911 us | 132684 |
| repvgg-B0_8xb32_in1k |  88.62 | 3188719872 | 30.66 |  |  |
| upernet_r50_4xb4-40k_voc12aug-512x512 |  1.18 | 262344851456 | 33.50 |  |  |
| cspresnext50_8xb32_in1k |  20.31 | 9180571648 | 20.23 |  |  |
| densenet161_4xb256_in1k |  4.62 | 25356292352 | 12.71 | 102217 us | 248063 |
| repvgg-B3g4_8xb32_in1k |  15.64 | 17884723200 | 30.34 |  |  |
| seresnet101_8xb32_in1k |  6.53 | 8621526016 | 6.11 | 73724 us | 116943 |
| resnet50_8xb256-rsb-a1-600e_in1k |  32.04 | 4654049280 | 16.18 | 17776 us | 261816 |
| repvgg-D2se_8xb32_in1k |  9.45 | 37378701312 | 38.33 |  |  |
| resnetv1d152_8xb32_in1k |  14.14 | 12198914048 | 18.72 | 39361 us | 309924 |
| resnetv1d101_8xb32_in1k |  19.34 | 8440932352 | 17.72 | 28630 us | 294828 |

resnet 系列运行结果：

| model | qps | mac | mac_utils | NEU timecost | efficiency |
| :-: | :-: | :-: | :-: | :-: | :-: |
| resnet18_8xb32_in1k |  92.90 | 2483513856 | 25.04 | 5390 us | 460763 |
| resnet34_8xb32_in1k |  53.49 | 4502997504 | 26.14 | 8643 us | 520999 |
| resnet50_8xb32_in1k |  32.04 | 4654049280 | 16.18 | 17793 us | 261566 |
| resnet101_8xb32_in1k |  18.99 | 8325326848 | 17.15 | 29384 us | 283329 |
| resnet152_8xb32_in1k |  13.93 | 12083308544 | 18.27 | 40188 us | 300670 |

转换期间缺少的算子：

| opr | ref |
| :-: | :-: |
| onnx.TopK | 61 |
| onnx.InstanceNormalization | 9 |
| onnx.Not | 8 |
| onnx.NonMaxSuppression | 2 |
| onnx.Range | 1 |
| onnx.ReduceL1 | 1 |


长时间不响应的模型，可从硬件模型库搜索下载：

* shufflenet-v1-1x_16xb64_in1k 
* esrgan_psnr-x4c64b23g32_1xb16-1000k_div2k
* srgan_x4c64b16_1xb16-1000k_div2k
* deeplabv3_r50-d8_4xb4-80k_ade20k-512x512
* pspnet_r50-d8_4xb4-40k_coco-stuff10k-512x512
* deeplabv3plus_r50-d8_4xb4-160k_ade20k-512x512
* dbnetpp_resnet50_fpnc_1200e_icdar2015
* bisenetv2_fcn_4xb4-160k_cityscapes-1024x1024
* inception-v3_8xb32_in1k
* stdc1_in1k-pre_4xb12-80k_cityscapes-512x1024
