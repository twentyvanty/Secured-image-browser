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

## Graphic User Interface (GUI)
We used **Tkinter**, Python’s built-in library for creating GUI, as the main library to create the GUI components for this project. This is done by importing the tkinter module to the project.  

```from tkinter import Tk, Button, Label, Entry, filedialog, messagebox```  
  
These are the components used in this project. More details about the Tkinter library can be found in the reference section.   
  
Components:
- To create the main window, use ```Tk()```. Then ```.title()``` to name the title of the window. Use ```.geometry()``` to set the size of the window, and use ```.resizable(False, False)``` to make sure that the window will not be resizable.
- Use ```Label()``` and ```Entry()``` for input field.
- Use ```Button()``` to create button with text, and ```.pack() to organizes the widgets in blocks before placing in the parent widget.
- Use ```filedialog.askopenfilename()``` to create file/directory selection windows for user to select input image. Then use ()```filedialog.asksaveasfilename()``` for user to choose where to save the output image.
- Use ```messagebox.showerror()``` to display error message box and ```messagebox.showinfo()``` to display information message box.
- Use ```.config()``` to change text widget.
- Use ```.cget()``` to get the text from the widget.
- Use ```.mainloop``` to keep the window open and responsive.
- Use ```.destroy()``` to close the window.

## References
- https://dev.to/immah/building-a-simple-image-encryption-tool-using-python-2439
- https://www.geeksforgeeks.org/python/python-gui-tkinter/
- https://docs.python.org/3/library/dialog.html
- https://docs.python.org/3/library/tkinter.messagebox.html
  
## Sample Image Encryption / Decryption
Original image (sample.png)  
![sample](sample.png)

Encrypted image (sample_encrypted.png)  
![sample_encrypted](sample_encrypted.png)

Decrypted image (sample_decrypted.png)  
![sample_decrypted](sample_decrypted.png)
