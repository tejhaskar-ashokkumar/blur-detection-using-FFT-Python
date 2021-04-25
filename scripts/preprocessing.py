# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:09:42 2020

@author: Ashok
"""
from PIL import Image
import cv2
import glob as gl
import numpy as np
import os


inputFolder = "C:\\Users\Ashok\Desktop\ENGI_981_A\Code\Dataset_PNG"
outputgrayFolder = "C:\\Users\Ashok\Desktop\ENGI_981_A\Code\Resized\Resized_Gray"
outputcolorFolder = "C:\\Users\Ashok\Desktop\ENGI_981_A\Code\Resized\Resized_Color"


def PreprocessImg():
    count = 1

    for imagePath in os.listdir(inputFolder):
        inputPath = os.path.join(inputFolder, imagePath)
        image = cv2.imread(inputPath)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (256, 256))
        gray_img = cv2.resize(gray_img, (256, 256))
        grayPath = os.path.join(outputgrayFolder, 'resize_')
        colorPath = os.path.join(outputcolorFolder, 'resize_')
        cv2.imwrite(grayPath +str(count) +".png", gray_img)
        cv2.imwrite(colorPath +str(count) +".png", image)
        count += 1
        
        
        