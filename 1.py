#!/usr/bin/env python3
import os
import shutil

print("Start")

def loadArr(filename):
    result_arr = {}
    fh = open(filename, 'r')
    for line in fh:
        line = line.strip()
        arr = line.split(' ', 2)
        arr = [ x.strip() for x in arr]
        result_arr[arr[0]] = arr[1]
    fh.close()
    return result_arr
    
images_family_val = loadArr('data/images_family_val.txt')
images_manufacturer_val = loadArr('data/images_manufacturer_val.txt')
images_variant_val = loadArr('data/images_variant_val.txt')
keys = images_family_val.keys()
# print(keys)
for k in keys:
    print(k)
    name = "{} {} {}".format(images_manufacturer_val[k], images_family_val[k], images_variant_val[k].replace('/','-'))
    if images_family_val[k] == images_variant_val[k]:
        name = "{} {}".format(images_manufacturer_val[k], images_variant_val[k].replace('/','-'))
        if images_variant_val[k].startswith(images_manufacturer_val[k]):
            name = images_variant_val[k].replace('/','-')
    path = os.path.join('data2','testing' , name)
    if not os.path.exists(path):
         os.mkdir(path, 0o0777)
    shutil.copyfile(
        os.path.join('data', 'images', k+".jpg"),
        os.path.join('data2','testing', name, k+".jpg")
    )
    print(name)