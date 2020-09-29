#!/usr/bin/env python3
import os
import shutil
from PIL import Image
print("Start")

def loadArr(filename):
    result_arr = {}
    fh = open(filename, 'r')
    for line in fh:
        line = line.strip()
        arr = line.split(' ')
        arr = [ x.strip() for x in arr]
        result_arr[arr[0]] = " ".join(arr[1:])
    fh.close()
    return result_arr

def strToIntTuple(s):
    arr = s.split(" ")
    arr = [ int(x.strip()) for x in arr]
    return arr
    
images_family_val = loadArr('data/images_family_val.txt')
images_manufacturer_val = loadArr('data/images_manufacturer_val.txt')
images_variant_val = loadArr('data/images_variant_val.txt')
images_boxes = loadArr('data/images_box.txt')
keys = images_family_val.keys()
path = os.path.join('data2')
if not os.path.exists(path):
     os.mkdir(path, 0o0777)
path = os.path.join('data2', 'training')
if not os.path.exists(path):
     os.mkdir(path, 0o0777)
path = os.path.join('data2', 'testing')
if not os.path.exists(path):
     os.mkdir(path, 0o0777)


for k in keys:
    print(k)
    name = "{} {} {}".format(images_manufacturer_val[k], images_family_val[k], images_variant_val[k].replace('/','-'))
    if images_family_val[k] == images_variant_val[k]:
        name = "{} {}".format(images_manufacturer_val[k], images_variant_val[k].replace('/','-'))
        if images_variant_val[k].startswith(images_manufacturer_val[k]):
            name = images_variant_val[k].replace('/','-')
    path = os.path.join('data2','training', name)
    if not os.path.exists(path):
         os.mkdir(path, 0o0777)
    path = os.path.join('data2','testing', name)
    if not os.path.exists(path):
         os.mkdir(path, 0o0777)
    src_file = os.path.join('data', 'images', k+".jpg")
    dest_file = os.path.join('data2', 'training', name, k+".jpg")
    im = Image.open(src_file)
    im = im.crop(strToIntTuple(images_boxes[k]))
    im.save(dest_file, "JPEG", quality=100, optimize=False, progressive=False)