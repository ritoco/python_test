import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse #楕円を読み込む

#オブジェクト個数
NUM = 14

#背景色
plt.rcParams['axes.facecolor']  = '#aaaaaa'

#背面の楕円の大きさ、位置
ells = [Ellipse((1.0*i , 1.0*l), 
  width=2.5, height=1.5)
  for i in range(NUM)
  for l in range(NUM)] #NUMで得た個数をforで並べる

#前面の楕円の大きさ、位置
ells2 = [Ellipse((1.0*j , 1.0*k), 
  width=1.0 , height=1.0)
  for j in range(NUM)
  for k in range(NUM)] 


fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
for e in ells:

#背面の楕円
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(1) 
    e.set_facecolor( ( 0.1,  np.random.rand(), np.random.rand()) )#rgb = 3

#前面の楕円
for e2 in ells2:
    ax.add_artist(e2)
    e2.set_clip_box(ax.bbox)
    e2.set_alpha(1) 
    e2.set_facecolor( ( 0.9, np.random.rand(), np.random.rand()) ) #rgb = 3

#敷き詰める範囲
ax.set_xlim(0, 6) 
ax.set_ylim(0, 6)

plt.show()