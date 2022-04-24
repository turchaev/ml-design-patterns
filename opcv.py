import cv2
my_photo = cv2.imread('foto1.png')
cv2.imshow('MyPhoto', my_photo)
cv2.waitKey(0)
cv2.destroyAllWindows()