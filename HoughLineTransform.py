import cv2
import numpy as np

# Load the image
image_path = './images/sample.jpg'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred, threshold1=30, threshold2=150)

# Find lines using Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

# Loop through detected lines
for line in lines:
    rho, theta = line[0]
    angle = theta * 180 / np.pi

    # Filter lines based on angle
    if 45 <= angle <= 135 or 225 <= angle <= 315:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho

        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        # Draw lines on the image
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
print(angle)

cv2.imshow('Square Orientation', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
