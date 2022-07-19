class RotationType:
    RT_ZXY = 0
    RT_XZY = 1
    RT_XYZ = 2
    RT_YXZ = 3
    RT_YZX = 4
    RT_ZYX = 5

    ALL = [RT_ZXY, RT_XZY, RT_XYZ, RT_YXZ, RT_YZX, RT_ZYX]
    # un upright or un updown
    Notupdown = [RT_ZXY,RT_XZY]
 
class Axis:
    WIDTH = 0
    HEIGHT = 1
    LENGTH = 2

    ALL = [WIDTH, HEIGHT, LENGTH]

