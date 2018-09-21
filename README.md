# trn-pytorch-surveillance
This project is based on [TRN-pytorch]()  
Co-work with [Hgeun](https://github.com/Hgeun/tsn-pytorch-surveillance)
# Dataset
The original data set is UCF Crimes. We have trimmed the data to make it suitable for classification.  
Details are shown in
[Trimmed UCF Crimes](https://github.com/henniekim/action_recognition_study/wiki/Temporal-annotation-for-UCF-Crimes-dataset)
# Training

dropout  | rel5 | rel10 | rel15 | rel20
:--: | :--: | :--: | :--: | :--:
dropout 0.4 | x | o | o | o
dropout 0.6 | o | o | o | o
dropout 0.8 | x | o | o | o

```sh
CUDA_VISIBLE_DEVICES=0,1 python main.py moments RGB --arch InceptionV3 --num_segments 10 \
--consensus_type TRNmultiscale --batch-size 16 --dropout 0.6
```
# Testing
```sh
CUDA_VISIBLE_DEVICES=0,1 python test_models.py moments \
RGB model_old2/TRN_moments_RGB_InceptionV3_TRNmultiscale_segment20_best.pth.tar \
--arch InceptionV3 --crop_fusion_type TRNmultiscale --test_segment 20 --save_score TRUE 
```

or simply using
```sh
bash test_models.sh
```
# Results

dropout .6  | rel5 | rel10 | rel15 | rel20
:--: | :--: | :--: | :--: | :--:
TRN | 42.28 | **44.57** | 37.714 | 41.14

# Environment
Linux Ubuntu 14.04  
1 or 2 GPUs for training and testing ; GTX Titan (Pascal) (12GB each)

# Miscellaneous
This project is based on [TRN-pytorch]()
