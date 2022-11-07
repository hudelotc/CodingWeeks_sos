from image_processing_operations import *
from loading import *
import argparse
import numpy as np
import cv2
import sys


def apply_processing(image,process):
    imagedest=image
    if process == "resizing":
        new_size = input("What is the new size (two numbers separated by a space)  ?")
        l = new_size.split()
        dims=[]
        for i in l :
            dims.append(int(i))
        new_dims = tuple(dims)
        imagedest = resize_image(image,new_dims)
    return imagedest
    
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="path to input image")
    ap.add_argument("-o", "--output", required=True, help="path to output image")
    ap.add_argument("-p", "--processing", required=True, help="type of processing")
    args = vars(ap.parse_args())
    image_source_filename = args["input"]
    processing = args["processing"]
    image_dest = args["output"]
    image_source = load(image_source_filename)
    dest = apply_processing(image_source,  processing)
    cv2.imwrite(image_dest, dest)


