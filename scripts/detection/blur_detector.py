# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:16:54 2020

@author: Ashok
"""

import numpy as np


def detect_blur_fft(image,size):
    (h, w) = (256, 256)
    #center(x,y) of an image
    (cX,cY) = (int(w/2.0), int(h/2.0))
    #compute DFT of an image
    fft = np.fft.fft2(image)
    #shifting F(0,0) to the center
    fftshift = np.fft.fftshift(fft)
    #compute the magnitude 
    '''magnitude = 20*np.log(np.abs(fftshift))'''
    
        
    fftshift[cY - size:cY + size, cX - size:cX + size] = 0
    fftshift = np.fft.ifftshift(fftshift)
    recon = np.fft.ifft2(fftshift)
    magnitude = 20*np.log(np.abs(recon))
    mean = np.mean(magnitude)
    
    
    return mean




    
        
    