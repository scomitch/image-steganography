from PIL import Image


# This method extracts any hidden message from an image.
def extract_message(img_path):

    # Keep the image open whilst we process.
    with Image.open(img_path) as img:

        # Vars awaiting the hidden message
        binary_message = ''
        terminator = '00000000'

        # Get the pixels of the image
        pixels = list(img.getdata())

        # Loop through the RGB channels of the pixel so we can get the binary.
        for pix in pixels:
            binary_message += str(pix[0] & 1)
            binary_message += str(pix[1] & 1)
            binary_message += str(pix[2] & 1)

        # Find the end index where we have our terminator (set in LSBHide)
        end = binary_message.find(terminator)

        # If we have a terminator, i.e. one is found in the image.
        # Get our message from the starting index to the terminator
        if end != -1:
            binary_message = binary_message[:end]

        # Process the message by conerting back
        message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
        return message
