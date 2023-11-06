import hashlib
from PIL import Image
from imagehash import dhash

def compute_hash(filepath):
    """Compute MD5 hash of an image file."""
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def extract_exif(filepath):
    """Extract EAXIF data from an image file."""
    with Image.open(filepath) as img:
        exif_data = img._getexif()
        return exif_data

def detect_steganography(filepath):
    """Detect steganography using LSB analysis."""
    with Image.open(filepath) as img:
        width, height = img.size
        pixel_data = list(img.getdata())
        hidden_data = ''
        for pixel in pixel_data:
            for color_channel in pixel:
                hidden_data += str(color_channel & 1)
        return hidden_data

def perceptual_hash(filepath):
    """Generate perceptual hash of an image."""
    with Image.open(filepath) as img:
        hash_value = dhash(img)
        return str(hash_value)

def main():
    filepath = "C:\\Users\\itsme\\Dropbox\\PC\\Downloads\\t.jpg"

    md5_hash = compute_hash(filepath)
    print(f'MD5 Hash: {md5_hash}')

    exif_data = extract_exif(filepath)

    if exif_data is not None:
        print('\nEXIF Data:')
        for tag, value in exif_data.items():
            print(f'Tag: {tag}, Value: {value}')
    else:
        print('No EXIF data found.')

    hidden_data = detect_steganography(filepath)
    if hidden_data:
        print(f'\nSteganography Detected: {hidden_data[:100]}...')
    else:
        print('No steganography detected.')

    phash = perceptual_hash(filepath)
    print(f'\nPerceptual Hash: {phash}')

if __name__ == '__main__':
    main()
