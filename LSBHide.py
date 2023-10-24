from PIL import Image
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
        img.save('resources/out/out.bmp')


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
