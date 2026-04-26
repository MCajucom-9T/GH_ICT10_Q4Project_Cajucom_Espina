#Displaying images in Gallery
from pyscript import display, document


def disp_images(e): #def to display image
    img = document.getElementById("gallery")

    if img.style.display == "none": 
        img.style.display = "flex"
