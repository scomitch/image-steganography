from PIL import Image


def smuggle_string(message):
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '00000000'

    with Image.open('resources/Baboon.bmp') as img:
        pixels = list(img.getdata())

        binary_index = 0
        new_pixels = []

        for pix in pixels:
            if binary_index < len(binary_message):
                r = pix[0] & ~1 | int(binary_message[binary_index])
                binary_index += 1

                g = pix[1]
                b = pix[2]

                if binary_index < len(binary_message):
                    g = g & ~1 | int(binary_message[binary_index])
                    binary_index += 1

                if binary_index < len(binary_message):
                    b = b & ~1 | int(binary_message[binary_index])
                    binary_index += 1

                new_pixel = (r, g, b)
                new_pixels.append(new_pixel)
            else:
                new_pixels.append(pix)

        img.putdata(new_pixels)
        img.save('resources/out/out.bmp')
