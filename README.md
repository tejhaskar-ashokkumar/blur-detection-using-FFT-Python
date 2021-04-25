# blur-detection-using-FFT-Python

Run main.py to detect the image is blur or not. 

preprocessing.py - Changes the dimensions of multiple images into a unique dimensions for ease of system implementation

type_conversion.py - Converts the image of .jpg, .bmp, .png, .tiff to .png

denoise.py - Removes the noise and smoothen the image for better analysis

psnr.py - Calculates the Peak Signal Noise Ratio for input images. This score is used to evaluate the image has noise, less noise or no noise. 

blur_detetor.py - Python implementation of Python.

detect_blur_img.py - Detects the image is blurry or not using the average pixel intensity value. The average pixel intensity
values are chosen after several trial and error and this value works fine with Kaggle Blur Dataset.

brisque.py - Used to evaluate the image quality score.
