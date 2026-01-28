import os
import random
import shutil

# -----------------------------
# Source folder with all images
# -----------------------------
source_dir = r"C:\Users\...........\Desktop\dataset"

# -----------------------------
# Destination folder (automatically on Desktop)
# -----------------------------
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
dest_base = os.path.join(desktop, "dataset_split")

# Split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create destination folders
train_dir = os.path.join(dest_base, "train")
val_dir = os.path.join(dest_base, "val")
test_dir = os.path.join(dest_base, "test")

for d in [train_dir, val_dir, test_dir]:
    os.makedirs(d, exist_ok=True)

print(f"Folders created at: {dest_base}")

# -----------------------------
# Get all image files
# -----------------------------
all_files = [f for f in os.listdir(source_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

# Shuffle files randomly
random.shuffle(all_files)

# Compute split indices
total = len(all_files)
train_end = int(total * train_ratio)
val_end = train_end + int(total * val_ratio)

# Split files
train_files = all_files[:train_end]
val_files = all_files[train_end:val_end]
test_files = all_files[val_end:]

# Function to copy files
def copy_files(file_list, dest_folder):
    for f in file_list:
        src_path = os.path.join(source_dir, f)
        dst_path = os.path.join(dest_folder, f)
        shutil.copy2(src_path, dst_path)

# -----------------------------
# Copy files to respective folders
# -----------------------------
copy_files(train_files, train_dir)
copy_files(val_files, val_dir)
copy_files(test_files, test_dir)

# -----------------------------
# Print summary
# -----------------------------
print(f"Total images: {total}")
print(f"Training set: {len(train_files)} images")
print(f"Validation set: {len(val_files)} images")
print(f"Test set: {len(test_files)} images")
print(f"Data split completed! Check the folder: {dest_base}")
