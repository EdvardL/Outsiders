from python import Packer, Bin, Item, Painter
import time
start = time.time()

packer = Packer()

# self, partno, WHD, max_weight,put_type=1
bin = Bin(partno=794381, WHD=(1250, 2100, 1800), max_weight=8000000, put_type=0)
packer.addBin(bin)
# self, partno,typeof, WHD, weight, level, updown, color
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(250, 400, 700), weight=200, level=1, updown=True, color='red'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(250, 400, 700), weight=200, level=1, updown=True, color='red'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(250, 400, 700), weight=200, level=1, updown=True, color='red'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(250, 400, 700), weight=200, level=1, updown=True, color='red'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(250, 400, 700), weight=200, level=1, updown=True, color='red'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(250, 400, 700), weight=200, level=1, updown=True, color='red'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(250, 400, 700), weight=200, level=1, updown=True, color='red'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(50, 100, 800), weight=200, level=1, updown=True, color='blue'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(50, 100, 800), weight=200, level=1, updown=True, color='blue'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(50, 100, 800), weight=200, level=1, updown=True, color='blue'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(50, 100, 800), weight=200, level=1, updown=True, color='blue'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(50, 100, 800), weight=200, level=1, updown=True, color='blue'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(50, 100, 800), weight=200, level=1, updown=True, color='blue'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(50, 100, 800), weight=200, level=1, updown=True, color='blue'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(50, 100, 800), weight=200, level=1, updown=True, color='blue'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(50, 100, 800), weight=200, level=1, updown=True, color='blue'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(50, 100, 800), weight=200, level=1, updown=True, color='blue'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(50, 100, 800), weight=200, level=1, updown=True, color='blue'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(500, 900, 800), weight=200, level=1, updown=True, color='yellow'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(500, 900, 800), weight=200, level=1, updown=True, color='yellow'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(500, 900, 800), weight=200, level=1, updown=True, color='yellow'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(500, 900, 800), weight=200, level=1, updown=True, color='yellow'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(500, 900, 800), weight=200, level=1, updown=True, color='yellow'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(500, 900, 800), weight=200, level=1, updown=True, color='yellow'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(500, 900, 800), weight=200, level=1, updown=True, color='yellow'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(500, 900, 800), weight=200, level=1, updown=True, color='yellow'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(300, 400, 600), weight=200, level=1, updown=True, color='purple'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(300, 400, 600), weight=200, level=1, updown=True, color='purple'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(300, 400, 600), weight=200, level=1, updown=True, color='purple'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(300, 400, 600), weight=200, level=1, updown=True, color='purple'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(300, 400, 600), weight=200, level=1, updown=True, color='purple'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(300, 400, 600), weight=200, level=1, updown=True, color='purple'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(300, 400, 600), weight=200, level=1, updown=True, color='purple'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(300, 400, 600), weight=200, level=1, updown=True, color='purple'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(300, 400, 600), weight=200, level=1, updown=True, color='purple'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(300, 400, 600), weight=200, level=1, updown=True, color='purple'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(300, 400, 600), weight=200, level=1, updown=True, color='purple'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))
packer.addItem(Item(partno='12043Y1', typeof='cube', WHD=(150, 200, 100), weight=200, level=1, updown=True, color='green'))

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
stop = time.time()
print('used time : ',stop - start)

# draw results
painter = Painter(b)
painter.plotBoxAndItems()