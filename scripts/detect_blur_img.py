# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:13:54 2020

@author: Ashok
"""

from detection.blur_detector import detect_blur_fft
import numpy as np
import imutils
import cv2
import os

inputFolder = r'C:\Users\Ashok\Desktop\ENGI_981_A\Code\Denoised'
Category1 = r'C:\Users\Ashok\Desktop\ENGI_981_A\Code\Output\Category1'
Category2 = r'C:\Users\Ashok\Desktop\ENGI_981_A\Code\Output\Category2'
Category3 = r'C:\Users\Ashok\Desktop\ENGI_981_A\Code\Output\Category3'
Category4 = r'C:\Users\Ashok\Desktop\ENGI_981_A\Code\Output\Category4'

def blurDetector():
    count = 1
    for imagePath in os.listdir(inputFolder):
        inputPath = os.path.join(inputFolder, imagePath)
        img = cv2.imread(inputPath)
        outputPath1 = os.path.join(Category1, 'output_')
        outputPath2 = os.path.join(Category2, 'output_')
        outputPath3 = os.path.join(Category3, 'output_')
        outputPath4 = os.path.join(Category4, 'output_')
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        
        mean = detect_blur_fft(gray, size = 60)
        average_intensity = np.mean(mean)
        

        if average_intensity <= 10.99:
            color = (0, 0, 255)
            text = "Too Blur ({:.4f})"
            text = text.format(mean)
            cv2.putText(img, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            out = "output_" + "00000" + str(count)
            print(out ,"\t", mean)
            cv2.imwrite(outputPath1 + "00000" + str(count) + ".png", img)
        
        elif 11.0 <= average_intensity <= 15.99:
            color = (0, 0, 255)
            text = "Blur ({:.4f})"
            text = text.format(mean)
            cv2.putText(img, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            out = "output_" + "00000" + str(count)
            print(out ,"\t", mean)
            cv2.imwrite(outputPath2 + "00000" + str(count) + ".png", img)
        
        elif 16.00 <= average_intensity <= 20:
            color = (0, 0, 255)
            text = "Light Blur ({:.4f})"
            text = text.format(mean)
            cv2.putText(img, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            out = "output_" + "00000" + str(count)
            print(out ,"\t", mean)
            cv2.imwrite(outputPath3 + "00000" + str(count) + ".png", img)
            
        else:
            color = (255, 0, 0)
            text = "Not Blur ({:.4f})"
            text = text.format(mean)
            cv2.putText(img, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            out = "output_" + "00000" + str(count)
            print(out ,"\t", mean)
            cv2.imwrite(outputPath4 + "00000" + str(count) + ".png", img)
        count+= 1
            
        