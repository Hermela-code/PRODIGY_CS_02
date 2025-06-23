# Image Encryption with Pixel Permutation and Color Shifting

This is a simple Python script for encrypting images by scrambling pixel positions and shifting their color values. It uses the Python `Pillow` and `NumPy` libraries.

---

##  How It Works

- The image is read and converted into an array of pixels.
- The pixels are randomly shuffled based on a key you provide.
- Each pixel’s RGB values are then shifted by a fixed amount (also set by you).
- The result is saved as a new, encrypted image.

**Important:**  
To decrypt, you'd need to reverse the exact same steps using the same key and color shift value.

---

## Requirements

- Python 3
- Pillow
- NumPy

To install the required packages:

```bash
pip install pillow numpy

###If you're on a restricted Linux environment like Kali, use a virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install pillow numpy

## How to Use
**python3 encrypt.py**

## Settings

You can adjust two values in encrypt.py:

    **key** → controls how the pixels are shuffled

    **color_shift** → controls how much each color value is changed
DEMO - ** encrypt_image("sample.png", "encrypted_sample.png", key=9876, color_shift=50)
**

## Notes

Always use .png images to avoid compression issues.

Decryption is possible only if you have the exact key and color_shift used during encryption.
