from PIL import Image


def extract_message(img_path):
    with Image.open(img_path) as img:
        pixels = list(img.getdata())

        binary_message = ''
        for pix in pixels:
            binary_message += str(pix[0] & 1)
            binary_message += str(pix[1] & 1)
            binary_message += str(pix[2] & 1)

        terminator = '00000000'
        end = binary_message.find(terminator)
        if end != -1:
            binary_message = binary_message[:end]

        message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
        return message
