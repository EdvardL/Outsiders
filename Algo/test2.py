import json
import os
from python import Packer, Bin, Item, Painter
import time

def Pack(filename):
    f = open(filename)
    d = json.load(f)
    
    packer = Packer()

    bin_id = d['cargo_space']['id']
    bin_ZXY = d['cargo_space']['size']

    # self, partno, WHD, put_type=1
    bin = Bin(partno=bin_id, ZXY=bin_ZXY, put_type=0)
    packer.addBin(bin)
    # self, partno,typeof, WHD, weight, level, updown, color
    for item in d['cargo_groups']:
        packer.addItem(Item(partno=item['group_id'], 
                            typeof='cube',
                            ZXY=item['size'],
                            weight=item['mass'],
                            level=1,
                            updown=item['turnover'],
                            color='red'))
       

    packer.pack(bigger_first=True,distribute_items=False,fix_point=True,number_of_decimals=0)

    b = packer.bins[0]

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

    with open("../Data/Output/3"+ filename, 'w') as fp:
        json.dump(output_dict, fp)
    print(output_dict)

    return b

dirname = '../Data/Input'
dirnames = []
filenames = []
for dir in os.listdir(dirname):
    dirnames.append(dirname + '/' + dir)
    for name in os.listdir(dirname + '/' + dir):
        filename = dirname + '/' + dir + '/' + name
        filenames.append(filename)

        start = time.time()

        b = Pack(filename)

        stop = time.time()
        print('used time : ',stop - start)

        # draw results
        # painter = Painter(b)
        # painter.plotBoxAndItems()

        

print(*dirnames, sep='\n')
print(*filenames, sep='\n')