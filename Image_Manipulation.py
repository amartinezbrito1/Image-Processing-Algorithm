# -*- coding: utf-8 -*-

import PIL
from PIL import Image



def checkForNoise(im):
    
    height = im.height
    length = im.width
    
    bottom = height - 1
    rightSide = length -1
    x = 0
    y = 0
    
    noise = []
    
    #RGB Color mode
    if im.mode == "RGB":
        
        #preforms an operation on every pixel in an image. 
        for x in range(length):
            
            for y in range(height):
                #Get RGB Values from a pixel
                
                total = 0
                tuple = []
                
                #Handle Top Left Corner
                if x == 0 and y == 0:
                    tuple.append( im.getpixel((x,y)))
                    r = tuple[0]
                    CenterValue = r[0]
                    
                    
                    tuple.append( im.getpixel((x+1,y)) )                
                    tuple.append( im.getpixel((x+1,y+1)) )
                    tuple.append( im.getpixel((x,y+1)) )
                    
                    #unpack tuple
                    temp = tuple[1]
                    one = temp[0]
                    temp = tuple[2]
                    two = temp[0]
                    temp = tuple[3]
                    three = temp[0]

                    #calculate average value of block of neighboring pixels.
                    total = CenterValue + one + two + three

                    Avg = (total / 4)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 27
                    ub = Avg + 27
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                        
                #Handle Bottom Left Corner
                elif x == 0 and y == bottom:
                    tuple.append( im.getpixel((x,y)))
                    r = tuple[0]
                    CenterValue = r[0]
                    
                    
                    tuple.append( im.getpixel((x+1,y)) )
                    tuple.append( im.getpixel((x+1,y-1)) )
                    tuple.append( im.getpixel((x,y-1)) )
                    
                    #unpack tuple
                    temp = tuple[1]
                    one = temp[0]
                    temp = tuple[2]
                    two = temp[0]
                    temp = tuple[3]
                    three = temp[0]

                    #calculate average value of block of neighboring pixels.
                    total = CenterValue + one + two + three

                    Avg = (total / 4)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 27
                    ub = Avg + 27
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                
                #Handle Top Right Corner
                elif x == rightSide and y == 0:
                    tuple.append( im.getpixel((x,y)))
                    r = tuple[0]
                    CenterValue = r[0]
                    
                    
                    #pixel to the left of pixel
                    tuple.append(im.getpixel((x-1,y)))
                    tuple.append(im.getpixel((x,y+1)))
                    tuple.append(im.getpixel((x-1,y+1)))
                    
                    #unpack tuple
                    temp = tuple[1]
                    one = temp[0]
                    temp = tuple[2]
                    two = temp[0]
                    temp = tuple[3]
                    three = temp[0]

                    #calculate average value of block of neighboring pixels.
                    total = CenterValue + one + two + three

                    Avg = (total / 4)
                    Avg = round(Avg)
                    
                    lb = Avg - 27
                    ub = Avg + 27
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                    
                #Handle Bottom Right Corner
                elif x == rightSide and y == bottom:
                    tuple.append( im.getpixel((x,y)))
                    r = tuple[0]
                    CenterValue = r[0]
                    
                    
                    #pixel to the left of pixel
                    tuple.append(im.getpixel((x-1,y)))
                    tuple.append(im.getpixel((x,y-1)))
                    tuple.append(im.getpixel((x-1,y-1)))
                    
                    #unpack tuple
                    temp = tuple[1]
                    one = temp[0]
                    temp = tuple[2]
                    two = temp[0]
                    temp = tuple[3]
                    three = temp[0]

                    #calculate average value of block of neighboring pixels.
                    total = CenterValue + one + two + three

                    Avg = (total / 4)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 25
                    ub = Avg + 25
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                        
                #Handle Left Side
                elif x == 0 and y != bottom:
                    tuple.append( im.getpixel((x,y)))
                    r = tuple[0]
                    CenterValue = r[0]
                    
                    
                    #pixel to the right of pixel
                    tuple.append(im.getpixel((x+1,y)))
                    tuple.append(im.getpixel((x+1,y+1)))
                    tuple.append(im.getpixel((x+1,y-1)))
                    tuple.append(im.getpixel((x,y+1)))
                    tuple.append(im.getpixel((x,y-1)))
                    
                    #unpack tuple
                    temp = tuple[1]
                    one = temp[0]
                    temp = tuple[2]
                    two = temp[0]
                    temp = tuple[3]
                    three = temp[0]
                    temp = tuple[4]
                    four = temp[0]
                    temp = tuple[5]
                    five = temp[0]
                    
                    #calculate average value of block of neighboring pixels.
                    total = CenterValue + one + two + three + four + five

                    Avg = (total / 6)
                    Avg = round(Avg)
                    
                    lb = Avg - 25
                    ub = Avg + 25
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                        
                #Handle Top Side
                elif x != rightSide and y == 0:
                    tuple.append( im.getpixel((x,y)))
                    r = tuple[0]
                    CenterValue = r[0]
                    
                    
                    #pixel to the right of pixel
                    tuple.append(im.getpixel((x+1,y)))
                    tuple.append(im.getpixel((x-1,y)))
                    tuple.append(im.getpixel((x+1,y-1)))
                    tuple.append(im.getpixel((x-1,y-1)))
                    tuple.append(im.getpixel((x,y-1)))
                    
                    #unpack tuple
                    temp = tuple[1]
                    one = temp[0]
                    temp = tuple[2]
                    two = temp[0]
                    temp = tuple[3]
                    three = temp[0]
                    temp = tuple[4]
                    four = temp[0]
                    temp = tuple[5]
                    five = temp[0]
            
                    
                    #calculate average value of block of neighboring pixels.
                    total = CenterValue + one + two + three + four + five

                    Avg = (total / 6)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 27
                    ub = Avg + 27
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                
                #Handle Right Side
                elif x == rightSide and y != bottom:
                    tuple.append( im.getpixel((x,y)))
                    r = tuple[0]
                    CenterValue = r[0]
                    
                    
                    #pixel to the right of pixel
                    tuple.append(im.getpixel((x-1,y)))
                    tuple.append(im.getpixel((x-1,y+1)))
                    tuple.append(im.getpixel((x-1,y-1)))
                    tuple.append(im.getpixel((x,y+1)))
                    tuple.append(im.getpixel((x,y-1)))
                    
                    #unpack tuple
                    temp = tuple[1]
                    one = temp[0]
                    temp = tuple[2]
                    two = temp[0]
                    temp = tuple[3]
                    three = temp[0]
                    temp = tuple[4]
                    four = temp[0]
                    temp = tuple[5]
                    five = temp[0]
            
                    
                    #calculate average value of block of neighboring pixels.
                    total = CenterValue + one + two + three + four + five

                    Avg = (total / 6)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 27
                    ub = Avg + 27
                    
                    if CenterValue < lb  or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                        
                #Handle Bottom Edge
                elif x != rightSide and y == bottom:
                    tuple.append( im.getpixel((x,y)))
                    r = tuple[0]
                    CenterValue = r[0]
                    
                    
                    #pixel to the right of pixel
                    tuple.append(im.getpixel((x+1,y)))
                    tuple.append(im.getpixel((x-1,y)))
                    tuple.append(im.getpixel((x+1,y-1)))
                    tuple.append(im.getpixel((x-1,y-1)))
                    tuple.append(im.getpixel((x,y-1)))
                    
                    #unpack tuple
                    temp = tuple[1]
                    one = temp[0]
                    temp = tuple[2]
                    two = temp[0]
                    temp = tuple[3]
                    three = temp[0]
                    temp = tuple[4]
                    four = temp[0]
                    temp = tuple[5]
                    five = temp[0]
            
                    
                    #calculate average value of block of neighboring pixels.
                    total = CenterValue + one + two + three + four + five

                    Avg = (total / 6)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 27
                    ub = Avg + 27
                   
                    if CenterValue < lb  or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                        
                #All non edge values.
                else:
                    
                    tuple.append( im.getpixel((x,y)))
                    r = tuple[0]
                    CenterValue = r[0]
                    
                    
                    tuple.append(im.getpixel((x+1,y)))
                    tuple.append(im.getpixel((x-1,y)))
                    tuple.append(im.getpixel((x+1,y+1)))
                    tuple.append(im.getpixel((x-1,y-1)))
                    tuple.append(im.getpixel((x+1,y-1)))
                    tuple.append(im.getpixel((x-1,y+1)))
                    tuple.append(im.getpixel((x,y+1)))
                    tuple.append(im.getpixel((x,y-1)))
                    
                    #unpack tuple
                    temp = tuple[1]
                    one = temp[0]
                    temp = tuple[2]
                    two = temp[0]
                    temp = tuple[3]
                    three = temp[0]
                    temp = tuple[4]
                    four = temp[0]
                    temp = tuple[5]
                    five = temp[0]
                    temp = tuple[6]
                    six = temp[0]
                    temp = tuple[7]
                    seven = temp[0]
                    temp = tuple[8]
                    eight = temp[0]
            
                    
                    #calculate average value of block of neighboring pixels.
                    total = CenterValue + one + two + three + four + five + six + seven + eight

                    Avg = (total / 9)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 27
                    ub = Avg + 27
                    
                    if CenterValue < lb  or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
    #Single Channel color mode
    elif im.mode == "L":
        
        #preforms an operation on every pixel in an image. 
        for x in range(length):
            
            for y in range(height):
                #Get RGB Values from a pixel
                
                total = 0
                list = []
                
                #Handle Top Left Corner
                if x == 0 and y == 0:
                    list.append( im.getpixel((x,y)))
                    CenterValue = list[0]
                    
                    
                    list.append( im.getpixel((x+1,y)) )                
                    list.append( im.getpixel((x+1,y+1)) )
                    list.append( im.getpixel((x,y+1)) )
                    
                    #Sum and Average neighboring pixels matrix List
                    total = sum(list)

                    Avg = (total / 4)
                    Avg = round(Avg)

                    
                    lb = Avg - 27
                    ub = Avg + 27
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                        
                #Handle Bottom Left Corner
                elif x == 0 and y == bottom:
                    list.append( im.getpixel((x,y)))
                    CenterValue = list[0]
                    
                    
                    list.append( im.getpixel((x+1,y)) )
                    list.append( im.getpixel((x+1,y-1)) )
                    list.append( im.getpixel((x,y-1)) )
                    
                    #Sum and Average neighboring pixels matrix List
                    total = sum(list)


                    Avg = (total / 4)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 27
                    ub = Avg + 27
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                
                #Handle Top Right Corner
                elif x == rightSide and y == 0:
                    list.append( im.getpixel((x,y)))
                    CenterValue = list[0]
                    
                    
                    #pixel to the left of pixel
                    list.append(im.getpixel((x-1,y)))
                    list.append(im.getpixel((x,y+1)))
                    list.append(im.getpixel((x-1,y+1)))
                    
                    #Sum and Average neighboring pixels matrix List
                    total = sum(list)

                    Avg = (total / 4)
                    Avg = round(Avg)
                    
                    lb = Avg - 27
                    ub = Avg + 27
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                    
                #Handle Bottom Right Corner
                elif x == rightSide and y == bottom:
                    list.append( im.getpixel((x,y)))
                  
                    CenterValue = list[0]
                    
                    
                    #pixel to the left of pixel
                    list.append(im.getpixel((x-1,y)))
                    list.append(im.getpixel((x,y-1)))
                    list.append(im.getpixel((x-1,y-1)))
                    
                    #Sum and Average neighboring pixels matrix List
                    total = sum(list)

                    Avg = (total / 4)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 25
                    ub = Avg + 25
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                        
                #Handle Left Side
                elif x == 0 and y != bottom:
                    list.append( im.getpixel((x,y)))
                    CenterValue = list[0]
                
                    
                    #pixel to the right of pixel
                    list.append(im.getpixel((x+1,y)))
                    list.append(im.getpixel((x+1,y+1)))
                    list.append(im.getpixel((x+1,y-1)))
                    list.append(im.getpixel((x,y+1)))
                    list.append(im.getpixel((x,y-1)))
                    
                    #Sum and Average neighboring pixels matrix List
                    total = sum(list)

                    Avg = (total / 6)
                    Avg = round(Avg)
                    
                    lb = Avg - 25
                    ub = Avg + 25
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                        
                #Handle Top Side
                elif x != rightSide and y == 0:
                    list.append( im.getpixel((x,y)))
                    
                    CenterValue = list[0]
                    
                    
                    #pixel to the right of pixel
                    list.append(im.getpixel((x+1,y)))
                    list.append(im.getpixel((x-1,y)))
                    list.append(im.getpixel((x+1,y-1)))
                    list.append(im.getpixel((x-1,y-1)))
                    list.append(im.getpixel((x,y-1)))
                    
                    #Sum and Average neighboring pixels matrix List
                    total = sum(list)

                    Avg = (total / 6)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 27
                    ub = Avg + 27
                    
                    if CenterValue < lb or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                
                #Handle Right Side
                elif x == rightSide and y != bottom:
                    list.append( im.getpixel((x,y)))

                    CenterValue = list[0]
                    
                    
                    #pixel to the right of pixel
                    list.append(im.getpixel((x-1,y)))
                    list.append(im.getpixel((x-1,y+1)))
                    list.append(im.getpixel((x-1,y-1)))
                    list.append(im.getpixel((x,y+1)))
                    list.append(im.getpixel((x,y-1)))
                    
                    #Sum and Average neighboring pixels matrix List
                    total = sum(list)

                    Avg = (total / 6)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 27
                    ub = Avg + 27
                    
                    if CenterValue < lb  or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                        
                #Handle Bottom Edge
                elif x != rightSide and y == bottom:
                    list.append( im.getpixel((x,y)))

                    CenterValue = list[0]
                    
                    
                    #pixel to the right of pixel
                    list.append(im.getpixel((x+1,y)))
                    list.append(im.getpixel((x-1,y)))
                    list.append(im.getpixel((x+1,y-1)))
                    list.append(im.getpixel((x-1,y-1)))
                    list.append(im.getpixel((x,y-1)))
                    
                    #Sum and Average neighboring pixels matrix List
                    total = sum(list)

                    Avg = (total / 6)
                    Avg = round(Avg)
                    
                    
                    lb = Avg - 27
                    ub = Avg + 27
                   
                    if CenterValue < lb  or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
                        
                #All non edge values.
                else:
                    
                    list.append( im.getpixel((x,y)))
                    
                    CenterValue = list[0]
                    
                    
                    list.append(im.getpixel((x+1,y)))
                    list.append(im.getpixel((x-1,y)))
                    list.append(im.getpixel((x+1,y+1)))
                    list.append(im.getpixel((x-1,y-1)))
                    list.append(im.getpixel((x+1,y-1)))
                    list.append(im.getpixel((x-1,y+1)))
                    list.append(im.getpixel((x,y+1)))
                    list.append(im.getpixel((x,y-1)))
                    
                    #Sum and Average neighboring pixels matrix List
                    total = sum(list)

                    Avg = (total / 9)
                    Avg = round(Avg)
                    
                    lb = Avg - 25
                    ub = Avg + 25
                    
                    if CenterValue < lb  or CenterValue > ub:
                        noise.append(x)
                        noise.append(y)
   
                
    return noise


def markNoise(pixels, im):
    
    if im.mode == "L":
        im = im.convert("RGB")
        
    
    
    for i in range(len(pixels)):
        if (i % 2) == 0:
            x = pixels[i]
            y = pixels[i+1]
        
            im.putpixel((x,y),(255,0,0))
            
            
    
    
        
#program down here

file_name = input("Please enter image file name with extension: ")
im = Image.open(file_name)



noise = checkForNoise(im)
#print(len(noise))

#only works when image is previously converted to RGB as it marks noise Red.
#im = im.convert("RGB")
#markNoise(noise,im)



    
im.show()


