from loading import *
import numpy as np
import cv2




def resize_image(image, dims):
    image_resized = cv2.resize(image, dims)
    return image_resized




def rotate_image(image,degree):
    (h, w, d) = image.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, degree, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image


def draw_rectangle(image, tlcorner, brcorner,color, line_thickness):
    output = image.copy()
    cv2.rectangle(output, tlcorner, brcorner, color, line_thickness)
    return output


def princ():
    image = load("../Data/tetris_blocks.png")
    rotated = draw_rectangle(image, (320, 60), (420, 160), (0, 0, 255), 2)
    cv2.imshow("OpenCV Rotation", rotated)
    cv2.waitKey(0)


