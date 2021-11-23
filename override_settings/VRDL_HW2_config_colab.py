_base_ = [
    '/content/mmdetection/configs/_base_/models/faster_rcnn_r50_fpn.py',
    '/content/mmdetection/configs/_base_/datasets/coco_detection.py',
    '/content/mmdetection/configs/_base_/schedules/schedule_1x.py',
    '/content/mmdetection/configs/_base_/default_runtime.py'
]

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=10),
        ))

dataset_type = 'COCODataset'

classes = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

data = dict(
    test=dict(
        ann_file='/content/mmdetection/Object-detection-on-SVHN-dataset/annotations/test.json',
        classes=classes,
        img_prefix='/content/mmdetection/test/'))
