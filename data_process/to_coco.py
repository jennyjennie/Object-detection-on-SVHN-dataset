#!/usr/bin/python

# pip install lxml

import sys
import os
import json
import glob
import matplotlib.image

START_BOUNDING_BOX_ID = 1
# If necessary, pre-define category and its id
PRE_DEFINE_CATEGORIES = {"1": 1, "2": 2, "3": 3, "4": 4,
                         "5":5, "6": 6, "7": 7, "8": 8, "9": 9,
                         "10": 10}


def convert_train(data, json_file):
    json_dict = {"images": [], "annotations": [], "categories": []}
    # Bounding box info in mat file.
    bbox_info = ["height", "left", "top", "width", "label"]
    categories = PRE_DEFINE_CATEGORIES
    bnd_id = START_BOUNDING_BOX_ID
    for img_file in data:
        dir = os.path.join(TRAIN_DIR + img_file)
        img = matplotlib.image.imread(dir)

        image_id = int(img_file.strip('.png'))
        height, width = img.shape[0], img.shape[1]
        image = {
            "file_name": img_file,
            "height": height,
            "width": width,
            "id": image_id,
        }
        json_dict["images"].append(image)

        img_info = data[img_file]
        nobjects = len(img_info['label'])
        for idx in range(nobjects):
            height, x, y, width, label = [int(img_info[key][idx]) for key in bbox_info]
            category_id = categories[str(label)]
            ann = {
                "area": width * height,
                "iscrowd": 0,
                "image_id": image_id,
                "bbox": [x, y, width, height],
                "category_id": category_id,
                "id": bnd_id,
                "ignore": 0,
                "segmentation": [],
            }
            json_dict["annotations"].append(ann)
            bnd_id = bnd_id + 1

    for cate, cid in categories.items():
        cat = {"supercategory": "none", "id": cid, "name": cate}
        json_dict["categories"].append(cat)

    os.makedirs(os.path.dirname(json_file), exist_ok=True)
    json_fp = open(json_file, "w")
    json_str = json.dumps(json_dict, indent=4)
    json_fp.write(json_str)
    json_fp.close()


def make_coco_train():
    TRAIN_DIR = '/Users/jenny/Desktop/Visual_HW2/coco/images/'
    mat_file_dir = '/Users/jenny/Desktop/Visual_HW2/VRDL_HW2_RELEASED_DATASET/train'
    mat_file_path = os.path.join(mat_file_dir, 'digitStruct.json')
    with open(mat_file_path,'r',encoding='utf-8') as json_file:
        data = json.load(json_file)
    convert_train(data, '../coco/annotations/train.json')
    print("Success")


def make_coco_test():
    test_dir = '/Users/jenny/Desktop/Visual_HW2/VRDL_HW2_RELEASED_DATASET/test'
    json_dict = {"images": [], "annotations": [], "categories": []}
    categories = PRE_DEFINE_CATEGORIES
    img_names = sorted(os.listdir(test_dir), key=lambda fn:int(fn.strip('.png')))

    for img_name in img_names:
        image_id = int(img_name.strip('.png'))
        image = {
            "file_name": img_name,
            "id": image_id,
        }
        json_dict["images"].append(image)

    for cate, cid in categories.items():
        cat = {"supercategory": "none", "id": cid, "name": cate}
        json_dict["categories"].append(cat)

    json_file_path = '../coco/annotations/test.json'
    os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
    json_fp = open(json_file_path, "w")
    json_str = json.dumps(json_dict, indent=4)
    json_fp.write(json_str)
    json_fp.close()

    print("Success")


if __name__ == "__main__":
    make_coco_test()