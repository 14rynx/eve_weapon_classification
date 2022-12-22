# Importing Image class from PIL module
from functools import reduce
from PIL import Image
import os
import operator


def equalize(im):
    h = im.convert("L").histogram()
    lut = []
    for b in range(0, len(h), 256):
        # step size
        step = reduce(operator.add, h[b:b+256]) / 255
        # create equalization lookup table
        n = 0
        for i in range(256):
            lut.append(n / step)
            n = n + h[i+b]
    # map image through lookup table
    return im.point(lut*4)

    # Shows the image in image viewer


for root, _, files in os.walk("shiptype_classification", topdown=False):

    for file in files:
        print(os.path.join(root, file))

        with Image.open(os.path.join(root, file)) as img:

            img = equalize(img)

            # Shows the image in image viewer
            os.makedirs(root.replace("shiptype_classification", "shiptype_classification_normalized"), exist_ok=True)
            img.save(os.path.join(root, file).replace("shiptype_classification", "shiptype_classification_normalized"))
