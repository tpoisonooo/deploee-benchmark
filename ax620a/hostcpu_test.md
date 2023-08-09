编译选项：-DMEGPEAK_ARMV7=1 -Ofast -g  -DMEGPEAK_ARMV7=1  -mtune=native -mfloat-abi=hard -mfpu=neon -std=gnu++14

padal throughput: 5.411672 ns 0.739143 GFlops latency: 6.405562 ns :
padd throughput: 1.509807 ns 2.649345 GFlops latency: 5.024015 ns :
mla_s32 throughput: 5.275521 ns 1.516438 GFlops latency: 5.290761 ns :
mlal_s8 throughput: 2.923057 ns 5.473721 GFlops latency: 5.025521 ns :
mlal_s16 throughput: 2.770953 ns 2.887093 GFlops latency: 5.106042 ns :
mlal_s16_lane throughput: 2.765276 ns 2.893020 GFlops latency: 5.027750 ns :
mla_f32 throughput: 5.354490 ns 1.494073 GFlops latency: 10.047442 ns :
mul_s32 throughput: 5.393568 ns 0.741624 GFlops latency: 5.274667 ns :
mul_f32 throughput: 5.387370 ns 0.742477 GFlops latency: 5.398443 ns :
cvt throughput: 5.377729 ns 0.743808 GFlops latency: 5.352896 ns :
qrdmulh throughput: 5.275443 ns 0.758230 GFlops latency: 5.353959 ns :
rshl throughput: 2.763766 ns 1.447301 GFlops latency: 5.023833 ns :
