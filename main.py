from organizer import organize_files


from organizer import organize_files


def display_menu():
    print("\n" + "=" * 40)
    print("      AUTOMATED FILE ORGANIZER")
    print("=" * 40)
    print("1. Organize Files")
    print("2. View Log")
    print("3. Exit")
    print("=" * 40)


folder = "test_folder"

while True:
    display_menu()

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        organize_files(folder)
        print("\nFiles organized successfully!")

    elif choice == "2":
        try:
            with open("organizer.log", "r") as file:
                print("\n------ LOG FILE ------")
                print(file.read())
        except FileNotFoundError:
            print("\nLog file not found.")

    elif choice == "3":
        print("\nThank you for using File Organizer!")
        break

    else:
        print("\nInvalid choice! Please enter 1, 2, or 3.")