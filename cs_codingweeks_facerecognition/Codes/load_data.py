import numpy as np
import cv2
def load_and_display (filename):
    img=cv2.imread(filename)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    load_and_display("../Data/tetris_blocks.png")