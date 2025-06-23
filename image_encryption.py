from PIL import Image
import numpy as np
import random

def encrypt_image(input_path, output_path, key, color_shift):
    img = Image.open(input_path).convert("RGB")
    img_array = np.array(img)
    h, w, _ = img_array.shape

    flat_pixels = img_array.reshape(-1, 3)

    random.seed(key)
    indices = list(range(len(flat_pixels)))
    random.shuffle(indices)

    
    permuted_pixels = flat_pixels[indices]

    
    permuted_pixels = permuted_pixels.astype(np.uint8)

    encrypted_img_array = permuted_pixels.reshape(h, w, 3)
    encrypted_img = Image.fromarray(encrypted_img_array)
    encrypted_img.save(output_path)

    print(f"Encrypted image saved as: {output_path}")

if __name__ == "__main__":
    encrypt_image("sample.png", "encrypted_sample.png", key=9876, color_shift=50)

