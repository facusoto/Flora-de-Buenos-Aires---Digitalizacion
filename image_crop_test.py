# Importing Image class from PIL module
from PIL import Image
import csv

for image in images:
    path = f"C:\Program Files\Tesseract-OCR\tessert\imagenes\{image}"
    im, im2 = Image.open(path)

    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size

    # Setting the points for cropped image
    # IM1 (Left)
    left = 0
    top = 0
    right = width /2
    bottom = height

    # IM2 (Right)
    im2_left = width / 2
    im2_top = 0
    im2_right = width
    im2_bottom = height

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im2 = im.crop((im2_left, im2_top, im2_right, im2_bottom))

    # Shows the image in image viewer
    im1.show()


