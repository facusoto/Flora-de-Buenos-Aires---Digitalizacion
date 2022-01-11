# Importing Image class from PIL module
from PIL import Image
import os
import os.path

# Elementos útiles
images = r"C://Users/Facu/Desktop/Code/Flora-de-Buenos-Aires---Digitalizacion/imagenes"

counter = 0
for file in os.listdir(images):
    img_file = images+"/"+file

    im = Image.open(img_file)
    im2 = im

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
    im2 = im2.crop((im2_left, im2_top, im2_right, im2_bottom))

    def save_image():
        # Saves the image in directory
        image_path = r"C:\Users\Facu\Desktop\Code\Flora-de-Buenos-Aires---Digitalizacion\imagenes_cortadas"
        name1 = f"{file}"
        name2 = f"side-{file}"

        im1.save(f"{image_path}\{name1}")
        im2.save(f"{image_path}\{name2}")
        
        print(f'Imagenes {name1} y {name2} guardadas')
    
    save_image()

    im.close()
    im2.close()