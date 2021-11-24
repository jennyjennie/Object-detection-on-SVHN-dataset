# Object-detection-on-SVHN-dataset


## Description

Object detection on SVHN dataset using mmdetection for VRDL HW2

## Requirements

In this project, mmdetection was used. Please refer to [mmdetection](https://github.com/open-mmlab/mmdetection.git) for installation.

To install other requirements:

```setup
pip install -r requirements.txt
```
## Dataset Preparation
#### Prepare annotations
+ Use ```read_mat.py```  to parse the digitStruct.mat
+ Use ```to_coco.py``` to generate train.json and test.json

#### Project structure
```
mmdetection 
└─── coco
│    │
│    └─── annotations
│    │    │  train.json
│    │    |  test.json
│    │
│    └─── images
│         │  1.png
│         |  2.png
│         |  ...
│
└─── VRDL_HW2_config.py
└─── config  
└─── ...
```


## Training

To train the model used in this project, run this command:

```train
cd mmdetection
python tools/train.py VRDL_HW2_config.py
```


## Test

To test the trained model, run:

```test
python tools/test.py VRDL_HW2_config.py  ${CHECKPOINT_FILE} --format-only --options jsonfile_prefix=${JSONFILE_PREFIX}
```
Then run ```prediction_to_json.py``` to get the desired answer.json

---

Or simply run the [inference.ipynb](https://github.com/jennyjennie/Object-detection-on-SVHN-dataset/blob/master/inference.ipynb) to generate answer.json and benchmark the model.

## Pre-trained Models

The pretrained model can be downloaded here:

https://drive.google.com/drive/folders/169dGedQ7nyYgUtvX7s2wwtcf58InXj-Q?usp=sharing

## Results

The model achieves the following performance on :


| Model name         | mAP  | Speed |
| ------------------ |---------------- | -------------- |
| Faster-rcnn   |     0.3930         |     0.2894 (s)      |
