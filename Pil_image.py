from PIL import Image
import os

# Step 1: इमेज का पाथ दें
image_path = 'path/to/your/image.jpg'  # उदाहरण: 'C:/Users/YourName/Pictures/photo.jpg'

# Step 2: इमेज खोलें
img = Image.open(image_path)

# Step 3: Resize करें (width, height)
new_size = (300, 300)
resized_img = img.resize(new_size)


save_path = 'path/to/save/resized_image.jpg' 
resized_img.save(save_path)

print("Image resized and saved successfully!")
