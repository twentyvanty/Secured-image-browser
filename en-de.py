import os # provides functions to interact w/os
from tkinter import TK, Button, Label, Entry, filedialog, messagebox # provides GUI elements like buttons, labels, and input fields
from PIL import Image # allows to open, manipulate, and save image
import random # shuffle the pixels in a deterministic way, using a seed

# returns a random object that can shuffle items the same way every time if given the same seed value.
def get_seeded_random(seed) :
    """Returns a seeded random generator."""
    return random.Random(seed)

# key for both encrypt and decrypt images consistently

def encrypt_image(input_image_path, output_image_path, seed):
    """Encrypts the image by manipulating pixel values."""
    image = Image.open(input_image_path)
    width, height = image.size
    
    # get pixel data as a list
    pixels = list(image.getdata())
    random_gen = get_seeded_random(seed)
    
    # Create a list of pixel indices
    indices = list(range(len(pixels)))
    #shuffle the indices using the seeded random generator
    random_gen.shuffle(indices)
    
    # reorder pixels based on shuffled indices
    encrypted_pixels = [pixels[i] for i in indices]
    
    # create new image
    encrypt_image = Image.new(image.mode, (width,height))
    # apply encrypted pixels to the new image
    encrypt_image.putdata(encrypted_pixels)
    # save the encrpyted image
    encrypt_image.save(output_image_path)
    
    return True
# load the image and extract its pixel data
# The pixel order is shuffled using a seeded random generator to ensure the same shuffle order is maintained when decrypting.
# We create a new image with the shuffled pixel values and save it as the encrypted image.

def decrypt_image(input_image_path, output_image_path, seed):
    """Decrypts the image by reversing the encryption process."""
    image = Image.open(input_image_path)
    width, height = image.size
    
    # get encrypted pixel data as a list
    encrypted_pixels = list(image.getdata())
    random_gen = get_seeded_random(seed)
    
    # create a new list to hold pixel indices in their original order
    indices = list(range(len(encrypted_pixels)))
    # shuffle the indices again to get the original order
    random_gen.shuffle(indices)
    
    # create a new image to hold the decrypted data
    decrypted_pixels = [None] * len(encrypted_pixels)
    
    # restore original pixels using the shuffled indices
    for original_index, shuffled_index in enumerate(indices):
        decrypted_pixels[shuffled_index] = encrypted_pixels[original_index]
    
    # save the decrypted image
    decrypted_image = Image.new(image.mode, (width, height))
    decrypted_image.putdata(decrypted_pixels)
    decrypt_image.save(output_image_path)
    
    return True
# Loads the encrypted image.
# Uses the same random seed to reshuffle the pixels back into their original order.
# Creates and saves a new image with the decrypted pixels.
