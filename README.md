# Secured-image-browser
An image browser built with python that allow user to encrypt / decrypt image. The encryption and decryption function performed automatically once saving or opening an image file. The browser support image raw file format, e.g., *.bmp.

## Setup Project
- Open command prompt on laptop
  1. type ```python -m pip install --upgrade pip```
  2. type ```python -m pip install pillow```
  3. type ```python -m pip install cryptography```
- Create file on vs code and import library following below
  1. ```import os # provides functions to interact w/os```
  2. ```from tkinter import Tk, Button, Label, Entry, filedialog, messagebox # provides GUI elements like buttons, labels, and input fields```
  3. ```from PIL import Image, ImageTk # allows to open, manipulate, and save image```
  4. ```import random # shuffle the pixels in a deterministic way, using a seed```
     
## Program Execution
- Run the program in vscode using ```python en-de.py```
- Select input image to encrypt / decrypt
- Enter seed key (must be integer)
- Click Encrypt / Decrypt button
- Choose the path to save the output image. User can modify the output image name, however, a suggested name is given as default.
- The program successfully encrypte / decrypt the image.
  
## Sample Image Encryption / Decryption
Original image (sample.png)  
![sample](sample.png)

Encrypted image (sample_encrypted.png)  
![sample_encrypted](sample_encrypted.png)

Decrypted image (sample_decrypted.png)  
![sample_decrypted](sample_decrypted.png)
