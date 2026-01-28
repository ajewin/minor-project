import cv2 as cv
import os

# -----------------------------
# Directories
# -----------------------------

# Base directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Source directory containing your original images
source_dir = r"C:\Users\.........\Downloads\No gesture"

# Target directory where grayscale images will be saved
target_dir = os.path.join(BASE_DIR, "convertedGrayScaleDataset1")
os.makedirs(target_dir, exist_ok=True)

# -----------------------------
# Process images
# -----------------------------

for root, dirs, files in os.walk(source_dir):
    for file in files:
        # Only process .jpg, .jpeg, .png files
        if not file.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        img_name = os.path.splitext(file)[0]  # Get filename without extension
        img_path = os.path.join(root, file)

        # Read the image
        img = cv.imread(img_path)
        if img is None:
            print(f"Could not read image: {img_path}, skipping")
            continue

        # Convert to grayscale
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Resize to 96x96
        resized = cv.resize(gray, (96, 96))

        # Recreate folder structure in target directory
        rel_path = os.path.relpath(root, source_dir)
        out_folder = os.path.join(target_dir, rel_path)
        os.makedirs(out_folder, exist_ok=True)

        # Save the processed image
        save_path = os.path.join(out_folder, f"{img_name}_gray.jpg")
        cv.imwrite(save_path, resized)
        print(f"Processed {img_name} -> {save_path}")

print("All images processed!")
