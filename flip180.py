import cv2 


for i in range(0,819):
    name = "up" + str(i) + ".jpg"
    image = cv2.imread(name)
    rotated = cv2.flip(image,0)
    name = "upSign" + str(i) + ".jpg"
    cv2.imwrite(name, rotated)