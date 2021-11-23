_base_ = [
    '/home/trainer/JennyHo/Visual_HW2/mmdetection/configs/_base_/models/faster_rcnn_r50_fpn.py',
    '/home/trainer/JennyHo/Visual_HW2/mmdetection/configs/_base_/datasets/coco_detection.py',
    '/home/trainer/JennyHo/Visual_HW2/mmdetection/configs/_base_/schedules/schedule_1x.py',
    '/home/trainer/JennyHo/Visual_HW2/mmdetection/configs/_base_/default_runtime.py'
]

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=10),
        ))

dataset_type = 'COCODataset'

classes = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

data = dict(
    train=dict(
        ann_file='/home/trainer/JennyHo/Visual_HW2/mmdetection/coco/annotations/train.json',
        classes=classes,
        img_prefix='/home/trainer/JennyHo/Visual_HW2/mmdetection/coco/images/'),
    val=dict(
        ann_file='/home/trainer/JennyHo/Visual_HW2/mmdetection/coco/annotations/val.json',
        classes=classes,
        img_prefix='/home/trainer/JennyHo/Visual_HW2/mmdetection/coco/images/'),
    test=dict(
        ann_file='/home/trainer/JennyHo/Visual_HW2/mmdetection/coco/annotations/test.json',
        classes=classes,
        img_prefix='/home/trainer/JennyHo/Visual_HW2/mmdetection/test/'))
