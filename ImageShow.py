from PIL import Image, ImageDraw, ImageFont
import os

# For this program the cover image is static
coverImage = Image.open('resources/parrots.bmp')


# Show horizontal combines the cover image with the newly generated cover image.
def show_horizontal(imagePath, hiddenMsg, out_number, show):

    # Parse some text for the unique filename.
    filename = hiddenMsg.replace(" ", "")
    filename = filename[:10]

    # Open the LSB Image
    LSBImage = Image.open(imagePath)
    dst = Image.new('RGB', (coverImage.width + LSBImage.width, LSBImage.height))
    dst.paste(coverImage, (0, 0))
    dst.paste(LSBImage, (coverImage.width, 0))

    # We need to draw some text to distinguish which image is which
    draw = ImageDraw.Draw(dst)
    font = ImageFont.load_default()

    # Draw the text on the bottom right of each image.
    draw.text((coverImage.width - 125, LSBImage.height - 30), "Cover Image (out/" + out_number + ")", fill="white", font=font)
    draw.text((dst.width - 125, LSBImage.height - 30), "LSB Image", fill="white", font=font)

    # Save the new image and try and open it with the Windows Default app.
    saved_path = 'resources/comparisons/out-' + out_number + '-cover-' + filename + "-comparison.bmp"
    dst.save(saved_path)

    if show:
        os.system(f"start {saved_path}")
