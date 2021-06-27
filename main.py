# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 12:44:37 2021

@author: TASMIM
"""

import cv2
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract

Data_dir = 'Data/'

image_name = input("Enter image file name with extension: ")

image_file = Data_dir + image_name

print(image_file)
image = Image.open(image_file)
#image = cv2.imread(image_file)
plt.imshow(image)

out_text =pytesseract.image_to_string(image, lang = 'ben+eng')
print(out_text)