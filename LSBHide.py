import os
import re

from PIL import Image
from ImageShow import show_horizontal
import sys

cover_image = 'resources/parrots.bmp'


def smuggle_string(message):
    # Check for the constraints for the image, if it fails, return back to the menu
    constraint_check = check_constraints(cover_image, message)
    if not constraint_check:
        return

    # Turns our string into binary, with trailing 0's to indicate the message has terminated.
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '00000000'

    # Keep the image open and parse data.
    with Image.open(cover_image) as img:

        # Fetch the pixels of the image so we know the positioning on where to hide the data
        pixels = list(img.getdata())

        # Vars to instantiate the LSB algorithm
        binary_index = 0
        new_pixels = []

        # For each pixel in the pixel array (note: this is an RGB tuple)
        for pix in pixels:

            # Make sure we're not exceeding the length of the message in binary
            if binary_index < len(binary_message):

                # pix[0] is the red channel and clears the LSB of the channel.
                # | is a bitwise OR, setting the LSB of RED to the next bit on the binary
                r = pix[0] & ~1 | int(binary_message[binary_index])

                # Next bit in the message.
                binary_index += 1

                # Get the Green and Blue channels.
                g = pix[1]
                b = pix[2]

                # Is there still a bit to hide? If so repeat for the green channel.
                if binary_index < len(binary_message):
                    g = g & ~1 | int(binary_message[binary_index])
                    binary_index += 1

                # Is there still a bit again? If so hide in the blue channel.
                if binary_index < len(binary_message):
                    b = b & ~1 | int(binary_message[binary_index])
                    binary_index += 1

                # Set the new pixel with the changed RGB above and append it to the array.
                new_pixel = (r, g, b)
                new_pixels.append(new_pixel)
            else:
                # Message length has been exceeded, continue as normal.
                new_pixels.append(pix)

        # Set the data.
        img.putdata(new_pixels)
        out_number = str(check_output_number('resources/out'))
        img_string = 'resources/out/out-' + out_number + '.bmp'
        img.save(img_string)

        print("Enter 'y' if you would like to see a comparison of the cover image and newly generate image. Else press enter")
        choice = input(":- ")
        if choice == 'y':
            # Display image.
            show_horizontal(img_string, message, out_number, True)
        else:
            show_horizontal(img_string, message, out_number, False)



# Checks for predefined constraints and ensures the cover image passes checks.
def check_constraints(image_path, string_to_hide):

    # Open up the cover image using pillow
    cover_image = Image.open(image_path)

    # Make sure the cover image is a .bmp
    if cover_image.format != "BMP":
        print("\n ! Error: The image must be in .bmp format !\n")
        return False

    # Make sure the image is full RGB, i.e. 24 bit color mapping
    if cover_image.mode != "RGB":
        print("\n ! Error: The image must have 24 bit color mapping !\n")
        return False

    # Get the width, height of the image, multiply by 3 to get total bytes.
    w, h = cover_image.size

    # Number of bytes available, minus 54 bytes for metadata and
    image_bytes_allocated = ((w * h * 3) - 54) // 8

    # Get the number of bytes in a string
    string_bytes = len(string_to_hide)
    if string_bytes >= image_bytes_allocated:
        print("\n ! Error: The message you are trying to hide is too long for the image !\n")
        return False

    return True


def check_output_number(file_path):
    files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
    numbers = []
    for fi in files:
        match = re.search(r'(\d+)(?:\.\w+)?$', fi)
        if match:
            numbers.append(int(match.group(1)))

    if len(numbers) == 5:
        file_to_delete = min(numbers)
        remove_string = file_path + '/out-' + str(file_to_delete) + '.bmp'
        os.remove(os.path.join(remove_string))
        print(f"Deleted output file: ", remove_string)

    if numbers:
        next_number = max(numbers) + 1
    else:
        next_number = 1

    return next_number
