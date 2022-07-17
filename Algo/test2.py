import json
import os
from python import Packer, Bin, Item, Painter
import time

def Pack(filename):
    f = open(filename)
    d = json.load(f)
    
    packer = Packer()

    # self, partno, WHD, max_weight,put_type=1
    bin = Bin(partno=d['cargo_space']['id'], 
              WHD=d['cargo_space']['size'],
              max_weight=d['cargo_space']['carrying_capacity'] * 1000,
              put_type=0)
    packer.addBin(bin)
    # self, partno,typeof, WHD, weight, level, updown, color
    for item in d['cargo_groups']:
        packer.addItem(Item(partno=item['id'], 
                            typeof='cube',
                            WHD=item['size'],
                            weight=item['mass'],
                            level=1,
                            updown=item['turnover'],
                            color='red'))
       

    packer.pack(bigger_first=True,distribute_items=False,fix_point=True,number_of_decimals=0)

    b = packer.bins[0]
    volume = b.width * b.height * b.depth
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
        print("W*H*D : ",str(item.width) +'*'+ str(item.height) +'*'+ str(item.depth))
        print("volume : ",float(item.width) * float(item.height) * float(item.depth))
        print("weight : ",float(item.weight))
        volume_t += float(item.width) * float(item.height) * float(item.depth)
        print("***************************************************")
    print("***************************************************")
    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("partno : ",item.partno)
        print("color : ",item.color)
        print("W*H*D : ",str(item.width) +'*'+ str(item.height) +'*'+ str(item.depth))
        print("volume : ",float(item.width) * float(item.height) * float(item.depth))
        print("weight : ",float(item.weight))
        volume_f += float(item.width) * float(item.height) * float(item.depth)
        unfitted_name += '{},'.format(item.partno)
        print("***************************************************")
    print("***************************************************")
    print('space utilization : {}%'.format(round(volume_t / float(volume) * 100 ,2)))
    print('residual volumn : ', float(volume) - volume_t )
    print('unpack item : ',unfitted_name)
    print('unpack item volume : ',volume_f)
    print("gravity distribution : ",b.gravity)

    return b

dirname = 'Data/_vg_85_bgg5jsons'
dirnames = []
filenames = []
for dir in os.listdir(dirname):
    dirnames.append(dirname + '/' + dir)
    for name in os.listdir(dirname + '/' + dir):
        filename = dirname + '/' + dir + '/' + name
        filenames.append(filename)

        start = time.time()

        # b = Pack(filename)

        stop = time.time()
        #print('used time : ',stop - start)

        # draw results
        # painter = Painter(b)
        # painter.plotBoxAndItems()

print(*dirnames, sep='\n')
print(*filenames, sep='\n')