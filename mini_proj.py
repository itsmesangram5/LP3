import hashlib
import exifread
from PIL import Image
import numpy as np

# Step 1: User Input
#image_path = input("Enter the path to the target image file: ")
image_path="C:\\Users\\itsme\\Dropbox\\PC\\Downloads\\t.jpg"

# Step 2: MD5 Hashing
def calculate_md5(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
        md5_hash = hashlib.md5(image_data).hexdigest()
    return md5_hash

md5_hash = calculate_md5(image_path)
print("MD5 Hash:", md5_hash)

# Step 3: EXIF Data Extraction
def extract_exif_data(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)
    return tags

exif_data = extract_exif_data(image_path)
print("EXIF Data:")
for tag, value in exif_data.items():
    print(f"{tag}: {value}")

# Step 4: Steganography Detection (Simplified LSB Analysis)
def detect_steganography(image_path):
    image = Image.open(image_path)
    pixel_values = np.array(image)
    lsb = pixel_values & 1  # Extract the least significant bit (LSB) from each pixel

    # Check for steganography (e.g., if LSB is not uniform)
    steganography_detected = np.any(lsb != lsb[0, 0, :])

    return steganography_detected

steganography_detected = detect_steganography(image_path)
if steganography_detected:
    print("Steganography Detected")
    # You might want to display or analyze the LSB data here

# Step 6: Perceptual Hashing (You'll need a suitable library for this, like imagehash)
# Install imagehash with: pip install imagehash
from PIL import Image
import imagehash

def generate_perceptual_hash(image_path):
    image = Image.open(image_path)
    phash = imagehash.phash(image)
    return phash

perceptual_hash = generate_perceptual_hash(image_path)
print("Perceptual Hash:", perceptual_hash)
