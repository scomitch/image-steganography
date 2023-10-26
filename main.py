import os
import sys

import LSBExtract
import LSBHide


# Menu function, prompts the user for entering LSB information.
# LSBHide (Hides a string into the cover image)
# List Images (Lists all images in the out folder, giving an option to choose which one to pull a message from)
def menu():
    while True:
        print("Main Menu - Please Choose from the following:"
              "\n1: Hide a String in the image"
              "\n2: Extract a hidden string from an image"
              "\n3: Quit")

        choice = input(":- ")

        try:
            choice = int(choice)
        except ValueError:
            print("\n! Error: Please enter a valid number between 1 and 4 !\n")

        if choice == 1:
            message = input("Please enter the string you wish to smuggle:\n:- ")
            LSBHide.smuggle_string(message)
        elif choice == 2:
            list_images()
        elif choice == 3:
            sys.exit(1)
        else:
            print("Your choice was invalid, please try again")


def list_images():
    all_images = [f for f in os.listdir('resources/out') if os.path.isfile(os.path.join('resources/out', f))]

    if not all_images:
        print("There are no images with smuggled data currently stored.")
        return None

    all_images.sort()

    for index, filename in enumerate(all_images, 1):
        print(f"{index}: {filename}")

    while True:
        try:
            img_choice = int(input("Please choose from the above options: "))
            if 1 <= img_choice <= len(all_images):
                selected_image = all_images[img_choice - 1]
                print(f"Selected Image: {selected_image}")
                print(LSBExtract.extract_message(os.path.join('resources/out/', selected_image)))
                break
            else:
                print("Invalid Selection. Please try again.")
        except:
            print("\nPlease enter a numerical option as listed.")

    menu()


if __name__ == "__main__":
    try:
        print("Welcome to the Data Smuggling application!")
        menu()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
