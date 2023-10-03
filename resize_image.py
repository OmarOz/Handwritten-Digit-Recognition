from PIL import Image
import os

img_num=6062
digit=1

while os.path.isfile(f'Images/IMG_{img_num}.JPG'):
    try:
        original_image=Image.open(f'Images/IMG_{img_num}.JPG')
        resized_image = original_image.resize((28, 28), Image.LANCZOS)
        resized_image.save(f'digit{digit}.png')
    except:
        print("error")
    finally:
        img_num+=1
        digit+=1    

