# # 3D
#
#
# # 1基于时间的三维移动
# from gameobjects.vector3 import *
# A = (-6, 2, 2)
# B = (7, 5, 10)
# plasma_speed = 100. # meters per second
# AB = Vector3.from_points(A, B)
# print "Vector to droid is", AB
# distance_to_target = AB.get_magnitude()
# print "Distance to droid is", distance_to_target, "meters"
# plasma_heading = AB.get_normalized()
# print "Heading is", plasma_heading
# #######输出结果#########
# Vector to droid is (13, 3, 8)
# Distance to droid is 15.5563491861 meters
# Heading is (0.835672, 0.192847, 0.514259)


# 2 3D透视(3D坐标映射到2D坐标)
def perspective_project(vector3, d):
    x, y, z = vector3
    # d的意思是视距（viewingdistance），也就是摄像头到3D世界物体在屏幕上的像素体现之间的距离。比如说，一个在(10, 5, 100)的物体移动到了(11, 5,100)，
    # 视距是100的时候，它在屏幕上就刚好移动了1个像素，但如果它的z不是100，或者视距不是100，
    # 那么可能移动距离就不再是1个像素的距离。有些抽象，不过玩过3D游戏的话（这里指国外的3D大作），都有一种滚轮调节远近的功能，这就是视距（当然调的时候视野也会变化，这个下面说）。
    return (x * d/z, -y * d/z)


# 3 视野，视距
from math import tan
def calculate_viewing_distance(fov, screen_width):
    d = (screen_width/2.0) / tan(fov/2.0)
    return d
