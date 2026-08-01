import cv2
import os
image_path = "sample1.png"
if not os.path.exists(image_path):
    print("Image not found")
else:
    image = cv2.imread(image_path)
    if image is None:
        print("Could not read image")
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Original Image", image)
        cv2.imshow("Grayscale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()