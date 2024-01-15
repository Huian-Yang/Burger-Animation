from tkinter import *
import time

WIDTH = 500  #constant (not gonna change)
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()
window.title("Burger Animation")

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file='C:\\Users\\Huian\\OneDrive\\Desktop\\Python\\GUI Window\\mcdonalds500.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW) #put the image on the canvas


photo_image = PhotoImage(file='C:\\Users\\Huian\\OneDrive\\Desktop\\Python\\GUI Window\\trueburger.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW) #put the image on the canvas

image_width = photo_image.width()  #turns the image's width and hegiht into variables
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image) #get the coordnites of my_image
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0): #if coordnites is bigger than width or less than 0 
        xVelocity = -xVelocity #turns it to negative to positive infinitely as the loop plays (allows direaction change)
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0): 
        yVelocity = -yVelocity
    
    canvas.move(my_image,xVelocity,yVelocity)  #chnages the image location dynamically (in the direaction of those 2 varibales)
    window.update() #update window after each cycle
    time.sleep(0.01) #delays for 0.01 seconds


window.mainloop()










