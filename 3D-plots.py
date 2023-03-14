#%matplotlib notebook
#%matplotlib ipympl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
#os.chdir('/Users/nicolasvv/OneDrive - Vrije Universiteit Brussel/Onderzoek/n occipitalis tertius/microscribe n occ tertius')
os.chdir('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Onderzoek/n occipitalis tertius/microscribe n occ tertius')

data = pd.read_excel('NOT 62_python - 1 side.xlsx')
data

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1,1,1, projection='3d')
for i in np.unique(data['color']):
    ax.plot(data['x1'][data['color'] == i],
            data['y1'][data['color'] == i],
            data['z1'][data['color'] == i], '-o')

ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')

##Aaanpassing 1
