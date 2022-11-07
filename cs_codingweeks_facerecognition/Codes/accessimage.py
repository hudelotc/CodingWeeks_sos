from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

import requests
import cv2



subscription_key = "aba0684df3f542eeaa6ae939cfbc664c"
search_term = "Celine Hudelot"

client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))

image_results = client.images.search(query=search_term) 
print(image_results)

if image_results.value:
    first_image_result = image_results.value[1]
    print("Total number of images returned: {}".format(len(image_results.value)))
    print("First image thumbnail url: {}".format(
        first_image_result.thumbnail_url))
    print("First image content url: {}".format(first_image_result.content_url))
    img_data = requests.get(first_image_result.content_url).content
    with open('image_name.jpg', 'wb') as handler:
         handler.write(img_data)
else:
    print("No image results returned!")


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread('image_name.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w] 
    roi_color = img[y:y+h, x:x+w]

cv2.imwrite("face_detection.png",img)

cv2.imshow('img',img)
cv2.waitKey(0)