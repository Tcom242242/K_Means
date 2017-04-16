import yaml
# グラフ化に必要なものの準備
import matplotlib
import matplotlib.pyplot as plt

# データの扱いに必要なライブラリ
import pandas as pd
import numpy as np
import datetime as dt
import pdb
import numpy as np

plt.style.use('ggplot') 
font = {'family' : 'meiryo'}
matplotlib.rc('font',  **font)

f = open("result.yaml")
data = yaml.load(f)
data = np.array(data)

cluster1 = data[0][':v_list']
cluster1_vec = data[0][':vec']
cluster2 = data[1][':v_list']
cluster2_vec = data[1][':vec']
cluster3 = data[2][':v_list']
cluster3_vec = data[2][':vec']

x1 = [v[0] for v in cluster1]
y1 = [v[1] for v in cluster1]
x2 = [v[0] for v in cluster2]
y2 = [v[1] for v in cluster2]
x3 = [v[0] for v in cluster3]
y3 = [v[1] for v in cluster3]


x1_c = cluster1_vec[0]
y1_c = cluster1_vec[1]
x2_c = cluster2_vec[0]
y2_c = cluster2_vec[1]
x3_c = cluster3_vec[0]
y3_c = cluster3_vec[1]


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x1, y1, c = "red")
ax.scatter(x1_c, y1_c, c = "red", s=100)
ax.scatter(x2, y2, c = "blue" )
ax.scatter(x2_c, y2_c, c = "blue", s=100)
ax.scatter(x3, y3, c = "green" )
ax.scatter(x3_c, y3_c, c = "green", s=100)

fig.show()

plt.show()
plt.savefig("result.jpg")
