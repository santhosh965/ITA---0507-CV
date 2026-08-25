import cv2

# -----------------------------------------
# Image Watermarking using OpenCV
# -----------------------------------------

# Load the original image
original = cv2.imread("sample3.png")

# Load the watermark image
watermark = cv2.imread("watermark.png")

# Check whether images are loaded
if original is None:
    print("Error: Original image not found!")
    exit()

if watermark is None:
    print("Error: Watermark image not found!")
    exit()

# Resize watermark
watermark_width = 250
watermark_height = 100

watermark = cv2.resize(
    watermark,
    (watermark_width, watermark_height)
)

# Get original image dimensions
height, width = original.shape[:2]

# Position of watermark
# Bottom-right corner
x = width - watermark_width - 20
y = height - watermark_height - 20

# Make sure the watermark fits inside the image
if x < 0 or y < 0:
    print("Error: Watermark is too large for the original image!")
    exit()

# Select the region of interest (ROI)
roi = original[
    y:y + watermark_height,
    x:x + watermark_width
]

# Transparency of watermark
alpha = 0.4

# Blend watermark with the original image
watermarked_roi = cv2.addWeighted(
    roi,
    1 - alpha,
    watermark,
    alpha,
    0
)

# Put the blended region back into the original image
original[
    y:y + watermark_height,
    x:x + watermark_width
] = watermarked_roi

# Display the result
cv2.imshow("Original Image", cv2.imread("sample3.png"))
cv2.imshow("Watermarked Image", original)

# Save the watermarked image
cv2.imwrite("watermarked_output.jpg", original)

print("Watermark inserted successfully!")
print("Saved as: watermarked_output.jpg")

# Wait for a key press
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()