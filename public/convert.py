from PIL import Image
import os

# === CONFIG ===
input_folder = "./images"  # Path to your image folder
output_folder = "./images_web"  # Output folder
max_size = (2560, 2560)  # Resize to fit within this (width, height)
convert_to_webp = True  # Set False to save as optimized JPG

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported input formats
extensions = (".jpg", ".jpeg", ".JPG", ".JPEG")

# Process each file
for filename in os.listdir(input_folder):
    if filename.endswith(extensions):
        input_path = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, f"{base_name}.webp" if convert_to_webp else f"{base_name}.jpg")

        with Image.open(input_path) as img:
            img.thumbnail(max_size, Image.LANCZOS)
            if convert_to_webp:
                img.save(output_path, "WEBP", quality=80)
            else:
                img.save(output_path, "JPEG", optimize=True, quality=75)

        print(f"Converted {filename} → {output_path}")
