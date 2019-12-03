import cv2 


for i in range(0,819):
    name = "frame" + str(i) + ".jpg"
    image = cv2.imread(name)
    rotated = cv2.flip(image,0)
    name = "uparrow" + str(i) + ".jpg"
    cv2.imwrite(name, rotated)