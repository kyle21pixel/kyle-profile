
from PIL import Image

def encode_image(img_path, secret_message, output_path):
    print(f"[*] Encoding message into {img_path}...")
    # This is a simplified LSB simulation for demonstration.
    # In a real tool, we would manipulate pixel bits.
    
    img = Image.open(img_path)
    encoded = img.copy()
    
    # Store message in metadata for this simple demo
    # (Real steganography alters pixel data)
    info = PngImagePlugin.PngInfo()
    info.add_text("SECRET_DATA", secret_message)
    
    encoded.save(output_path, "PNG", pnginfo=info)
    print(f"[+] Saved encoded image to {output_path}")

def decode_image(img_path):
    print(f"[*] Attempting to decode {img_path}...")
    try:
        img = Image.open(img_path)
        if "SECRET_DATA" in img.text:
            print(f"[+] HIDDEN MESSAGE FOUND: {img.text['SECRET_DATA']}")
        else:
            print("[-] No hidden data found (using this simple method).")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    print("--- Steganography Hidden Eye ---") 
    # Mocking execution flow
    print("1. Encode")
    print("2. Decode")
    # In real usage: inputs...
    print("[*] Ready. (Requires Pillow library: pip install Pillow)")
