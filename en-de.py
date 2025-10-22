import os
from tkinter import Tk, Button, Label, Entry, filedialog, messagebox 
from PIL import Image 
import random 

def get_seeded_random(seed) :
    """Returns a seeded random generator."""
    return random.Random(seed)


def encrypt_image(input_image_path, output_image_path, seed):
    """Encrypts the image by manipulating pixel values."""
    with Image.open(input_image_path) as image:
        width, height = image.size
        pixels = list(image.getdata())
        mode = image.mode
    
    random_gen = get_seeded_random(seed)
    indices = list(range(len(pixels)))
    random_gen.shuffle(indices)
    
    encrypted_pixels = [pixels[i] for i in indices]
    
    encrypted_image = Image.new(mode, (width,height))
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save(output_image_path)
    
    return True


def decrypt_image(input_image_path, output_image_path, seed):
    """Decrypts the image by reversing the encryption process."""
    with Image.open(input_image_path) as image:
        width, height = image.size
        encrypted_pixels = list(image.getdata())
        mode = image.mode
    
    random_gen = get_seeded_random(seed)
    indices = list(range(len(encrypted_pixels)))
    random_gen.shuffle(indices)
    
    decrypted_pixels = [None] * len(encrypted_pixels)
    
    for original_index, shuffled_index in enumerate(indices):
        decrypted_pixels[shuffled_index] = encrypted_pixels[original_index]
    
    decrypted_image = Image.new(mode, (width, height))
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save(output_image_path)
    
    return True


def select_input_img():
    """Opens a file dialog to select an input image."""
    input_image_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.gif"), ("All files", "*.*")]
    )
    input_image_label.config(text=input_image_path)


def select_output_img(input_image_path, mode):
    """Opens a file dialog to select an output image path."""

    base, ext = os.path.splitext(os.path.basename(input_image_path))

    if mode == "Encrypt" :
        default_name = base + "_encrypted"  + ext
    else :
        if base.endswith("_encrypted"):
            base = base[:-10]
        default_name = base + "_decrypted"  + ext

    output_image_path = filedialog.asksaveasfilename(
        defaultextension=".png", 
        initialfile=default_name,
        filetypes=[("PNG files", "*.png"),("JPEG files", "*.jpg;*.jpeg"),("All files", "*.*")], 
        title=f"Save {mode} Image"
    )

    return output_image_path


def button_encrypt():
    
    input_image_path = input_image_label.cget("text")

    seed = seed_entry.get().strip()
    if not seed:
        messagebox.showerror("Error", "Please enter a seed (integer).")
        return
    
    try:
        int(seed)
    except ValueError:
        messagebox.showerror("Error", "Seed must be an integer.")
        return

    if not input_image_path:
        messagebox.showerror("Error", "Please select input image.")
        return       
    
    output_image_path = select_output_img(input_image_path, "Encrypt")
    
    if not output_image_path:
            return
    
    if encrypt_image(input_image_path, output_image_path, seed):
        messagebox.showinfo("Success", "Image encrypted successfully!")
        root.destroy()


def button_decrypt():

    input_image_path = input_image_label.cget("text")
    seed = seed_entry.get().strip()

    if not seed:
        messagebox.showerror("Error", "Please enter a seed (integer).")
        return
    
    try:
        int(seed)
    except ValueError:
        messagebox.showerror("Error", "Seed must be an integer.")
        return

    if not input_image_path:
        messagebox.showerror("Error", "Please select input and output images.")
        return
    
    output_image_path = select_output_img(input_image_path, "Decrypt")

    if decrypt_image(input_image_path, output_image_path, seed):
        messagebox.showinfo("Success", "Image decrypted successfully!")
        root.destroy()

# main
root = Tk()
root.title("Image Encryption Tool")
root.geometry("400x400")
root.resizable(False, False)

Label(root, text="Select Image to Encrypt/Decrypt:").pack(pady=5)
input_image_label = Label(root, text="No image selected")
input_image_label.pack(pady=5)
Button(root, text="Browse", command=select_input_img).pack(pady=5)

Label(root, text="Enter Seed Key:").pack(pady=5)
seed_entry = Entry(root)
seed_entry.pack(pady=5)
seed_entry.insert(0, "12345")

Button(root, text="Encrypt Image", width=20, command=button_encrypt).pack(pady=5)
Button(root, text="Decrypt Image", width=20, command=button_decrypt).pack(pady=5)
root.mainloop()
