from cryptography.fernet import Fernet, InvalidToken
import base64
from pathlib import Path
from tkinter import Tk, Button, Label, filedialog, messagebox, Toplevel
from PIL import Image, ImageTk
import os

KEY_FILENAME = "filekey.key"

def generate_key():
    """Generates a Fernet key and saves it to a file."""
    key_file_path = Path("filekey.key")
    if not key_file_path.exists():
        key = Fernet.generate_key()
        with open("filekey.key", "wb") as key_file:
            key_file.write(key)
        print("Key has been generated and saved.")
    else:
        print("Key file already exists. Using existing key.")
    
def encrypt_image(image_file, key_file, out_path: str = None):
    """Encrypts an image file using a given key."""
    # Load the key from the key file
    with open(key_file, "rb") as k_file:
        key = k_file.read()
    
    # Initialize the Fernet cipher suite
    fernet = Fernet(key)
    
    # Read the original image data in binary mode
    with open(image_file, "rb") as f:
        image_data = f.read()
    
    # Encrypt the image data
    encrypted_data = fernet.encrypt(image_data)
    
    # Write the encrypted data to a new file
    if out_path is None:
        p = Path(image_file)
        base = p.stem
        ext = p.suffix or ".png"
        out_path = str(p.with_name(base + "_encrypted" + ext))

    with open(out_path, "wb") as locked_photo_file:
        locked_photo_file.write(encrypted_data)

    print(f"Image encrypted successfully and saved to: {out_path}")
    
    return out_path


def decrypt_image(encrypted_image_file, key_file, out_path: str = None):
    """Decrypts an encrypted image file using a given key."""
    # Load the key from the key file
    with open(key_file, "rb") as k_file:
        key = k_file.read()
    
    # Initialize the Fernet cipher suite
    fernet = Fernet(key)
    
    # Read the encrypted image data in binary mode
    with open(encrypted_image_file, "rb") as ef:
        encrypted_data = ef.read()
    
    # Decrypt the image data
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Write the decrypted data to a new file
    if out_path is None:
        p = Path(encrypted_image_file)
        base = p.stem
        ext = p.suffix or ".png"
        if base.endswith("_encrypted"):
            base = base[:-10]
        out_path = str(p.with_name(base + "_decrypted" + ext))

    with open(out_path, "wb") as output_file:
        output_file.write(decrypted_data)
    
    print(f"Image decrypted successfully and saved to: {out_path}")

    return out_path


def show_image_popup(image_path: str, title: str = "Image Preview"):
    """Show image in a popup window (resized to fit)."""
    try:
        img = Image.open(image_path)
    except Exception as e:
        messagebox.showerror("Preview error", f"Cannot open image for preview:\n{e}")
        return
    
    popup = Toplevel(root)
    popup.title(title)

    # imgae resizing if too big
    max_w, max_h = 800, 600
    w, h = img.size
    ratio = min(max_w / w, max_h / h, 1.0)
    img_resized = img.resize((int(w*ratio), int(h*ratio)), Image.LANCZOS)
    
    # convert
    tk_img = ImageTk.PhotoImage(img)

    # display
    lbl = Label(popup, image=tk_img)
    lbl.image = tk_img  # keep reference
    lbl.pack()

    Button(popup, text="Close", command=popup.destroy).pack(pady=6)

def select_and_process():
    """Called when user clicks Browse: choose file, then decrypt or encrypt automatically."""
    
    path = filedialog.askopenfilename(
        title="Select Image (or encrypted file)",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.gif"), ("All files", "*.*")]
    )

    if not path:
        return
    
    input_label.config(text=path)
    folder = os.path.dirname(path) or "."

    try:
        # try decrypting first
        dec_path = decrypt_image(path, KEY_FILENAME)  # uses default name near file
        messagebox.showinfo("Decrypted", f"File decrypted and saved to:\n{dec_path}")
        show_image_popup(dec_path, "Decrypted Image")

    except InvalidToken:
        # file is not encrypted with our key -> ask where to save encrypted file
        default_name = Path(path).stem + "_encrypted" + (Path(path).suffix or ".png")
        
        save_path = filedialog.asksaveasfilename(
            defaultextension=Path(path).suffix or ".png",
            initialdir=folder,
            initialfile=default_name,
            title="Save Encrypted File As"
        )

        if not save_path:
            messagebox.showinfo("Cancelled", "Encryption cancelled.")
            return
        
        try:
            enc_out = encrypt_image(path, KEY_FILENAME, out_path=save_path)
            messagebox.showinfo("Encrypted", f"Image encrypted and saved to:\n{enc_out}")
        
        except Exception as e:
            messagebox.showerror("Encryption error", f"Failed to encrypt:\n{e}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")


if __name__ == "__main__":
    generate_key()

    root = Tk()
    root.title("Image Encryption Tool")
    root.geometry("420x200")
    root.resizable(False, False)

    Label(root, text="Select Image to Encrypt/Decrypt:").pack(pady=(12,6))
    input_label = Label(root, text="No image selected", wraplength=380)
    input_label.pack(pady=6)

    Button(root, text="Browse", width=20, command=select_and_process).pack(pady=6)
    Button(root, text="Exit", width=20, command=root.destroy).pack(pady=(8,6))

    root.mainloop()