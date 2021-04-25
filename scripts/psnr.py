# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:57:50 2021

@author: Ashok
"""

from math import log10, sqrt
import cv2
import os
import numpy as np
  
original = r'C:\Users\Ashok\Desktop\ENGI_981_A\Code\real_test_input'
compressed = r'C:\Users\Ashok\Desktop\ENGI_981_A\Code\real_test_output'

for originalPath in os.listdir(original):
    for compressedPath in os.listdir(compressed):
        original = cv2.imread(original)
        compressed = cv2.imread(compressed)
        mse = np.mean((original - compressed) ** 2)

        max_pixel = 255.0
        psnr = 20 * log10(max_pixel / sqrt(mse))
  
        
        print(originalPath , "\t" , str(psnr))
       
