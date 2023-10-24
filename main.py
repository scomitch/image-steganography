import LSBExtract
import LSBHide


def menu():
    print("Welcome to the Data Smuggling application!")
    print("Please Choose from the following:"
          "\n1: Hide a String in the image"
          "\n2: Extract a hidden string from an image"
          "\n3: Show original & altered image")

    choice = input(":- ")

    if int(choice) == 1:
        message = input("Please enter the string you wish to smuggle:\n:- ")
        LSBHide.smuggle_string(message)
    elif int(choice) == 2:
        list_images()
    elif int(choice) == 3:
        print("todo")
        # image_show
    else:
        print("Your choice was invalid, please try again")

1
def list_images():

    print(LSBExtract.extract_message('resources/out/out.bmp'))


    # all_images = [f for f in os.listdir('resources/out') if os.path.isfile((os.path.join('resources/out'), f))]
    #
    # if not all_images:
    #     print("There are no images with smuggled data currently stored.")
    #     return None
    #
    # for index, filename in enumerate(all_images, 1):
    #     print(f"{index + 1}: {filename}")
    #
    # while True:
    #     try:
    #         img_choice = int(input("Please choose from the above options: "))
    #         if 1 <= img_choice <= len(all_images):
    #             selected_image = all_images[img_choice - 1]
    #             print(f"Selected Image: {selected_image}")
    #             LSBExtract.extract_message(os.path.join('resources/out/', selected_image))
    #         else:
    #             print("Invalid Selection. Please try again.")
    #     except:
    #         print("Please enter a numerical option as listed.")


if __name__ == "__main__":
    menu()
