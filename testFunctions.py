from tkinter import *
from time import sleep
from imageFunctions import *

root=Tk()

myCanvas=Canvas(root,width=600,height=600)
myPhoto=PhotoImage(file='greenpig.png')
myCanvas.pack()
myCanvas.create_image(0, 0, anchor=NW, image=myPhoto)

myNewPhoto=resizeImage(myPhoto,128,128)

myNewPhoto=switchColors(myNewPhoto,'#99e76b','#ffaaff')
myNewPhoto=makeTransparent(myNewPhoto,'#000000')

myNewPhotoArray=rotatedImagesArray(myNewPhoto,12)

for i in range(len(myNewPhotoArray)):
    print("making image "+str(i)+" transparent.")
    myNewPhotoArray[i]=makeTransparent(myNewPhotoArray[i],'#000000')

canvasImage=myCanvas.create_image(300,300,anchor=CENTER, image=myNewPhoto)

for i in range(1000): #some arbitrary number of degrees
    myCanvas.delete(canvasImage)
    canvasImage = myCanvas.create_image(300, 300, image=myNewPhotoArray[getImageIndex(i,12)], anchor=CENTER)
    root.update()
    sleep(.005)

root.mainloop()