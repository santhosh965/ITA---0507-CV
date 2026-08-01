import cv2
image = cv2.imread("sample4.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)
cv2.imshow("Original Image", gray)
cv2.imshow("Histogram Equalized Image", equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()