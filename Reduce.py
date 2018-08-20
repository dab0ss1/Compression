# dependencies
import os
import numpy as np
import scipy.misc
import cv2

'''
Reduced the file size and quality of the pictures by running the JPEG compression
algorithm on the picture.
'''

# global variables
IMAGE_PATH = "./rose.jpg"
EXPORT_PATH = "./Reduced Pictures/"

# main
def main():
    checkPathsExist()
    arrColors = importPicture()
    exportPicture(arrColors)
# end main

# Check if the paths exist
def checkPathsExist():
    global IMAGE_PATH
    global EXPORT_PATH
    if not os.path.exists(IMAGE_PATH):
        print("The image path does not exist")
        exit()
    if not os.path.exists(EXPORT_PATH):
        print("The export path does not exist")
        exit()

# Imports the pixels from the picture
def importPicture():
    global IMAGE_PATH
    image = cv2.imread(IMAGE_PATH)

    if image is None:
        print("Make sure the image path points to an image file")
        exit()

    for y in range(len(image)):
        for x in range(len(image[y])):
            hold0 = image[y][x][0]
            image[y][x][0] = image[y][x][2]
            image[y][x][2] = hold0
    return image

# Exports the array of pixels into a picture
def exportPicture(arrColors):
    global IMAGE_PATH
    global EXPORT_PATH
    scipy.misc.imsave(EXPORT_PATH + IMAGE_PATH.split('/')[-1].split('.')[0] + "_r.jpg", np.array(arrColors))


if __name__ == '__main__':
    main()