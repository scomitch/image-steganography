import LSBHide

print("Welcome to the Data Smuggling application!")

while True:
    print("Please Choose from the following:"
          "\n1: Hide a String in the image"
          "\n2: Extract a hidden string from an image")

    choice = input(":- ")

    if choice == 1:
        message = input("Please enter the string you wish to smuggle:\n:- ")
        LSBHide.smuggle_string(message)
    elif choice == 2:
        break
    else:
        print("Your choice was invalid, please try again")
