import cv2 as cv
import numpy as np
import os

path = 'Header'
for image in os.listdir(path):
    image_path = os.path.join(path, image)
    image1 = cv.imread(image_path)
    image2 = cv.resize(image1, (1280, 125))
    cv.imwrite(image_path, image2)

print("Done with the image resizing pleas eokay")