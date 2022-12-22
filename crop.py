# Importing Image class from PIL module
from PIL import Image
import os

# Opens a image in RGB mode

for root, _, files in os.walk("raw", topdown=False):
    for file in files:
        print(os.path.join(root, file))

        with Image.open(os.path.join(root, file)) as img:

            width, height = img.size

            left = width * 0.25
            top = height * 0.25
            right = width * 0.75
            bottom = height * 0.75

            # Cropped image of above dimension
            # (It will not change original image)
            img = img.crop((left, top, right, bottom))

            # Shows the image in image viewer
            os.makedirs(root.replace("raw", "weapon_classification"), exist_ok=True)
            img.save(os.path.join(root, file).replace("raw", "weapon_classification").replace("jpg", "png"))
