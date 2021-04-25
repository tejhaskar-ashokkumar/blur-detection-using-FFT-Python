# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:21:04 2020

@author: Ashok
"""

from preprocessing import PreprocessImg
from type_conversion import imgTypeConv
from brisque import brisqueCalc
from denoise import denoise
from detect_blur_img import blurDetector



def main():
    print("Automatic Image Blur Detection/Removal and Improving Image Resolution")
    print("\n Converting to .png . . . .")
    imgTypeConv()
    print("\n Preprocessing in progres. <Converting Image to grayscale of size 256 x 256>")
    PreprocessImg()
    print("\n Check the destination folder for Resized Images")
    print("\n Calculating and  Printing Brisque Score . . . .")
    brisqueCalc()
    print("\n Performing Denoising. . . . ")
    denoise()
    print("\n Detecting whether Image is Blurry or Not . . . .")
    blurDetector()
    print("\n Check the destination folder for Blur or Not . . . .")

if __name__ == '__main__':
    main()


