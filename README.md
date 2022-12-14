# level2_objectdetection_cv-level2-cv-01
## Member๐ฅ
| [๊น๋ฒ์ค](https://github.com/quasar529) | [๋ฐฑ์ฐ์ด](https://github.com/wooyeolBaek) | [์กฐ์ฉ์ฌ](https://github.com/yyongjae) | [์กฐ์ค์ฌ](https://github.com/KidsareBornStars) | [์ต๋ชํ](https://github.com/MyeongheonChoi) |
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
### ๋ํ ์ฃผ์  ๋ฐ ๊ฐ์

์ฃผ์ด์ง ์ฌ์ง์์ ์ฐ๋ ๊ธฐ๋ฅผ Detection ํ๋ ๋ชจ๋ธ์ ๋ง๋ค์ด, ํ๊ฒฝ ๋ถ๋ด์ ์ค์ผ ์ ์๋ ๋ฐฉ๋ฒ ์ค ํ๋์ธ ๋ถ๋ฆฌ์๊ฑฐ์ ์ ์ฉํด
'์ฐ๋ ๊ธฐ ๋๋', '๋งค๋ฆฝ์ง ๋ถ์กฑ'๊ณผ ๊ฐ์ ์ฌ๋ฌ ์ฌํ ๋ฌธ์ ๋ฅผ ํด๊ฒฐํ๊ณ ์ ํ๋ค.
๋ฌธ์  ํด๊ฒฐ์ ์ํ ๋ฐ์ดํฐ์์ผ๋ก๋ 10๊ฐ์ง ์ข๋ฅ์ ์ฐ๋ ๊ธฐ๊ฐ ์ฐํ ์ฌ์ง ๋ฐ์ดํฐ์์ ์ฌ์ฉํ๋ค.
ํ๊ฐ ๋ฐฉ๋ฒ์ Test set์ mAP50(Mean Average Precision)๋ก ํ๊ฐํ๋ค.
(์ด๋ Test set์ ์ด 4871์ฅ์ผ๋ก, ์ด ์ค 50%๋ง public์ด๊ณ  ๋๋จธ์ง๋ private์ด๋ค.)

### ๋ฐ์ดํฐ์์ ๊ตฌ์กฐ

- ์ ์ฒด ์ด๋ฏธ์ง ๊ฐ์ : 9754์ฅ (train : 4883์ฅ, test : 4871์ฅ)
- 10 class : General trash, Paper, Paper pack, Metal, Glass, Plastic, Styrofoam, Plastic bag, Battery, Clothing
- ์ด๋ฏธ์ง ํฌ๊ธฐ : (1024, 1024)
- annotation file์ย [coco format](https://cocodataset.org/#home)์ผ๋ก(images, annotations)์ ์ ๋ณด๋ฅผ ๊ฐ์ง๊ณ  ์๋ค.
    - images
        - id: ํ์ผ ์์์ image ๊ณ ์  id, ex) 1
        - height: 1024
        - width: 1024
        - file*name: ex) train*/0000.jpg
    - annotations
        - id: ํ์ผ ์์ annotation ๊ณ ์  id, ex) 1
        - bbox: ๊ฐ์ฒด๊ฐ ์กด์ฌํ๋ ๋ฐ์ค์ ์ขํ (x*min, y*min, w, h)
        - area: ๊ฐ์ฒด๊ฐ ์กด์ฌํ๋ ๋ฐ์ค์ ํฌ๊ธฐ
        - category_id: ๊ฐ์ฒด๊ฐ ํด๋นํ๋ class์ id
        - image_id: annotation์ด ํ์๋ ์ด๋ฏธ์ง ๊ณ ์  id
    - ๋จ test set์ train set๊ณผ๋ ๋ค๋ฅด๊ฒ annotation ์ ๋ณด๊ฐ ํฌํจ๋์ด ์์ง ์๊ณ  ์ด๋ฏธ์ง ์ ๋ณด๋ง ๊ฐ์ง๊ณ  ์๋ค.

***
## Procedures
**[2022.11.14 - 2022.11.18]**
- Object Detection ์ด๋ก  ํ์ต.
- ์ฌ์ฉํ  ๋ผ์ด๋ธ๋ฌ๋ฆฌ ๊ฒฐ์  -> mmdetection ์ฌ์ฉ๋ฒ ์์ง.

**[2022.11.21 - 2022.11.25]**
- Model ๊ฒฐ์  
  - 1-stage model : yoloV5, yoloV7
  - 2-stage model : ResNet50-faster_rcnn, SwinTransfomer-faster_rcnn, ATSS
- CV strategy ์คํ 
  - Class ๋น์จ
  - bbox ํฌ๊ธฐ ๋น์จ
  - class & bbox ํฌ๊ธฐ ๋ชจ๋ ๊ณ ๋ คํ ๋น์จ <-test set์ ๊ฐ์ฅ ๊ทผ์ ํ๋ค๋ ๊ฒฐ๋ก ๋ด๋ฆผ.
- Augmentation
  - 1-stage model : `hyp.scratch_high.yaml` ์ ์ฉ
  - 2-stage model : 
    - `ShiftScaleRotate`, `RandomBrightnessContrast`, (`RGBShift`, `HueSaturationValue`), `GaussNoise`, `JpegCompression`, `ChannelShuffle`, (`Blur`,`MedianBlur`), `RandomFlip`
    - TTA : `Resize`, `RandomFlip`, `Normalize`, `Pad`, `ImageToTensor`, `Collect`
- Experiments:
    - Image Tiling : ๋น๊ต์  ์์ ์ด๋ฏธ์ง์ confidence score ํฅ์์ ๋ชฉ์ ์ผ๋ก test set์ 4๊ฐ์ ์ด๋ฏธ์ง๋ก tilingํ ํ inference ์งํ -> tiling์ผ๋ก ๋๋ ์ง ๋น๊ต์  ํฐ ๋ฌผ์ฒด์ bbox๋ฅผ NMS๋ก ์ ๊ฑฐํ๋ ๋ฌธ์  ์ดํ ์งํ ์ค๋จ

**[2022.11.28 - 2022.11.29]**
- ์ ํจ ๊ธฐ๋ฒ ์ ์ฉํ ๋ชจ๋  fold ํ์ต
- CV strategy
  - ๊ฐ๋ก,์ธ๋ก ๋น์จ์ด ์ผ์  ๊ธฐ์ค๋ณด๋ค ์๊ฑฐ๋ ํฐ bbox ์ ๊ฑฐ ํ CV -> ๊ธฐ์กด๋ณด๋ค ์ฑ๋ฅ ํ๋ฝ. ์ ์ฉX.

**[2022.11.30 - 2022.12.01]**
- Pseudo Labeling with threshold = 0.6
- Ensemble : NMS, Soft-NMS, WBF  
<img src="files\pipeline.png" width="90%" height="30%"/>

***
## Result
**Public 9th. Private 12th(9th).**  
<img src="files\result_leaderboard.png" width="20%" height="5%"/>
- ๋จ์ผ ๋ชจ๋ธ ์ ์ถ ์ต๊ณ  ์ ์ : 0.6103โ0.5987 (Swin_transformer-ATSS)
- Ensemble ํ (public โ private)
    - 0.6810 โ 0.6635 : swin-l, yoloV5, yoloV7์ f0~4์ pseudo label ์ด 30๊ฐ WBF Ensemble
    - 0.6776 โ 0.6602 : swin-l, yoloV5, yoloV7์ f0~4 ์ด 15๊ฐ WBF Ensemble
    - 0.6756 โ 0.6587 : swin-l f0,f2,f4์ yoloV5 f0~4 yoloV7 f0~4 ์ด 13๊ฐ WBF Ensemble
***
## Conclusion
### ์ํ ์ 

1. ๊ฐ์คโ์คํโ๋ถ์โ์ฌ์คํ์ ๊ณผ์ ์ ์งํค๋ ค๊ณ  ๋ธ๋ ฅํ๊ณ , ์์ฌ๊ฒฐ์  ์ญ์ ์ต๋ํ ์คํ์ ๊ธฐ๋ฐ์ผ๋ก ์งํํ๊ธฐ ์ํด ๋ธ๋ ฅํ๋ค.
2. ํ์ ์ค ์๊ฑด๋ค์ ๋ํ์ฌ ํ์๋ค๋ผ๋ฆฌ ์ํต์ ํตํ์ฌ ๊ฒฐ์ ํ๋ ค ํ์๊ณ , ์คํ๋ผ์ธ ๋ฏธํ์ ํตํ์ฌ ๊ฐ๊น์์ง๋ ์๊ฐ์ ๊ฐ์ก๋ค.
3. ์ ์ ์์น ๋ฐ ์์์ ๋งค๋ฌ๋ฆฌ์ง ์๊ณ  ๊ณํํ ์คํ์ ์งํํ๋ ๋ฐ ์ด์ ์ ๋ง์ท๋ค.
4. ์๋ก์ ์ํ์ฐฉ์ค๋ฅผ ๊ณต์ ํด ์ค๋ฅ ํด๊ฒฐํ๋ ์๊ฐ์ ์ค์ผ ์ ์์๋ค.

### ์์ฌ์ด ์ 

1. ๊ฒฝ์ง ๋ํ ์ด๊ธฐ์ ํ์คํฌ์ ๋ํ ์ด๋ ค์์ผ๋ก ์ธํด ์ผ์  ๊ด๋ฆฌ๋ฅผ ์ฒ ์ ํ ํ์ง ๋ชปํด ์ฒซ ์ฃผ๋ฅผ ์์ฝ๊ฒ ๋ณด๋๋ค.
2. ์กฐ๊ธ ๋ ๋ง์ด ๋ถ์ํ์ฌ ํจ์จ์ ์ผ๋ก ์๊ฐ์ ์ฌ์ฉํ  ์ ์์์ ๊ฒ ๊ฐ์๋ฐ ๋ค๋ค ์ฒ์์ด๋ค๋ณด๋ ์กฐ๊ธ ์ด๋ ค์ ๋ค.
3. ๋ชจ๋ธ ํ์ต ์๋์ ์ ์ฝ์ผ๋ก ๋ ๋ง์ ์์ ์คํ์ ํ์ง ๋ชปํ๋ค.
4. ๋ง์ง๋ง Ensemble ๋จ๊ณ์์ ์ ์ถ ํ์ผ์ ์ฉ๋ ๋ฐ ์๋ฒ ์๋ ์ด์๋ก, ๊ณํํ๋ ์ ๋ต์ ๋ฐํ์ผ๋ก ์งํํ ์คํ์ ๊ฒฐ๊ณผ๋ฅผ ์ ์ถํ์ง ๋ชปํ๋ค.
5. EDA๋ฅผ ์ข ๋ ๊ตฌ์ฒด์ ์ด๊ณ  ์ธ๋ถ์ ์ผ๋ก ํ์ผ๋ฉด Data๋ฅผ ์ ํ์ํ์ ๊ฒ์ด๊ณ  ๊ทธ์ ๋ฐ๋ฅธ ์ถ๊ฐ์ ์ธ ์ ๋ต์ ์ธ์ธ ์ ์์์ ๊ฒ ๊ฐ๋ค.
6. ๋ชจ๋ธ ์์ธก ๊ฒฐ๊ณผ์ ์ถฉ๋ถํ ๋ถ์๊ณผ ๋ชจ๋ธ ๊ตฌ์กฐ์ ๋ํ ๊ณ ๋ ค ์์ด mAP๋ง ๋ณด๊ณ  ๋ฌธ์ ๋ฅผ ์ ์ํ๋ค๋ณด๋ ๋ณธ์ง์ ์ธ ๋ฌธ์ ์ ์ ๊ทผํ์ง ๋ชปํด์, ์คํ ๊ฒฐ๊ณผ๋ค์ ํ๋์ ๊ฒฐ๊ณผ๋ก ์๋ ด์ํค์ง ๋ชปํ ๊ฒ ๊ฐ๋ค.
7. ์ถฉ๋ถํ Augmentation ์คํ์ ํ๋ค๊ณ  ์๊ฐ๋์ง๋ง ํจ๊ณผ์ ์ธ ๋ฐฉ๋ฒ์ ์ฐพ์ง ๋ชปํ ๊ฒ ๊ฐ๋ค.
8. ๊ณํ ๋ฐ ๊ด๋ฆฌ ๋ฐฉ๋ฒ์ ๋ํด ๋ง์ ์ด์ผ๊ธฐ๋ฅผ ๋๋ด์ง๋ง ๊ทธ๋งํผ์ ํจ์จ์ ๋ด์ง๋ ๋ชปํ ๊ฒ ๊ฐ๋ค.

### ํ๋ก์ ํธ๋ฅผ ํตํด ๋ฐฐ์ด ์ 

1. ๋ชจ๋  ์์ฌ๊ฒฐ์ ์ ๋๋,์ถ์ธก์ด ์๋ ์คํ ์งํ ํ ๊ฒฐ๊ณผ๋ฅผ ๋ถ์ ํ ํ ์ด๋ฅผ ๊ธฐ๋ฐ์ผ๋ก ํด์ผ์ง ํฉ๋นํ๊ณ  ์ฌ๋ฐ๋ฅธ ์์ฌ๊ฒฐ์ ์ด ๊ฐ๋ฅํ๋ค.
2. Detection Task์์ ๊ฐ์ค์ ์ธ์ฐ๊ณ  ์คํ์ ํ๋ ๋ฐ์ ๋ง์ ์๊ฐ์ด ์์๋๊ธฐ ๋๋ฌธ์, ์คํ์ ์๋, ๊ฒ์ฆํ๋ ๊ณผ์ ์ ๋น ๋ฅด๊ฒ ๊ฑฐ์น๋ ๊ฒ์ด ์ค์ํด ๋ณด์ธ๋ค. 
3. ์๊ฐ๋ณด๋ค ๋ง์ ๊ธฐ๋ฅ์ด ๋ผ์ด๋ธ๋ฌ๋ฆฌ ๋ด๋ถ์ ๊ตฌํ๋์ด ์๋ ๊ฒฝ์ฐ๊ฐ ๋ง์, ์ด๋ฅผ ์ ํ์ฉํ๋ฉด ์๊ฐ ๋จ์ถ์ ํ  ์ ์์ผ๋ ๊ด๋ จ ๋ฌธ์๋ฅผ ์ ์ฝ์ด๋ณด๋ ๊ฒ์ด ์ค์ํ๋ค.
***
### Folder Structure ๐
```
๐ level2_objectdetection_cv-level2-cv-01
โ      
โโโ ๐ mmdetection
โ      โ
โ      โโโ ๐ config
โ      โ     โ 
โ      โ     โโโ ๐ __base__
โ      โ     โ    โโโ ๐ datasets
โ      โ     โ    โ    โโโ ๐ coco_detection.py
โ      โ     โ    โ    โโโ ๐ coco_detection_classbalanceddataset.py
โ      โ     โ    โ    โโโ ๐ coco_detection_cutout.py
โ      โ     โ    โ    โโโ ๐ coco_detection_heavy.py
โ      โ     โ    โ    โโโ ๐ coco_detection_mixup.py
โ      โ     โ    โ    โโโ ๐ coco_detection_mosaic.py
โ      โ     โ    โ    โโโ ...
โ      โ     โ    โโโ ๐ models
โ      โ     โ    โ    โโโ ๐ faster_rcnn_r50_fpn.py
โ      โ     โ    โ    โโโ ๐ faster_rcnn_r50_fpn_ciou.py
โ      โ     โ    โ    โโโ ๐ faster_rcnn_r50_fpn_diou.py
โ      โ     โ    โ    โโโ ...
โ      โ     โ    โโโ ๐ schedules
โ      โ     โ    โ    โโโ ๐ schedule_1x.py
โ      โ     โ    โโโ ๐ default_runtime.py
โ      โ     โ 
โ      โ     โโโ ๐ atss_swin-l-p4-w12_fpn_dyhead_mstrain_2x_coco.py
โ      โ     โโโ ๐ faster_rcnn_r50.py
โ      โ     โโโ ๐ faster_rcnn_swin.py
โ      โ     โโโ ๐ swin_large_dyhead_base.py
โ      โ     โโโ ...
โ      โ
โ      โโโ ๐ mmdet
โ      โ
โ      โโโ ๐ tools
โ           โโโ ๐ train.py
โ           โโโ ๐ test.py
โ           โโโ ๐ test_csv.py
โ           โโโ ...
โ
โโโ ๐ submission
โ     โโโ...
โ
โโโ ๐ utility
โ     โโโ ๐ convert2Yolo
โ     โ     โโโ example.py
โ     โ     โโโ...
โ     โโโ ๐ CV_strategy.ipynb
โ     โโโ ๐ EDA.ipynb
โ     โโโ ๐ confusion_matrix.py
โ     โโโ ๐ csv_csv.ipynb
โ     โโโ ๐ csv_json.ipynb
โ     โโโ ๐ ensemble.ipynb
โ     โโโ ๐ image_split.ipynb
โ     โโโ ๐ modify_precision.ipynb
โ     โโโ ๐ pseudolabeling.ipynb
โ     โโโ ๐ split_for_yolodata.ipynb
โ     โโโ ๐ tile_combine.ipynb
โ      
โโโ ๐ yolov5
โ    โ
โ    โโโ ๐ data
โ    โ    โโโ ๐ hyps
โ    โ    โ    โโโ ๐ hyp.scratch_high.yaml
โ    โ    โ    โโโ ๐ hyp.custom.yaml
โ    โ    โ    โโโ ...
โ    โ    โโโ ๐ custom_data.yaml
โ    โ    โโโ ๐ custom_data_fold1.yaml
โ    โ    โโโ ...
โ    โ 
โ    โโโ ๐ models
โ    โ    โโโ ๐ yolo.py
โ    โ    โโโ ๐ yolo5l-custom.yaml
โ    โ    โโโ ...
โ    โ    
โ    โโโ ๐ utils
โ    โ    โโโ ...
โ    โ    
โ    โโโ ๐ train.py
โ    โโโ ๐ hubconf.py
โ    โโโ ๐ inference.ipynb
โ    โโโ ...
โ
โโโ ๐ yolov7
     โ
     โโโ ๐ cfg
     โ    โโโ ๐ baseline
     โ    โ    โโโ ๐ yolor-w6.yaml
     โ    โ    โโโ ๐ yolov3.yaml
     โ    โ    โโโ ...
     โ    โโโ ๐ deploy
     โ    โ    โโโ ๐ yolov7-w6.yaml
     โ    โ    โโโ ๐ yolov7.yaml
     โ    โ    โ    โโโ ...
     โ    โโโ ๐ training
     โ    โ    โโโ ๐ yolov7-w6.yaml
     โ    โ    โโโ ๐ yolov7.yaml
     โ    โ    โโโ ...
     โโโ ๐ data
     โ    โโโ ๐ coco.yaml
     โ    โโโ ๐ hyp.scratch.custom.yaml
     โ    โโโ ...
     โโโ ๐ models
     โ    โโโ ๐ yolo.py
     โ    โโโ ...
     โ    
     โโโ ๐ utils
     โ    โโโ ...
     โ    
     โโโ ๐ train.py
     โโโ ๐ train_aux.py
     โโโ ๐ hubconf.py
     โโโ ๐ inference.ipynb
     โโโ ...    

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
        configs/{config ํ์ผ๋ช}
```
#### Step 3. : Test
```bash
python tools/test_csv.py \
        configs/{config ํ์ผ๋ช} \
        work_dirs/{config ํ์ผ๋ช}/{checkpoint ํ์ผ๋ช} \
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

