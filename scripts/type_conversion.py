# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:12:09 2020

@author: Ashok
"""

from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os

inputFolder = "C:\\Users\Ashok\Desktop\ENGI_981_A\Code\Dataset"
outputFolder = "C:\\Users\Ashok\Desktop\ENGI_981_A\Code\Dataset_PNG"

def imgTypeConv():
    i = 1
    for imagePath in os.listdir(inputFolder):
        inputPath = os.path.join(inputFolder, imagePath)
        img = Image.open(inputPath)
        fullOutPath = os.path.join(outputFolder,'img_'+str(i)+'.png')
        i = i + 1
        img.save(fullOutPath)


