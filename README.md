
Introduction
This project uses **image steganography** to hide secret messages inside images. It provides encryption to embed messages and password-protected decryption to extract them securely.  

 Features
- Hide text messages inside images without visual changes  
- Password-protected decryption for security  
- Lightweight and efficient image processing  
- Cross-platform compatibility (Windows, Linux, Google Colab)  
- Simple and user-friendly interface  



Technologies Used
- **Python**  
- **OpenCV (`cv2`)** – For image processing  
- **NumPy (`numpy`)** – For pixel manipulation  
- **OS (`os`)** – For file handling  

 Installation & Setup  

1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
2. Run the encryption script:  
  
3. Run the decryption script:  
   
  
  
1. **Encryption:**  
   - The user enters a secret message and a passcode.  
   - The message is embedded into an image.  
   - The encrypted image is saved.  

2. **Decryption:**  
   - The user provides the encrypted image and passcode.  
   - If the passcode is correct, the hidden message is revealed.  
