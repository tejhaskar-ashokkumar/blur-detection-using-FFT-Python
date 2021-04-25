# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:58:37 2020

@author: Ashok
"""

import imquality.brisque as brisque
import PIL.Image as Image
import os


path = r'C:\Users\Ashok\Desktop\ENGI_981_A\Code\real_test_input'


for imagePath in os.listdir(path):
    inputPath = os.path.join(path, imagePath)
    img = Image.open(inputPath)
    score = brisque.score(img)
    print(imagePath , "\t" , score)
    


    
        

            
        

        
    
        
        
        
        
        
        
        
    