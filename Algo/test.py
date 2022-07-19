from python import Packer, Bin, Item, Painter
import time
import json


start = time.time()

packer = Packer()

json_file = open("../Data/Input/0/30_cl.json")
data_dict = json.load(json_file)

bin_id = data_dict['cargo_space']['id']
bin_ZXY = data_dict['cargo_space']['size']

# self, partno, ZXY, weight,put_type=1
bin = Bin(partno=bin_id, ZXY=bin_ZXY, put_type=0)
packer.addBin(bin)

for item_data in data_dict['cargo_groups']:
    for i in range(item_data['count']):
        item_id = item_data['group_id']
        item_ZXY = item_data['size']
        item_weight = item_data['mass']
        # self, partno,typeof, ZXY, weight, level, updown, color
        packer.addItem(Item(partno=item_id, typeof='cube', ZXY=item_ZXY, weight=item_weight, level=1, updown=True, color='red'))

packer.pack(bigger_first=True,distribute_items=False,fix_point=True,number_of_decimals=0)

b = packer.bins[0]
volume = b.width * b.height * b.length
print(":::::::::::", b.string())

print("FITTED ITEMS:")
volume_t = 0
volume_f = 0
unfitted_name = ''
for item in b.items:
    print("partno : ",item.partno)
    print("color : ",item.color)
    print("position : ",item.position)
    print("rotation type : ",item.rotation_type)
    print("W*H*D : ",str(item.width) +'*'+ str(item.height) +'*'+ str(item.length))
    print("volume : ",float(item.width) * float(item.height) * float(item.length))
    print("weight : ",float(item.weight))
    volume_t += float(item.width) * float(item.height) * float(item.length)
    print("***************************************************")
print("***************************************************")
print("UNFITTED ITEMS:")
for item in b.unfitted_items:
    print("partno : ",item.partno)
    print("color : ",item.color)
    print("W*H*D : ",str(item.width) +'*'+ str(item.height) +'*'+ str(item.length))
    print("volume : ",float(item.width) * float(item.height) * float(item.length))
    print("weight : ",float(item.weight))
    volume_f += float(item.width) * float(item.height) * float(item.length)
    unfitted_name += '{},'.format(item.partno)
    print("***************************************************")
print("***************************************************")
print('space utilization : {}%'.format(round(volume_t / float(volume) * 100 ,2)))
print('residual volumn : ', float(volume) - volume_t )
print('unpack item : ',unfitted_name)
print('unpack item volume : ',volume_f)
print("gravity distribution : ",b.gravity)
stop = time.time()
print('used time : ',stop - start)

# draw results
painter = Painter(b)
painter.plotBoxAndItems()

packed_cargos_info = [] 
count = 1
for item in b.items:
    dimension = item.getDimension()
    item_info = {}
    item_info["calculated_size"] = {"height": str(dimension[2]), "length": str(dimension[1]), "width": str(dimension[0])}
    item_info["cargo_id"] = item.partno
    item_info["id"] = count
    item_info["mass"] = str(item.weight)
    item_info["position"] = {"x": str(item.position[1]), "y": str(item.position[2]), "z": str(item.position[0])}
    item_info["size"] = {"height": str(item.length), "length": str(item.height), "width": str(item.width)}
    item_info["sort"] = 1
    item_info["stacking"] = True
    item_info["turnover"] = True
    item_info["type"] = "box"
    count += 1
    packed_cargos_info.append(item_info)

print(packed_cargos_info)
unpacked_cargos_info = []

for item in b.unfitted_items:
    item_info = {}
    item_info["group_id"] =  item.partno,
    item_info["id"] = 0,
    item_info["mass"] = str(item.weight),
    item_info["position"] = {"x": -1, "y": -1, "z": -1},
    item_info["size"] = {"height": str(item.width), "length": str(item.height), "width": str(item.length)},
    item_info["sort"] = 1
    item_info["stacking"] = True
    item_info["turnover"] = True
    unpacked_cargos_info.append(item_info)



output_dict = {
"cargoSpace": {
"loading_size": {
"height": bin_ZXY[1],
"length": bin_ZXY[2],
"width": bin_ZXY[0]
},
"position": [
bin_ZXY[1]/2,
bin_ZXY[2]/2,
bin_ZXY[0]/2
],
"type": "pallet"
},
"cargos": packed_cargos_info,
"unpacked": unpacked_cargos_info
}

with open("../Data/Output/30_cl.json", 'w') as fp:
    json.dump(output_dict, fp)
print(output_dict)