# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:19:36 2021

@author: Casper Kanaar

WI4231 - TDA Assignment - Assignment 1.

"""
# =============================================================================
# Importing relevant modules
import numpy as np 
from matplotlib import pyplot as plt 
from ripser import Rips 

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 22})

# =============================================================================
# Turn on/off plotting 
plotting = True

# =============================================================================
# Importing the data 
data = np.genfromtxt("matrix1.txt", delimiter = ",")

figure_import = plt.figure(figsize = (10,10),dpi = 300)

if plotting == True:
    plt.imshow(data)

# =============================================================================
# Transforming the data to a scatter plot with x and y coordinates between 0 and 1
scatter_coordinates = []

for i in range(len(data)): 
    for j in range(len(data[i])): 
        # if data[i][j] != 0:
        if data[i][j] != 0 and i%2 == 0 and j%2 == 0: 
            """ NOTE!
            There is a cheat in this line: and i%10 == 0 and j%10 == 0
            This is done to circumvent the memory issue for now.
            This creates incorrect results and a solution to this has yet to be found. 
            """
            scatter_coordinates.append([j/len(data[i]),1 - i/len(data)])

scatter_coordinates = np.array(scatter_coordinates)          
scatter_x, scatter_y = scatter_coordinates.reshape(-1,2).T

if plotting == True:   
    figure_scatter = plt.figure(figsize = (10,10),dpi = 300)
    plt.scatter(scatter_x,scatter_y,s = 1, color = "black")  

# =============================================================================
# Generating the persistence diagram and finding the value of epsilon that generates 2 clusters.
rips = Rips(maxdim = 0,thresh = 1)
dgms = rips.fit_transform(scatter_coordinates)
H0_dgm = dgms[0]

if plotting == True:
    figure_persistence = plt.figure(figsize = (10,10), dpi = 300)
    rips.plot(dgms, legend=False, show=False)

# The deat of 2 clusters is at H0_dgm[-2][1], but we are interested in the birth of the 2 clusters, which is when the 3 clusters become 2. This is at: 
epsilon = H0_dgm[-3][1]

# =============================================================================
# Plotting circles with radius epsilon around every point to examplify the clusters. 
if plotting == True: 
    figure_cluster, ax_cluster = plt.subplots(figsize = (10,10),dpi = 300)
    for i in range(len(scatter_x)): 
        circle = plt.Circle((scatter_x[i],scatter_y[i]),epsilon/2,color = 'black',alpha = 0.05)
        ax_cluster.add_patch(circle)




























            