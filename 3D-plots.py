#% matplotlib notebook
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os

os.chdir('./python xlsx files')
import pandas as pd
import numpy as np

data = pd.read_excel('197 supraorb python.xlsx')

fig = plt.figure(figsize=plt.figaspect(.8))
ax = fig.add_subplot(1, 1, 1, projection='3d')
# for i in np.unique(data['color_l']):
#    ax.scatter(data['x1_l'][data['color_l'] == i],
#            data['y1_l'][data['color_l'] == i],
#            data['z1_l'][data['color_l'] == i], '-v')  #d=diamond v=triagle o=cercle s=square

## for all points in the xls:
# ax.scatter(data['x1_l'],
#           data['y1_l'],
#           data['z1_l'],
#           s=20,
#           facecolor='C0',
#           edgecolor='C1')


# for single point on in the xls:
ax.scatter(data['x1_l'][0],
           data['y1_l'][0],
           data['z1_l'][0],
           s=20,
           facecolor='C0',
           edgecolor='C1')

# for i in np.unique(data['color_r']):
#    ax.plot(data['x1_r'][data['color_r'] == i],
#            data['y1_r'][data['color_r'] == i],
#            data['z1_r'][data['color_r'] == i],
#            '-d',
#            color='C0',
#           )
for i in [1]:
    ax.plot(data['x1_r'][data['color_r'] == i],
            data['y1_r'][data['color_r'] == i],
            data['z1_r'][data['color_r'] == i],
            '-d',
            color='C0',
            label='ref',
            linewidth=2,
            linestyle='--'
            )
for i in [5]:
    ax.plot(data['x1_r'][data['color_r'] == i],
            data['y1_r'][data['color_r'] == i],
            data['z1_r'][data['color_r'] == i],
            '-o',
            color='C1',
            label='line',
            linewidth=1,
            linestyle='-',
            markersize=3
            )
ax.set_xlabel('X');
ax.set_ylabel('Y');
ax.set_zlabel('Z')
ax.legend()

plt.show()
