import json

json_file = 'mpii_annotations.json'
with open(json_file) as f:
    ann = json.load(f)
res = []
for item in ann:
    if item['numOtherPeople'] != 0 and item['people_index'] <= item['numOtherPeople']:
        continue
    tmp = {}
    tmp['path'] = item['img_paths']
    tmp['isVal'] = int(item['isValidation'])
    tmp['width'] = item['img_width']
    tmp['height'] = item['img_height']
    tmp['joints'] = []
    tmp['annlist_index'] = item['annolist_index']
    tmp['numPeople'] = int(item['numOtherPeople']) + 1
    if item['numOtherPeople'] != 0:
        for i in range(tmp['numPeople'] - 1):
            tmp['joints'].append(item['joint_others'][i])
    tmp['joints'].append(item['joint_self'])
    res.append(tmp)
print(len(res))
with open('res_.json', 'w') as res_file:
    json.dump(res, res_file)


