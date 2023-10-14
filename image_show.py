from PIL import Image

image = Image.open('resources/Baboon.bmp')
image1 = Image.open('resources/out/out-1.bmp')

def show_horizontal(image, image1):
    dst = Image.new('RGB', (image.width + image1.width, image1.height))
    dst.paste(image, (0, 0))
    dst.paste(image1, (image.width, 0))
    return dst


show_horizontal(image, image).save('resources/Baboon.bmp')
