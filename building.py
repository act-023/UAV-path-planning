import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

len=100
width=100
h=22
map=np.zeros((len,width,h))
bds = []
class building():
    def __init__(self,x,y,l,w,h):
        self.x=x   #建筑中心x坐标
        self.y=y   #建筑中心y坐标
        self.l=l        #建筑长半值
        self.w=w       #建筑宽半值
        self.h=h    #建筑高度
for i in range(5):
    bds.append(building(random.randint(10, len - 10), random.randint(10, width - 10), random.randint(1, 10),
                 random.randint(1, 10), random.randint(9, 13)))
    # map[bds[i].x - bds[i].l:bds[i].x + bds[i].l,bds[i].y - bds[i].w:bds[i].y + bds[i].w, 0:bds[i].h] = 1
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for ob in bds:
    # 绘画出所有建筑
    x = ob.x
    y = ob.y
    z = 0
    dx = ob.l
    dy = ob.w
    dz = ob.h
    xx = np.linspace(x - dx, x + dx, 2)
    yy = np.linspace(y - dy, y + dy, 2)
    zz = np.linspace(z, z + dz, 2)

    xx2, yy2 = np.meshgrid(xx, yy)

    ax.plot_surface(xx2, yy2, np.full_like(xx2, z))
    ax.plot_surface(xx2, yy2, np.full_like(xx2, z + dz))

    yy2, zz2 = np.meshgrid(yy, zz)
    ax.plot_surface(np.full_like(yy2, x - dx), yy2, zz2)
    ax.plot_surface(np.full_like(yy2, x + dx), yy2, zz2)

    xx2, zz2 = np.meshgrid(xx, zz)
    ax.plot_surface(xx2, np.full_like(yy2, y - dy), zz2)
    ax.plot_surface(xx2, np.full_like(yy2, y + dy), zz2)
plt.savefig('1.jpg')
bds.append(building(random.randint(10, len - 10), random.randint(10, width - 10), random.randint(1, 10),
                 random.randint(1, 10), random.randint(9, 13)))
for ob in bds:
    # 绘画出所有建筑
    x = ob.x
    y = ob.y
    z = 0
    dx = ob.l
    dy = ob.w
    dz = ob.h
    xx = np.linspace(x - dx, x + dx, 2)
    yy = np.linspace(y - dy, y + dy, 2)
    zz = np.linspace(z, z + dz, 2)

    xx2, yy2 = np.meshgrid(xx, yy)

    ax.plot_surface(xx2, yy2, np.full_like(xx2, z))
    ax.plot_surface(xx2, yy2, np.full_like(xx2, z + dz))

    yy2, zz2 = np.meshgrid(yy, zz)
    ax.plot_surface(np.full_like(yy2, x - dx), yy2, zz2)
    ax.plot_surface(np.full_like(yy2, x + dx), yy2, zz2)

    xx2, zz2 = np.meshgrid(xx, zz)
    ax.plot_surface(xx2, np.full_like(yy2, y - dy), zz2)
    ax.plot_surface(xx2, np.full_like(yy2, y + dy), zz2)
plt.savefig('2.jpg')
