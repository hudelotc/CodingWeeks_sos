import numpy as np
import cv2

def load(filename):
     image=cv2.imread(filename)
     return image


def load_and_display (filename):
    img=cv2.imread(filename)
    print(type(img))
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




# image = load("../Data/tetris_blocks.png")
# # Affichage de la taille de l'image
# (h, w, d) = image.shape
# print("width={}, height={}, depth={}".format(w, h, d))
# # Récupération et affichade de la valeur d'un pixel à une position donnée
# (B, G, R) = image[100, 50]
# print("R={}, G={}, B={}".format(R, G, B))
# # extraction d'une zone d'interêt de taille 100x100 à partir de la position x=320,y=60
# roi = image[60:160, 320:420]
# # affichage de la région d'intérêt
# cv2.imshow("ROI", roi)
# cv2.waitKey(0)  
    
