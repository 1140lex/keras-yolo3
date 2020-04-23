import json
from collections import defaultdict

name_box_id = defaultdict(list)
id_name = dict()
f = open(
    "./output/coco_annotations.json")
data = json.load(f)

annotations = data['annotations']
for ant in annotations:
    id = ant['image_id']
    name = './output/' + data['images'][id]['file_name']
    cat = ant['category_id']

    name_box_id[name].append([ant['bbox'], cat])

f = open('train.txt', 'w')
for key in name_box_id.keys():
    f.write(key)
    box_infos = name_box_id[key]
    for info in box_infos:
        x_min = int(info[0][0])
        y_min = int(info[0][1])
        x_max = x_min + int(info[0][2])
        y_max = y_min + int(info[0][3])

        box_info = " %d,%d,%d,%d,%d" % (
            x_min, y_min, x_max, y_max, int(info[1]))
        f.write(box_info)
    f.write('\n')
f.close()
