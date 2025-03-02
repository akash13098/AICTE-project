import cv2
import os

# Read the image
img_path = "image.jpg"  # Change this if needed
img = cv2.imread(img_path)

if img is None:
    print("Error: Image not found!")
    exit()

# Input secret message and password
msg = input("Enter the secret message: ")
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(255)}

# Encode message into the image
n, m, z = 0, 0, 0
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = (n + 1) % img.shape[0]
    m = (m + 1) % img.shape[1]
    z = (z + 1) % 3

# Save encrypted image
encrypted_path = "encryptedImage.jpg"
cv2.imwrite(encrypted_path, img)
print(f"Encryption completed! Image saved as {encrypted_path}")


with open("password.txt", "w") as file:
    file.write(password)

print("Password saved for decryption.")
