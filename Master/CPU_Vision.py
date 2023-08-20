# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 02:44:28 2023

@author: Aaron
"""

from PIL import Image
from itertools import product
import numpy as np


def get_image_data():
    im = (Image.open('maze.png').convert('L'))
    im = im.point(lambda x: 255 if x >150 else 0 )
    array = np.array(im)
    output_cols=[]

    w, h = im.size
    
    width = 45 
    
    w_gap = w//width
    h_gap = h//width
    
    for yindex, y in enumerate(array):
        for xindex, x in enumerate(y):
            if array[xindex][yindex] < 50:
                row = yindex // w_gap
                col = xindex // h_gap
                output_cols.append((row,col))
            


    return list(set(output_cols))

    

