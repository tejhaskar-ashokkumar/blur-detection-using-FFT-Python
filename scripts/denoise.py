# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:52:06 2020

@author: Ashok
"""

import numpy as np
import cv2
import os

inputFolder = "C:\\Users\Ashok\Desktop\ENGI_981_A\Code\Resized\Resized_Color"
outputFolder = "C:\\Users\Ashok\Desktop\ENGI_981_A\Code\Denoised"

def denoise():
    count = 1
    for imagePath in os.listdir(inputFolder):
        inputPath = os.path.join(inputFolder, imagePath)
        image = cv2.imread(inputPath)
        dst = cv2.fastNlMeansDenoisingColored(image)
        outputPath = os.path.join(outputFolder, 'denoise_')
        cv2.imwrite(outputPath + str(count) + ".png", image)
        count+=1



