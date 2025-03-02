import cv2

# Load the encrypted image
encrypted_path = "encryptedImage.jpg"
img = cv2.imread(encrypted_path)

if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Load the password
try:
    with open("password.txt", "r") as file:
        correct_password = file.read().strip()
except FileNotFoundError:
    print("Error: Password file not found!")
    exit()


password = input("Enter the passcode for decryption: ")

# Validate password
if password != correct_password:
    print("Wrong password! Decryption failed.")
    exit()


c = {i: chr(i) for i in range(255)}

# Extract message from image
message = ""
n, m, z = 0, 0, 0
for _ in range(100):  # Assuming message length is max 100 characters
    char_code = img[n, m, z]
    if char_code == 0:
        break  # Stop if message ends
    message += c[char_code]
    n = (n + 1) % img.shape[0]
    m = (m + 1) % img.shape[1]
    z = (z + 1) % 3

print("Decryption successful! Secret message:")
print(message)
