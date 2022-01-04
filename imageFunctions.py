
from math import pi
from math import sqrt
from math import cos
from math import sin
from tkinter import PhotoImage

#takes a photoimage as input, returns photoimage with transparency
def makeTransparent(img, colorToMakeTransparentInHexFormat):
    newPhotoImage = PhotoImage(width=img.width(), height=img.height())
    for x in range(img.width()):
        for y in range(img.height()):
            rgb = '#%02x%02x%02x' % img.get(x, y)
            if rgb != colorToMakeTransparentInHexFormat:
                newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

#takes a photoimage as input and current color, returns image with altered color
def switchColors(img, currentColor, futureColor):
    newPhotoImage = PhotoImage(width=img.width(), height=img.height())
    for x in range(img.width()):
        for y in range(img.height()):
            rgb = '#%02x%02x%02x' % img.get(x, y)
            if rgb == currentColor:
                newPhotoImage.put(futureColor, (x, y))
            else:
                newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

#takes a photoimage as input, desired width and height and returns photo image with
# desired width and height
def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

#returns a rotated PhotoImage
def rotatedPhotoImage(img, angle):
    angleInRads = angle * pi / 180
    diagonal = sqrt(img.width()**2 + img.height()**2)
    xmidpoint = img.width()/2
    ymidpoint = img.height()/2
    newPhotoImage = PhotoImage(width=int(diagonal), height=int(diagonal))
    for x in range(img.width()):
        for y in range(img.height()):

            # convert to ordinary mathematical coordinates
            xnew = float(x)
            ynew = float(-y)

            # shift to origin
            xnew = xnew - xmidpoint
            ynew = ynew + ymidpoint

            # new rotated variables, rotated around origin (0,0) using simoultaneous assigment
            xnew, ynew = xnew*cos(angleInRads) - ynew*sin(angleInRads), xnew * sin(angleInRads) + ynew*cos(angleInRads)

            # shift back to quadrant iv (x,-y), but centered in bigger box
            xnew = xnew + diagonal/2
            ynew = ynew - diagonal/2

            # convert to -y coordinates
            xnew = xnew
            ynew = -ynew

            # get pixel data from the pixel being rotated in hex format
            rgb = '#%02x%02x%02x' % img.get(x, y)

            # put that pixel data into the new image
            newPhotoImage.put(rgb, (int(xnew), int(ynew)))

            # this helps fill in empty pixels due to rounding issues
            newPhotoImage.put(rgb, (int(xnew+1), int(ynew)))

    return newPhotoImage

############## Used in conjuction together #########################
#takes a png file as input, returns array of rotated photoimages
def rotatedImagesArray(filename="myphoto.png"):
    originalImage = PhotoImage(file=filename)
    rotatedImages = []
    for i in range(16):  # using 16 images
        angle = i*22.5  # 360degrees/16 images = 22.5 degrees
        rotatedImages.append(rotatedPhotoImage(originalImage, angle))
    return rotatedImages

#takes a photoimage as input, returns array of rotated photoimages
def rotatedImagesArray16(originalImage):
    rotatedImages = []
    for i in range(16):  # using 16 images
        angle = i*22.5  # 360degrees/16 images = 22.5 degrees
        rotatedImages.append(rotatedPhotoImage(originalImage, angle))
    return rotatedImages

#returns index of array for closest image to a given angle for array of 
#16 images
def getImageIndex16(angle):
    # resets 360 to 0
    angle = angle % 360
    # using 16 images: 360/16 is 22.5 degrees, 11.25 is 1/2 of 22.5
    index = (angle-11.25)/22.5 + 1
    index = int(index)
    index = index % 16
    return index

#returns an array of images
def rotatedImagesArray(originalImage, numberOfImages):
    rotatedImages = []
    for i in range(numberOfImages):
        angle = i*(360/numberOfImages)
        print("making rotated image at "+ str(angle) + " degrees.")
        rotatedImages.append(rotatedPhotoImage(originalImage, angle))
    return rotatedImages

#returns index for closest image given a number of images
def getImageIndex(angle, numberOfImages):
    angle = angle % 360
    angleSlice=360/numberOfImages
    halfAngleSlice= angleSlice/2
    index = (angle-halfAngleSlice)/angleSlice + 1
    index = int(index)
    index = index % numberOfImages
    return index

#returns best image from array for a given angle
def getImage(angle, rotatedImageArray):
    numberOfImages=len(rotatedImageArray)
    index=getImageIndex(angle, numberOfImages)
    return(rotatedImageArray[index])

#####################################################################

