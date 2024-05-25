import cv2
import os

# Read the image
img = cv2.imread("bg.jpg")

# Ensure the image is read correctly
if img is None:
    raise FileNotFoundError("The image file was not found.")

msg = input("Enter secret message: ")
password = input("Enter a password: ")

# Create dictionaries for character to ASCII and vice versa
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Initialize indices
n = 0
m = 0
z = 0

# Ensure the image has enough pixels to hold the message
if len(msg) > img.size // 3:
    raise ValueError("The message is too long to fit in the image.")

# Embed the message in the image
for char in msg:
    img[n, m, z] = d[char]
    z += 1
    if z == 3:
        z = 0
        m += 1
        if m == img.shape[1]:
            m = 0
            n += 1
            if n == img.shape[0]:
                raise ValueError("The image is too small to hold the message.")

# Save the modified image
cv2.imwrite("encryptedImage.jpg", img)

# Open the image (this works on Windows)
if os.name == 'nt':
    os.startfile("encryptedImage.jpg")
else:
    # For macOS
    if sys.platform == "darwin":
        os.system(f"open encryptedImage.jpg")
    # For Linux
    else:
        os.system(f"xdg-open encryptedImage.jpg")

# Decryption process
message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for _ in range(len(msg)):
        message += c[img[n, m, z]]
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m == img.shape[1]:
                m = 0
                n += 1
    print("Decrypted message =", message)
else:
    print("Authentication failed")
