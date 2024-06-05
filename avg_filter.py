# -*- coding: utf-8 -*-

import PIL
from PIL import Image

def avg_filter(input_img):
    
    # Open the image
    img = Image.open(input_img)
    
    # Get the image size
    width, height = img.size
    
    # Set the filter size
    filter_size = 3
    filter_sum = 9    
    
    # RGB Color mode
    if img.mode == "RGB":
        
        output = Image.new("RGB", (width, height))
                
        # Handle non-edge pixels
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                r, g, b = 0, 0, 0
                
                # Add all values in the 3x3 filter
                for i in range(filter_size):
                    for j in range(filter_size):
                        pixel_value = img.getpixel((x-1+i, y-1+j))
                        r += pixel_value[0]
                        g += pixel_value[1]
                        b += pixel_value[2]
                        
                # Calculate average value        
                r_avg = r // filter_sum
                g_avg = g // filter_sum
                b_avg = b // filter_sum
                
                # Difference between neighbors
                r_least, g_least, b_least = r_avg - 25, g_avg - 25, b_avg - 25
                r_most, g_most, b_most = r_avg + 25, g_avg + 25, b_avg + 25
                
                # Replace if the difference is huge
                target_value = img.getpixel((x,y))
                
                if (target_value[0] < r_least or target_value[0] > r_most 
                or target_value[1] < g_least or target_value[1] > g_most 
                or target_value[2] < b_least or target_value[2] > b_most):
                    output.putpixel((x, y), (r_avg, g_avg, b_avg))
                
                else:
                    output.putpixel((x,y), target_value)
                
        
        # Save the output image 
        output_img = "output_image.jpg"
        output.save(output_img)
        
    
    else:
        output = Image.new("L", (width, height))
        
        # Handle non-edge pixels
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                pixel_value = 0
                
                # Add all values in the 3x3 filter
                for i in range(filter_size):
                    for j in range(filter_size):
                        pixel_value += img.getpixel((x-1+i, y-1+j))
                 
                # Calculate average value        
                avg_value = pixel_value // filter_sum
                
                # Difference between neighbors
                least = avg_value - 25
                most = avg_value + 25
                
                # Replace if the difference is huge
                target_value = img.getpixel((x,y))

                if target_value < least or target_value > most:
                    output.putpixel((x,y), avg_value)
                    
                else:
                    output.putpixel((x,y), target_value)
        
        # Save the output image        
        output_img = "output_image.jpg"
        output.save(output_img)


# Call the function
avg_filter("Lena_noise.jpg")







