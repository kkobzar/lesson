import cv2


image = cv2.imread('hooman.jpg')
print(image)

cv2.imshow('Hooman', image)

cv2.waitKey()