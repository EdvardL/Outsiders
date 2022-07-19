from .constants import RotationType, Axis
from .auxiliary_methods import intersect, set2Decimal
import numpy as np
# required to plot a representation of Bin and contained items 
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
DEFAULT_NUMBER_OF_DECIMALS = 0
START_POSITION = [0, 0, 0]


class Item:
    def __init__(self, partno, ZYX, weight, level, color='yellow', updown=True, typeof='cube'):
        ''' '''
        self.partno = partno
        self.typeof = typeof
        self.width = ZYX['width']
        self.height = ZYX['height']
        self.length = ZYX['length']
        self.weight = weight
        # Packing Priority level ,choose 1-3
        self.level = level
        # Upside down? True or False
        self.updown = updown if typeof == 'cube' else False
        # Draw item color
        self.color = color
        self.rotation_type = 0
        self.position = START_POSITION
        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS

    def formatNumbers(self, number_of_decimals):
        ''' '''
        self.width = set2Decimal(self.width, number_of_decimals)
        self.height = set2Decimal(self.height, number_of_decimals)
        self.length = set2Decimal(self.length, number_of_decimals)
        self.weight = set2Decimal(self.weight, number_of_decimals)
        self.number_of_decimals = number_of_decimals

    def string(self):
        ''' '''
        return "%s(%sx%sx%s, weight: %s) pos(%s) rt(%s) vol(%s)" % (
            self.partno, self.width, self.height, self.length, self.weight,
            self.position, self.rotation_type, self.getVolume()
        )

    def getVolume(self):
        ''' '''
        return set2Decimal(self.width * self.height * self.length, self.number_of_decimals)

    def getMaxArea(self):
        ''' '''
        a = sorted([self.width,self.height,self.length],reverse=True) if self.updown == True else [self.width,self.height,self.length]
    
        return set2Decimal(a[0] * a[1] , self.number_of_decimals)

    def getDimension(self):
        ''' rotation type '''
        if self.rotation_type == RotationType.RT_ZYX:
            dimension = [self.width, self.height, self.length]
        elif self.rotation_type == RotationType.RT_XZY:
            dimension = [self.height, self.width, self.length]
        elif self.rotation_type == RotationType.RT_XYZ:
            dimension = [self.height, self.length, self.width]
        elif self.rotation_type == RotationType.RT_YXZ:
            dimension = [self.length, self.height, self.width]
        elif self.rotation_type == RotationType.RT_YZX:
            dimension = [self.length, self.width, self.height]
        elif self.rotation_type == RotationType.RT_ZXY: #############
            dimension = [self.width, self.length, self.height]
        else:
            dimension = []

        return dimension


class Bin:
    def __init__(self, partno, ZYX,put_type=1):
        ''' '''
        self.partno = partno
        self.width = ZYX['width']
        self.length = ZYX['length']
        self.height = ZYX['height']
        self.items = []
        self.fit_items = np.array([[0,ZYX['length'],0,ZYX['height'],0,0]])
        self.unfitted_items = []
        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS
        self.fix_point = False
        self.put_type = put_type
        # used to put gravity distribution
        self.gravity = []

    def formatNumbers(self, number_of_decimals):
        ''' '''
        self.width = set2Decimal(self.width, number_of_decimals)
        self.height = set2Decimal(self.height, number_of_decimals)
        self.length = set2Decimal(self.length, number_of_decimals)
        self.number_of_decimals = number_of_decimals

    def string(self):
        ''' '''
        return "%s(%sx%sx%s) vol(%s)" % (
            self.partno, self.width, self.height, self.length,
            self.getVolume()
        )

    def getVolume(self):
        ''' '''
        return set2Decimal(
            self.width * self.height * self.length, self.number_of_decimals
        )

    def putItem(self, item, pivot,axis=None):
        ''' put item in bin '''
        fit = False
        valid_item_position = item.position
        item.position = pivot
        rotate = RotationType.ALL if item.updown == True else RotationType.Notupdown
        for i in range(0, len(rotate)):
            item.rotation_type = i
            dimension = item.getDimension()
            # rotatate
            if (
                self.width < pivot[0] + dimension[0] or
                self.height < pivot[1] + dimension[1] or
                self.length < pivot[2] + dimension[2]
            ):
                continue

            fit = True

            for current_item_in_bin in self.items:
                if intersect(current_item_in_bin, item):
                    fit = False
                    break

            if fit:
                if self.fix_point == True :
                        
                    [w,h,d] = dimension
                    [x,y,z] = [float(pivot[0]),float(pivot[1]),float(pivot[2])]

                    for i in range(3):
                        # fix height
                        y = self.checkHeight([x,x+float(w),y,y+float(h),z,z+float(d)])
                        # fix width
                        x = self.checkWidth([x,x+float(w),y,y+float(h),z,z+float(d)])
                        # fix length
                        z = self.checkLength([x,x+float(w),y,y+float(h),z,z+float(d)])

                    self.fit_items = np.append(self.fit_items,np.array([[x,x+float(w),y,y+float(h),z,z+float(d)]]),axis=0)
                    item.position = [set2Decimal(x),set2Decimal(y),set2Decimal(z)]
                    
                self.items.append(item)

            if not fit:
                item.position = valid_item_position

            return fit

        if not fit:
            item.position = valid_item_position

        return fit

    def checkLength(self,unfix_point):
        ''' fix item position z '''
        z_ = [[0,0],[float(self.length),float(self.length)]]
        for j in self.fit_items:
            # creat x set
            x_bottom = set([i for i in range(int(j[0]),int(j[1]))])
            x_top = set([i for i in range(int(unfix_point[0]),int(unfix_point[1]))])
            # creat y set
            y_bottom = set([i for i in range(int(j[2]),int(j[3]))])
            y_top = set([i for i in range(int(unfix_point[2]),int(unfix_point[3]))])
            # find intersection on x set and y set.
            if len(x_bottom & x_top) != 0 and len(y_bottom & y_top) != 0 :
                z_.append([float(j[4]),float(j[5])])
        top_length = unfix_point[5] - unfix_point[4]
        # find diff set on z_.
        z_ = sorted(z_, key = lambda z_ : z_[1])
        for j in range(len(z_)-1):
            if z_[j+1][0] -z_[j][1] >= top_length:
                return z_[j][1]
        return unfix_point[4]

    def checkWidth(self,unfix_point):
        ''' fix item position x ''' 
        x_ = [[0,0],[float(self.width),float(self.width)]]
        for j in self.fit_items:
            # creat z set
            z_bottom = set([i for i in range(int(j[4]),int(j[5]))])
            z_top = set([i for i in range(int(unfix_point[4]),int(unfix_point[5]))])
            # creat y set
            y_bottom = set([i for i in range(int(j[2]),int(j[3]))])
            y_top = set([i for i in range(int(unfix_point[2]),int(unfix_point[3]))])
            # find intersection on z set and y set.
            if len(z_bottom & z_top) != 0 and len(y_bottom & y_top) != 0 :
                x_.append([float(j[0]),float(j[1])])
        top_width = unfix_point[1] - unfix_point[0]
        # find diff set on x_bottom and x_top.
        x_ = sorted(x_,key = lambda x_ : x_[1])
        for j in range(len(x_)-1):
            if x_[j+1][0] -x_[j][1] >= top_width:
                return x_[j][1]
        return unfix_point[0]
    
    def checkHeight(self,unfix_point):
        '''fix item position y '''
        y_ = [[0,0],[float(self.height),float(self.height)]]
        for j in self.fit_items:
            # creat x set
            x_bottom = set([i for i in range(int(j[0]),int(j[1]))])
            x_top = set([i for i in range(int(unfix_point[0]),int(unfix_point[1]))])
            # creat z set
            z_bottom = set([i for i in range(int(j[4]),int(j[5]))])
            z_top = set([i for i in range(int(unfix_point[4]),int(unfix_point[5]))])
            # find intersection on x set and z set.
            if len(x_bottom & x_top) != 0 and len(z_bottom & z_top) != 0 :
                y_.append([float(j[2]),float(j[3])])
        top_height = unfix_point[3] - unfix_point[2]
        # find diff set on y_bottom and y_top.
        y_ = sorted(y_,key = lambda y_ : y_[1])
        for j in range(len(y_)-1):
            if y_[j+1][0] -y_[j][1] >= top_height:
                return y_[j][1]

        return unfix_point[2]

    def clearBin(self):
        ''' clear item which in bin '''
        self.items = []
        self.fit_items = np.array([[0,self.width,0,self.height,0,0]])
        return


class Packer:
    def __init__(self):
        ''' '''
        self.bins = []
        self.items = []
        self.unfit_items = []
        self.total_items = 0
        self.binding = []
        
    def addBin(self, bin):
        ''' '''
        return self.bins.append(bin)

    def addItem(self, item):
        ''' '''
        self.total_items = len(self.items) + 1

        return self.items.append(item)

    def pack2Bin(self, bin, item,fix_point):
        ''' pack item to bin '''
        fitted = False
        bin.fix_point = fix_point

        if not bin.items:
            response = bin.putItem(item, item.position)

            if not response:
                bin.unfitted_items.append(item)
            return

        for axis in range(0, 3):
            items_in_bin = bin.items
            for ib in items_in_bin:
                pivot = [0, 0, 0]
                w, h, d = ib.getDimension()
                if axis == Axis.WIDTH:
                    pivot = [ib.position[0] + w,ib.position[1],ib.position[2]]
                elif axis == Axis.HEIGHT:
                    pivot = [ib.position[0],ib.position[1],ib.position[2] + d]
                elif axis == Axis.LENGTH:
                    pivot = [ib.position[0],ib.position[1] + h,ib.position[2]]
                    
                if bin.putItem(item, pivot, axis):
                    fitted = True
                    break
            if fitted:
                break
        if not fitted:
            bin.unfitted_items.append(item)

    def putOrder(self):
        self.items.sort(key=lambda item: item.position[1], reverse=False)
        self.items.sort(key=lambda item: item.position[2], reverse=False)
        self.items.sort(key=lambda item: item.position[0], reverse=False)
        return

    def pack(self, bigger_first=False,distribute_items=False,fix_point=True,binding=[],number_of_decimals=DEFAULT_NUMBER_OF_DECIMALS):
        '''pack master func '''
        # set decimals
        for bin in self.bins:
            bin.formatNumbers(number_of_decimals)

        for item in self.items:
            item.formatNumbers(number_of_decimals)
            
        self.bins.sort(key=lambda bin: bin.getVolume(), reverse=bigger_first)
        self.items.sort(key=lambda item: item.getVolume(), reverse=bigger_first)

        for bin in self.bins:
            # pack item to bin
            for item in self.items:
                self.pack2Bin(bin, item,fix_point)
            # no used
            if distribute_items :
                for item in bin.items:
                    self.items.remove(item)

            for item in self.items.copy():
                if item in bin.unfitted_items:
                    self.items.remove(item)

            if binding != []:
                # resorted
                self.items.sort(key=lambda item: item.getVolume(), reverse=bigger_first)
                self.items.sort(key=lambda item: item.level, reverse=False)
                self.items = self.items + bin.unfitted_items
                # clear bin
                bin.items = []
                bin.unfitted_items = self.unfit_items
                bin.fit_items = np.array([[0,bin.width,0,bin.height,0,0]])
                # repacking
                for item in self.items:
                    self.pack2Bin(bin, item,fix_point)
        # put order of items
        self.putOrder()

class Painter:
    def __init__(self,bins):
        ''' '''
        self.items = bins.items
        self.width = bins.width
        self.height = bins.height
        self.length = bins.length

    def _plotCube(self, ax, x, y, z, dx, dy, dz, color='red',mode=2):
        """ Auxiliary function to plot a cube. code taken somewhere from the web.  """
        xx = [x, x, x+dx, x+dx, x]
        yy = [y, y+dy, y+dy, y, y]
        
        kwargs = {'alpha': 1, 'color': color,'linewidth':1 }
        if mode == 1 :
            ax.plot3D(xx, yy, [z]*5, **kwargs)
            ax.plot3D(xx, yy, [z+dz]*5, **kwargs)
            ax.plot3D([x, x], [y, y], [z, z+dz], **kwargs)
            ax.plot3D([x, x], [y+dy, y+dy], [z, z+dz], **kwargs)
            ax.plot3D([x+dx, x+dx], [y+dy, y+dy], [z, z+dz], **kwargs)
            ax.plot3D([x+dx, x+dx], [y, y], [z, z+dz], **kwargs)
        else :
            p = Rectangle((x,y),dx,dy,fc=color,ec='black')
            p2 = Rectangle((x,y),dx,dy,fc=color,ec='black')
            p3 = Rectangle((y,z),dy,dz,fc=color,ec='black')
            p4 = Rectangle((y,z),dy,dz,fc=color,ec='black')
            p5 = Rectangle((x,z),dx,dz,fc=color,ec='black')
            p6 = Rectangle((x,z),dx,dz,fc=color,ec='black')
            ax.add_patch(p)
            ax.add_patch(p2)
            ax.add_patch(p3)
            ax.add_patch(p4)
            ax.add_patch(p5)
            ax.add_patch(p6)
            art3d.pathpatch_2d_to_3d(p, z=z, zdir="z")
            art3d.pathpatch_2d_to_3d(p2, z=z+dz, zdir="z")
            art3d.pathpatch_2d_to_3d(p3, z=x, zdir="x")
            art3d.pathpatch_2d_to_3d(p4, z=x + dx, zdir="x")
            art3d.pathpatch_2d_to_3d(p5, z=y, zdir="y")
            art3d.pathpatch_2d_to_3d(p6, z=y + dy, zdir="y")

    def plotBoxAndItems(self,title=""):
        """ side effective. Plot the Bin and the items it contains. """
        fig = plt.figure()
        axGlob = plt.axes(projection='3d')

        counter = 0
        # fit rotation type
        for item in self.items:
            rt = item.rotation_type  
            x,y,z = item.position
            [w,h,d] = item.getDimension()
            color = item.color
            if item.typeof == 'cube':
                 # plot item of cube
                self._plotCube(axGlob, float(x), float(y), float(z), float(w),float(h),float(d),color=color,mode=2)
            elif item.typeof == 'cylinder':
                # plot item of cylinder
                self._plotCylinder(axGlob, float(x), float(y), float(z), float(w),float(h),float(d),color=color,mode=2)
            
            counter = counter + 1  
        # plot bin 
        self._plotCube(axGlob,0, 0, 0, float(self.width), float(self.height), float(self.length),color='black',mode=1)

        plt.title('result')
        self.setAxesEqual(axGlob)
        plt.show()

    def setAxesEqual(self,ax):
        '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
        cubes as cubes, etc..  This is one possible solution to Matplotlib's
        ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

        Input
        ax: a matplotlib axis, e.g., as output from plt.gca().'''
        x_limits = ax.get_xlim3d()
        y_limits = ax.get_ylim3d()
        z_limits = ax.get_zlim3d()

        x_range = abs(x_limits[1] - x_limits[0])
        x_middle = np.mean(x_limits)
        y_range = abs(y_limits[1] - y_limits[0])
        y_middle = np.mean(y_limits)
        z_range = abs(z_limits[1] - z_limits[0])
        z_middle = np.mean(z_limits)

        # The plot bounding box is a sphere in the sense of the infinity
        # norm, hence I call half the max range the plot radius.
        plot_radius = 0.5 * max([x_range, y_range, z_range])

        ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
        ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
        ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

