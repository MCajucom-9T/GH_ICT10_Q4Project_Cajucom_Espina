#Displaying images in Gallery
from pyscript import display, document


def disp_images(e): #def to display image
    img = document.getElementById("gallery") #Gets the element with ID of Gallery

    if img.style.display == "none": #Checks if gallery is hidden. If it is hidden, it will change the display to flex.
        img.style.display = "flex"
