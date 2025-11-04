import os

# Step 1: Define the path to your image folder
image_folder = 'path/to/your/image/folder'  # e.g., 'C:/Users/YourName/Pictures'

# Step 2: List all files in the folder
all_files = os.listdir(image_folder)

# Step 3: Filter image files (jpg, png, etc.)
image_files = [f for f in all_files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# Step 4: Print image file names
for image in image_files:
    print(image)
