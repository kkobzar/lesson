import cv2


image = cv2.imread('monke-hooman.jpeg')

casc = cv2.CascadeClassifier('haarcascade_eye.xml')

eyes = casc.detectMultiScale(image)


for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 2)


cv2.imshow('Hooman', image)

cv2.waitKey()