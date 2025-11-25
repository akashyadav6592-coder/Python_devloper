from PIL import Image
import os

image_path = 'path/to/your/image.jpg'

img = Image.open(image_path)


new_size = (300, 300)
resized_img = img.resize(new_size)


save_path = 'path/to/save/resized_image.jpg' 
resized_img.save(save_path)

print("Image resized and saved successfully!")

