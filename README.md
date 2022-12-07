# level2_objectdetection_cv-level2-cv-01
## Member🔥
| [김범준](https://github.com/quasar529) | [백우열](https://github.com/wooyeolBaek) | [조용재](https://github.com/yyongjae) | [조윤재](https://github.com/KidsareBornStars) | [최명헌](https://github.com/MyeongheonChoi) |
| :-: | :-: | :-: | :-: | :-: |
| <img src="https://avatars.githubusercontent.com/quasar529" width="100"> | <img src="https://avatars.githubusercontent.com/wooyeolBaek" width="100"> | <img src="https://avatars.githubusercontent.com/yyongjae" width="100"> | <img src="https://avatars.githubusercontent.com/KidsareBornStars" width="100"> | <img src="https://avatars.githubusercontent.com/MyeongheonChoi" width="100"> |
***
## Index
* [Project Summary](#project-summary)
* [Procedures](#procedures)
* [Features](#features)
* [Result](#result)
* [Conclusion](#conclusion)
* [How to Run](#how-to-run)
***
## Project Summary
### 대회 주제 및 개요

주어진 사진에서 쓰레기를 Detection 하는 모델을 만들어, 환경 부담을 줄일 수 있는 방법 중 하나인 분리수거에 적용해
'쓰레기 대란', '매립지 부족'과 같은 여러 사회 문제를 해결하고자 한다.
문제 해결을 위한 데이터셋으로는 10가지 종류의 쓰레기가 찍힌 사진 데이터셋을 사용한다.
평가 방법은 Test set의 mAP50(Mean Average Precision)로 평가한다.
(이때 Test set은 총 4871장으로, 이 중 50%만 public이고 나머지는 private이다.)

### 데이터셋의 구조

- 전체 이미지 개수 : 9754장 (train : 4883장, test : 4871장)
- 10 class : General trash, Paper, Paper pack, Metal, Glass, Plastic, Styrofoam, Plastic bag, Battery, Clothing
- 이미지 크기 : (1024, 1024)
- annotation file은 [coco format](https://cocodataset.org/#home)으로(images, annotations)의 정보를 가지고 있다.
    - images
        - id: 파일 안에서 image 고유 id, ex) 1
        - height: 1024
        - width: 1024
        - file*name: ex) train*/0000.jpg
    - annotations
        - id: 파일 안에 annotation 고유 id, ex) 1
        - bbox: 객체가 존재하는 박스의 좌표 (x*min, y*min, w, h)
        - area: 객체가 존재하는 박스의 크기
        - category_id: 객체가 해당하는 class의 id
        - image_id: annotation이 표시된 이미지 고유 id
    - 단 test set은 train set과는 다르게 annotation 정보가 포함되어 있지 않고 이미지 정보만 가지고 있다.

***
## Procedures
**[2022.11.14 - 2022.11.18]**
- Object Detection 이론 학습.
- 사용할 라이브러리 결정 -> mmdetection 사용법 숙지.

**[2022.11.21 - 2022.11.25]**
- Model 결정 
  - 1-stage model : yoloV5, yoloV7
  - 2-stage model : ResNet50-faster_rcnn, SwinTransfomer-faster_rcnn, ATSS
- CV strategy 실험 
  - Class 비율
  - bbox 크기 비율
  - class & bbox 크기 모두 고려한 비율 <-test set에 가장 근접하다는 결론내림.
- Augmentation
  - 1-stage model : `hyp.scratch_high.yaml` 적용
  - 2-stage model : 
    - `ShiftScaleRotate`, `RandomBrightnessContrast`, (`RGBShift`, `HueSaturationValue`), `GaussNoise`, `JpegCompression`, `ChannelShuffle`, (`Blur`,`MedianBlur`), `RandomFlip`
    - TTA : `Resize`, `RandomFlip`, `Normalize`, `Pad`, `ImageToTensor`, `Collect`
- Experiments:
    - Image Tiling : 비교적 작은 이미지의 confidence score 향상을 목적으로 test set을 4개의 이미지로 tiling한 후 inference 진행 -> tiling으로 나눠진 비교적 큰 물체의 bbox를 NMS로 제거하는 문제 이후 진행 중단

**[2022.11.28 - 2022.11.29]**
- 유효 기법 적용한 모든 fold 학습
- CV strategy
  - 가로,세로 비율이 일정 기준보다 작거나 큰 bbox 제거 후 CV -> 기존보다 성능 하락. 적용X.

**[2022.11.30 - 2022.12.01]**
- Pseudo Labeling with threshold = 0.6
- Ensemble : NMS, Soft-NMS, WBF  
<img src="files\pipeline.png" width="90%" height="30%"/>

***
## Result
**Public 9th. Private 12th(9th).**  
<img src="files\result_leaderboard.png" width="20%" height="5%"/>
- 단일 모델 제출 최고 점수 : 0.6103→0.5987 (Swin_transformer-ATSS)
- Ensemble 후 (public → private)
    - 0.6810 → 0.6635 : swin-l, yoloV5, yoloV7의 f0~4와 pseudo label 총 30개 WBF Ensemble
    - 0.6776 → 0.6602 : swin-l, yoloV5, yoloV7의 f0~4 총 15개 WBF Ensemble
    - 0.6756 → 0.6587 : swin-l f0,f2,f4와 yoloV5 f0~4 yoloV7 f0~4 총 13개 WBF Ensemble
***
## Conclusion
### 잘한 점

1. 가설→실험→분석→재실험의 과정을 지키려고 노력했고, 의사결정 역시 최대한 실험을 기반으로 진행하기 위해 노력했다.
2. 회의 중 안건들에 대하여 팀원들끼리 소통을 통하여 결정하려 하였고, 오프라인 미팅을 통하여 가까워지는 시간을 가졌다.
3. 점수 상승 및 순위에 매달리지 않고 계획한 실험을 진행하는 데 초점을 맞췄다.
4. 서로의 시행착오를 공유해 오류 해결하는 시간을 줄일 수 있었다.

### 아쉬운 점

1. 경진 대회 초기에 태스크에 대한 어려움으로 인해 일정 관리를 철저히 하지 못해 첫 주를 아쉽게 보냈다.
2. 조금 더 많이 분업하여 효율적으로 시간을 사용할 수 있었을 것 같은데 다들 처음이다보니 조금 어려웠다.
3. 모델 학습 속도의 제약으로 더 많은 수의 실험을 하지 못했다.
4. 마지막 Ensemble 단계에서 제출 파일의 용량 및 서버 속도 이슈로, 계획했던 전략을 바탕으로 진행한 실험의 결과를 제출하지 못했다.
5. EDA를 좀 더 구체적이고 세부적으로 했으면 Data를 잘 파악했을 것이고 그에 따른 추가적인 전략을 세울 수 있었을 것 같다.
6. 모델 예측 결과의 충분한 분석과 모델 구조에 대한 고려 없이 mAP만 보고 문제를 정의하다보니 본질적인 문제에 접근하지 못해서, 실험 결과들을 하나의 결과로 수렴시키진 못한 것 같다.
7. 충분한 Augmentation 실험을 했다고 생각되지만 효과적인 방법을 찾지 못한 것 같다.
8. 계획 및 관리 방법에 대해 많은 이야기를 나눴지만 그만큼의 효율을 내지는 못한 것 같다.

### 프로젝트를 통해 배운 점

1. 모든 의사결정은 느낌,추측이 아닌 실험 진행 후 결과를 분석 한 후 이를 기반으로 해야지 합당하고 올바른 의사결정이 가능하다.
2. Detection Task에서 가설을 세우고 실험을 하는 데에 많은 시간이 소요되기 때문에, 실험을 시도, 검증하는 과정을 빠르게 거치는 것이 중요해 보인다. 
3. 생각보다 많은 기능이 라이브러리 내부에 구현되어 있는 경우가 많아, 이를 잘 활용하면 시간 단축을 할 수 있으니 관련 문서를 잘 읽어보는 것이 중요하다.
***
### Folder Structure 📂
```
📂 level2_objectdetection_cv-level2-cv-01
│      
├── 📂 mmdetection
│      │
│      ├── 📂 config
│      │     │ 
│      │     ├── 📂 __base__
│      │     │    ├── 📂 datasets
│      │     │    │    ├── 📑 coco_detection.py
│      │     │    │    ├── 📑 coco_detection_classbalanceddataset.py
│      │     │    │    ├── 📑 coco_detection_cutout.py
│      │     │    │    ├── 📑 coco_detection_heavy.py
│      │     │    │    ├── 📑 coco_detection_mixup.py
│      │     │    │    ├── 📑 coco_detection_mosaic.py
│      │     │    │    └── ...
│      │     │    ├── 📂 models
│      │     │    │    ├── 📑 faster_rcnn_r50_fpn.py
│      │     │    │    ├── 📑 faster_rcnn_r50_fpn_ciou.py
│      │     │    │    ├── 📑 faster_rcnn_r50_fpn_diou.py
│      │     │    │    └── ...
│      │     │    ├── 📂 schedules
│      │     │    │    └── 📑 schedule_1x.py
│      │     │    └── 📑 default_runtime.py
│      │     │ 
│      │     ├── 📑 atss_swin-l-p4-w12_fpn_dyhead_mstrain_2x_coco.py
│      │     ├── 📑 faster_rcnn_r50.py
│      │     ├── 📑 faster_rcnn_swin.py
│      │     ├── 📑 swin_large_dyhead_base.py
│      │     └── ...
│      │
│      ├── 📂 mmdet
│      │
│      └── 📂 tools
│           ├── 📑 train.py
│           ├── 📑 test.py
│           ├── 📑 test_csv.py
│           └── ...
│
├── 📂 submission
│     └──...
│
├── 📂 utility
│     ├── 📂 convert2Yolo
│     │     ├── example.py
│     │     └──...
│     ├── 📑 CV_strategy.ipynb
│     ├── 📑 EDA.ipynb
│     ├── 📑 confusion_matrix.py
│     ├── 📑 csv_csv.ipynb
│     ├── 📑 csv_json.ipynb
│     ├── 📑 ensemble.ipynb
│     ├── 📑 image_split.ipynb
│     ├── 📑 modify_precision.ipynb
│     ├── 📑 pseudolabeling.ipynb
│     ├── 📑 split_for_yolodata.ipynb
│     └── 📑 tile_combine.ipynb
│      
├── 📂 yolov5
│    │
│    ├── 📂 data
│    │    ├── 📂 hyps
│    │    │    ├── 📑 hyp.scratch_high.yaml
│    │    │    ├── 📑 hyp.custom.yaml
│    │    │    └── ...
│    │    ├── 📑 custom_data.yaml
│    │    ├── 📑 custom_data_fold1.yaml
│    │    └── ...
│    │ 
│    ├── 📂 models
│    │    ├── 📑 yolo.py
│    │    ├── 📑 yolo5l-custom.yaml
│    │    └── ...
│    │    
│    ├── 📂 utils
│    │    └── ...
│    │    
│    ├── 📑 train.py
│    ├── 📑 hubconf.py
│    ├── 📑 inference.ipynb
│    └── ...
│
└── 📂 yolov7
     │
     ├── 📂 cfg
     │    ├── 📂 baseline
     │    │    ├── 📑 yolor-w6.yaml
     │    │    ├── 📑 yolov3.yaml
     │    │    └── ...
     │    ├── 📂 deploy
     │    │    ├── 📑 yolov7-w6.yaml
     │    │    ├── 📑 yolov7.yaml
     │    │    │    └── ...
     │    ├── 📂 training
     │    │    ├── 📑 yolov7-w6.yaml
     │    │    ├── 📑 yolov7.yaml
     │    │    └── ...
     ├── 📂 data
     │    ├── 📑 coco.yaml
     │    ├── 📑 hyp.scratch.custom.yaml
     │    └── ...
     ├── 📂 models
     │    ├── 📑 yolo.py
     │    └── ...
     │    
     ├── 📂 utils
     │    └── ...
     │    
     ├── 📑 train.py
     ├── 📑 train_aux.py
     ├── 📑 hubconf.py
     ├── 📑 inference.ipynb
     └── ...    

```

### How to Run
#### Requirements
- Python >= 3.7.5
- torch == 1.7.1
- albumentation >=0.3.2 --no-binary qudida,albumentations
- tqdm
- visdom
- seaborn
- albumentations
- pycocotools
- opencv-python
- tqdm
- torchnet
- pandas
- map-boxes
- jupyter
- ensemble_boxes==1.0.9

### MMDetection 
https://github.com/open-mmlab/mmdetection
#### Step 1.
```bash
cd mmdetection
```
#### Step 2. : Train
```bash
python tools/train.py \
        configs/{config 파일명}
```
#### Step 3. : Test
```bash
python tools/test_csv.py \
        configs/{config 파일명} \
        work_dirs/{config 파일명}/{checkpoint 파일명} \
        --eval bbox
```


### YoloV5 
https://github.com/ultralytics/yolov5
#### Step 1.

```bash
cd yolov5
```
#### Step 2. Train
```bash
python train.py --weights {pretrained_weight} --cfg {custom_model_config} --data{custom_data} --hyp {custom_hyp_yaml}
```

### YoloV7
https://github.com/WongKinYiu/yolov7

#### Step 1.
```
cd yolov7
```
#### Step 2. Train

#### Default
```
python train.py --weights {pretrained_weight} --cfg {custom_model_config} --data{custom_data} --hyp {custom_hyp_yaml} 
```
#### Training with bigger yolov7 models
```
python train_aux.py --weights {pretrained_weight} --cfg {custom_model_config} --data{custom_data} --hyp {custom_hyp_yaml}
```
***

