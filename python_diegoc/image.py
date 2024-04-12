import cv2 
imagen = cv2.imread("paisaje.jpg",1)
cv2.imshow("paisaje", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
