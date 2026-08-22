import cv2
image = cv2.imread("sample3.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
