'''
Create digitStruct.json for SVHM dataset.
digitStruct.json is for parsing to voc format.
'''

# Imports
import os
import h5py
import json

from config import *


# Get image name.
def get_img_name(f, names, idx=0):
    img_name = ''.join(map(chr, f[names[idx][0]][()].flatten()))

    return(img_name)


# Get bounding boxes of an image, including [height, left, top, width, label] info.
def get_img_boxes(f, bboxs, idx=0):
    """
    get the 'height', 'left', 'top', 'width', 'label' of bounding boxes of an image
    :param f: h5py.File
    :param idx: index of the image
    :return: dictionary
    """
    bbox_prop = ['height', 'left', 'top', 'width', 'label']
    meta = {key : [] for key in bbox_prop}

    box = f[bboxs[idx][0]]
    for key in box.keys():
        if box[key].shape[0] == 1:
            meta[key].append(int(box[key][0][0]))
        else:
            for i in range(box[key].shape[0]):
                meta[key].append(int(f[box[key][i][0]][()].item()))

    return meta


def main():
    mat_file_dir = TRAIN_DIR + 'digitStruct.mat'
    mat_file = h5py.File(mat_file_dir, 'r')
    names = mat_file['digitStruct/name']
    bboxs = mat_file['digitStruct/bbox']
    max = names.shape[0]
    print(names)

    img_infos = {}
    for idx in range(max):
        img_file = get_img_name(mat_file, names, idx)
        img_infos[img_file] = get_img_boxes(mat_file, bboxs, idx)
    # Write img_infos to json file.
    with open(TRAIN_DIR + 'digitStruct.json', "w") as outfile:
        json.dump(img_infos, outfile)


if __name__ == '__main__':
	main()
