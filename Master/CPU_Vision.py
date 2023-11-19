# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 02:44:28 2023

@author: Aaron
"""

from PIL import Image
import numpy as np


def get_image_data(image):
    im = (Image.open(image).convert('L'))
    im = im.point(lambda x: 255 if x >150 else 0 )

    output_cols=[]
    # Get image width and height
    w,h = im.size

    # Create array from image data and get dimensions
    array = np.array(im)
    array_x, array_y = array.shape

    # Must match width on astar.py as well 
    width = 45 

    w_gap = w//width
    h_gap = h//width


    # Check through array for any color and set 
    for yindex in range(array_y):
        for xindex in range (array_x):
            if array[xindex][yindex] < 50:
                row = yindex // w_gap
                col = xindex // h_gap
                output_cols.append((row,col))
            #print(xindex))


    return list(set(output_cols))


def get_tile_centerpoint(image,tiles):
    
    points =[]
    offset_x= 20
    offset_y = 40
    
    # Load in image and get size
    im = (Image.open(image).convert('L'))
    w,h = im.size
    
    width = 42
    
    # Get tile definitions
    w_gap = w//width
    h_gap = h//width
    
    # Revert tiles to centerpoint
    for index, tile in enumerate(tiles):
        # Change offset as maze solver goes on (this will need to be tuned)
        if index/ len(tiles) >= 0.25:
            offset_y = 10
            offset_x = 30
        if index/ len(tiles) >= 0.25:
            offset_x = 20
        
        row_val = tile[0]*w_gap + offset_x
        col_val = tile[1]*h_gap + offset_y
        points.append((row_val,col_val))
    
    
    return points
    