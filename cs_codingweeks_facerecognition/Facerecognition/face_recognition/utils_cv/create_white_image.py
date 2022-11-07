import numpy as np
import cv2


def create_white_image():
    a = 255*np.ones(shape=[4, 4, 1], dtype=np.uint8)
    return a

