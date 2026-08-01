import cv2
import matplotlib.pyplot as plt
image = cv2.imread("sample5.png")
cv2.imshow("Original Image", image)
for i, color in enumerate(('b', 'g', 'r')):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title("Color Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()