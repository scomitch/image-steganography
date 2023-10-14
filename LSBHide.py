from PIL import Image
import sys

cover_image = 'resources/parrots.bmp'


def smuggle_string(message):

    constraint_check = check_constraints(cover_image, message)
    if not constraint_check:
        print("Image and message does not comply with constraints. Exiting.")
        sys.exit(1)

    binary_message = ''.join(format(ord(char), '08b') for char in message) + '00000000'

    with Image.open(cover_image) as img:
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


def check_constraints(image_path, string_to_hide):

    # Open up the cover image using pillow
    cover = Image.open(image_path)

    # Make sure the cover image is a .bmp
    print('You have passed in an image with the format: ' + cover.format)
    if cover.format != "BMP":
        return False

    # Make sure the image is full RGB, i.e. 24 bit color mapping
    print('You have passed in an image with the color mapping ' + cover.mode)
    if cover.mode != "RGB":
        return False

    # Get the width, height of the image, multiply by 3 to get total bytes.
    w, h = cover.size

    # Number of bytes available, minus 54 bytes for metadata and
    image_bytes_allocated = ((w * h * 3) - 54) // 8
    print('The number of bytes allocated to hiding is: ' + str(image_bytes_allocated))

    # Get the number of bytes in a string
    string_bytes = len(string_to_hide)
    print('The number of bytes of hidden message is: ' + str(string_bytes))
    if string_bytes >= image_bytes_allocated:
        return False

    return True
