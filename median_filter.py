# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 23:17:41 2023

@author: abraham martinez
"""

# Median Filter
  

import cv2
import numpy as np
from PIL import Image

def median_filter(input_img):
    
    image_noisy = cv2.imread(input_img, 0)

    #Rows and columns of the image
    m, n = image_noisy.shape

    #Initializing array 
    new_image = np.zeros([m, n])

    #Traverse the image. For every 3X3 area
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp = [image_noisy[i-1, j-1],
                    image_noisy[i-1, j],
                    image_noisy[i-1, j + 1],
                    image_noisy[i, j-1],
                    image_noisy[i, j],
                    image_noisy[i, j + 1],
                    image_noisy[i + 1, j-1],
                    image_noisy[i + 1, j],
                    image_noisy[i + 1, j + 1]]

            temp = sorted(temp)
            new_image[i, j] = temp[4]

    # Unsigned 8-bit integer conversion for OpenCV to read
    new_image = new_image.astype(np.uint8)

    #Save the output image
    output_img = "output_median_filtered1.png"
    cv2.imwrite(output_img, new_image)

    #Display the output image using PIL for better visualization
    output_pil = Image.fromarray(new_image)
    output_pil.show()


median_filter("sample1.png")
