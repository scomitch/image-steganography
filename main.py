import os

from PIL import Image

import LSBExtract
import LSBHide


def menu():
    print("Welcome to the Data Smuggling application!")
    print("Please Choose from the following:"
          "\n1: Hide a String in the image"
          "\n2: Extract a hidden string from an image")

    choice = input(":- ")

    if choice == 1:
        message = input("Please enter the string you wish to smuggle:\n:- ")
        LSBHide.smuggle_string(message)
    elif choice == 2:
        LSBExtract.extract_message(list_images())
    else:
        print("Your choice was invalid, please try again")

def list_images():
    all_images = [f for f in os.listdir('resources/out') if os.path.isfile((os.path.join('resources/out'), f))]

    if not all_images:
        print("There are no images with smuggled data currently stored.")
        return None

    for index, filename in enumerate(all_images, 1):
        print(f"{index + 1}: {filename}")

    while True:
        try:
            img_choice = int(input("Please choose from the above options: "))
            if 1 <= img_choice <= len(all_images):
                selected_image = all_images[img_choice - 1]
                print(f"Selected Image: {selected_image}")
                return os.path.join('resources/out/', selected_image)
            else:
                print("Invalid Selection. Please try again.")
        except:
            print("Please enter a numerical option as listed.")


def check_constraints(image_path, string_to_hide):

    # Open up the cover image using pillow
    cover_image = Image.open(image_path)

    # Make sure the cover image is a .bmp
    print(cover_image.format)
    if cover_image.format != "BMP":
        return False

    # Make sure the image is full RGB, i.e. 24 bit color mapping
    print(cover_image.mode)
    if cover_image.mode != "RGB":
        return False

    # Get the width, height of the image, multiply by 3 to get total bytes.
    w, h = cover_image.size

    # Number of bytes available, minus 54 bytes for metadata and
    image_bytes_allocated = ((w * h * 3) - 54) // 8
    print(image_bytes_allocated)

    # Get the number of bytes in a string
    string_bytes = len(string_to_hide)
    print(string_bytes)
    if string_bytes >= image_bytes_allocated:
        return False

    return True


if __name__ == "__main__":
    check_constraints("resources/parrots.bmp", "Hi my name is bob")