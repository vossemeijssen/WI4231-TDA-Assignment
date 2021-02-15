# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:07:29 2021

@author: Casper
"""

import numpy as np 
from matplotlib import pyplot as plt 
from ripser import Rips

scatter_coordinates = np.array([[0,0],[-1,1],[-1,2],[0,3],[1,1],[1,2]])
scatter_x, scatter_y = scatter_coordinates.reshape(-1,2).T

figure_scatter = plt.figure(figsize = (10,10),dpi = 300)
plt.scatter(scatter_x,scatter_y, color = "black") 

rips = Rips(maxdim = 0)
dgms = rips.fit_transform(scatter_coordinates)
H0_dgm = dgms[0]

rips.plot(dgms) 