from PIL import Image

print("Welcome to the Data Smuggling application!")

while True:
    print("Please Choose from the following:"
          "\n1: Hide a String in the image"
          "\n2: Extract a hidden string from an image"
          "\n3: Show original & altered image")

    choice = input(":- ")

    if choice == 1:
        break
    elif choice == 2:
        break
    elif choice == 3:
        break
    else:
        print("Your choice was invalid, please try again")


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