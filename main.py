import cv2

# Load the image (replace 'path' with your image file path)

image = cv2.imread('Photos/meme.jpg')

# Specify text details
text = 'academic stress'
font = cv2.FONT_HERSHEY_SIMPLEX
org = (100, 360)  # Bottom-left corner coordinates
fontScale = 1
color = (0, 255, 0)  # Blue color
thickness = 2

# Add text to the image
image = cv2.putText(image, text, org, font, fontScale, color, thickness, cv2.LINE_AA)

# Specify text details for the second box
text2 = 'me'
org2 = (680, 450)  # Bottom-left corner coordinates for the second box
color2 = (0, 0, 255)  # Red color

# Add text to the image for the second box
image = cv2.putText(image, text2, org2, font, fontScale, color2, thickness, cv2.LINE_AA)

# Resizing the newly edited image
resized = cv2.resize(image, (700, 800))

# Saving the newly edited meme
cv2.imwrite('modified_meme.jpg', resized)


# Display the modified image
cv2.imshow('Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

