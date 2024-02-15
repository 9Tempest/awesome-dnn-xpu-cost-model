# awesome-dnn-xpu-cost-model
A list of awesome cost models(analytical, learnt) papers or projects for DNN execution time/memory consumption/energy estimation. Note that CPU models are included but not used for DNNs in general.

## CPU
### Analytical
- [Helal, Ahmed E., et al. "AutoMatch: An automated framework for relative performance estimation and workload distribution on heterogeneous HPC systems." 2017 IEEE International Symposium on Workload Characterization (IISWC). IEEE, 2017.](https://ieeexplore.ieee.org/abstract/document/8167754) (Citations: 14) (throughput estimation, memory consumption estimation)
### Learnt
- [Mendis, Charith, et al. "Ithemal: Accurate, portable and fast basic block throughput estimation using deep neural networks." International Conference on machine learning. PMLR, 2019.](https://proceedings.mlr.press/v97/mendis19a.html) (Citations: 154) (throughput estimation)
- [Sýkora, Ondřej, et al. "GRANITE: A Graph Neural Network Model for Basic Block Throughput Estimation." 2022 IEEE International Symposium on Workload Characterization (IISWC). IEEE, 2022.](https://ieeexplore.ieee.org/abstract/document/9975403) (Citations: 9) (throughput estimation)
## GPU
### Analytical
- [Gao, Yanjie, et al. "Estimating gpu memory consumption of deep learning models." Proceedings of the 28th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering. 2020.](https://dl.acm.org/doi/abs/10.1145/3368089.3417050) (Citations: 106) (memory consumption estimation)
- [Qi, Hang, Evan R. Sparks, and Ameet Talwalkar. "Paleo: A performance model for deep neural networks." International Conference on Learning Representations. 2016.](https://openreview.net/forum?id=SyVVJ85lg) (Citations: 201)(execution time estimation)
- [Wang, Mengdi, et al. "Characterizing deep learning training workloads on alibaba-pai." 2019 IEEE international symposium on workload characterization (IISWC). IEEE, 2019.](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9042047) (Citations: 46) (computation time estimation; io time estimation; communication time estimation on distributed gpu clusters)
- [Gu, Jiazhen, et al. "Deepprof: Performance analysis for deep learning applications via mining gpu execution patterns." arXiv preprint arXiv:1707.03750 (2017).](https://arxiv.org/abs/1707.03750) (Citations: 20) (using runtime GPU trace for performance analysis)

### Learnt
- [Justus, Daniel, et al. "Predicting the computational cost of deep learning models." 2018 IEEE international conference on big data (Big Data). IEEE, 2018.](https://ieeexplore.ieee.org/abstract/document/8622396/) (Citations: 262) (execution time estimation)
- [Bouzidi, Halima, et al. "Performance prediction for convolutional neural networks on edge gpus." Proceedings of the 18th ACM International Conference on Computing Frontiers. 2021.]( https://dl.acm.org/doi/abs/10.1145/3457388.3458666) (Citations:  18) (edge device CNN execution time estimation)
- [Venkataraman, Shivaram, et al. "Ernest: Efficient performance prediction for {Large-Scale} advanced analytics." 13th USENIX Symposium on Networked Systems Design and Implementation (NSDI 16). 2016.](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-venkataraman.pdf) (Citations: 584) (estimation using a small set of dataset, small set of machines and then scaling up to large dataset and large machines)
## FPGA
### Analytical

### Learnt

## TPU
### Analytical

### Learnt