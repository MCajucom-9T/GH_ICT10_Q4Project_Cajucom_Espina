
from pyscript import display, document


def disp_images(e):
    img = document.getElementById("gallery")

    if img.style.display == "none":
        img.style.display = "flex"
