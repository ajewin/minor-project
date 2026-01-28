import cv2 as cv
import os
import numpy as np
import random

# -----------------------------
# Source folder
# -----------------------------
source_dir = r"C:\Users\......\Desktop\dataset"

# -----------------------------
# Output folders
# -----------------------------
target_base = r"C:\Users\.......\Desktop\augmented_check"
folders = {
    "sensor_noise": os.path.join(target_base, "sensor_noise"),
    "gaussian_blur": os.path.join(target_base, "gaussian_blur"),
    "vertical_strip": os.path.join(target_base, "vertical_strip"),
    "horizontal_strip": os.path.join(target_base, "horizontal_strip"),
    "horizontal_flip": os.path.join(target_base, "horizontal_flip"),
}

for folder in folders.values():
    os.makedirs(folder, exist_ok=True)

# -----------------------------
# Augmentation functions
# -----------------------------
def mild_sensor_noise(img):
    noise = np.random.normal(0, 5, img.shape)
    noisy = img.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def mild_gaussian_blur(img):
    return cv.GaussianBlur(img, (3, 3), 0)

def vertical_strip_mask(img):
    img = img.copy()
    h, w, c = img.shape
    strip_width = 2  # thickness of each vertical strip in pixels
    gap = 8          # space between strips

    for x in range(0, w, strip_width + gap):
        img[:, x:x + strip_width, :] = 0  # black vertical strips
    return img

def horizontal_strip_mask(img):
    img = img.copy()
    h, w, c = img.shape
    strip_height = 2  # thickness of each horizontal strip in pixels
    gap = 8           # space between strips

    for y in range(0, h, strip_height + gap):
        img[y:y + strip_height, :, :] = 0  # black horizontal strips
    return img

# -----------------------------
# Process images
# -----------------------------
for file in os.listdir(source_dir):
    if not file.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    img_name = os.path.splitext(file)[0]
    img_path = os.path.join(source_dir, file)
    img = cv.imread(img_path)
    if img is None:
        print(f"Could not read {img_path}")
        continue

    # Apply each augmentation separately
    cv.imwrite(os.path.join(folders["sensor_noise"], f"{img_name}_noise.jpg"),
               mild_sensor_noise(img))

    cv.imwrite(os.path.join(folders["gaussian_blur"], f"{img_name}_blur.jpg"),
               mild_gaussian_blur(img))

    cv.imwrite(os.path.join(folders["vertical_strip"], f"{img_name}_vstrip.jpg"),
               vertical_strip_mask(img))

    cv.imwrite(os.path.join(folders["horizontal_strip"], f"{img_name}_hstrip.jpg"),
               horizontal_strip_mask(img))

    cv.imwrite(os.path.join(folders["horizontal_flip"], f"{img_name}_flip.jpg"),
               cv.flip(img, 1))

    print(f"Processed {img_name}")

print("All augmentations saved in separate folders on Desktop!")
