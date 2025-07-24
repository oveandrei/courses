from logic import File, Folder, FolderManager, FileManager

# Instantiate the managers responsible for tracking all folders and files
folder_manager = FolderManager()
file_manager = FileManager()


def validate_response(message: str) -> str:
    """
    Ensure the user provides a valid menu option (1–6).
    Re-prompts the user until valid input is given.
    """
    while message not in [str(x) for x in range(1, 7)]:
        print("The number must be an available choice.")
        message = input("Write the number here: ")
    return message


def client():
    """Main CLI interface for interacting with the file hierarchy system."""
    print("Hey, this is your file hierarchy system!")

    while True:
        # Show menu options
        print("---------------------------------")
        print("What would you like to do now?")
        print("1. Create a Folder")
        print("2. Create a File")
        print("3. Get the size of a File")
        print("4. Get the size of a Folder")
        print("5. Display all Folders")
        print("6. Quit")
        print("-----------------------------------")

        # Get and validate user input
        response = validate_response(input("Write the number here: "))

        if response == '1':
            # Ask user whether to create a nested folder
            response = input("Create a Folder in an existing Folder? (y/n): ").lower()

            if response == 'y':
                # Show existing folders
                print(f"Available folders: {folder_manager.get_all_folders()}")
                target_name = input("Choose a Folder to nest into: ")

                try:
                    # Get the folder object where the new folder will be nested
                    target_folder = folder_manager.get_folder_object(target_name)
                    new_folder_name = input("Name of new Folder: ")
                except KeyError:
                    print("That wasn't a valid folder name.")
                    continue

                # Create and register the new nested folder
                sub_folder = folder_manager.create_and_register_folder(new_folder_name)
                if sub_folder is None:
                    print("A folder with that name already exists.")
                    continue

                # Add the new folder as a child to the target folder
                target_folder.add(sub_folder)
                print("Folder created and added successfully.")

            elif response == 'n':
                # Create a top-level folder
                new_folder_name = input("Name of new Folder: ")
                new_folder = folder_manager.create_and_register_folder(new_folder_name)
                if new_folder is None:
                    print("A folder with that name already exists.")
                    continue
                print("Folder created successfully.")
            else:
                print("Invalid choice.")

        elif response == '2':
            # Show folders where files can be placed
            print(f"Available folders: {folder_manager.get_all_folders()}")
            try:
                target_folder_name = input("Select Folder to create the File in: ")
                file_name = input("File name: ")
                file_size = int(input("File size (number only): "))

                # Create and register the file
                file_obj = file_manager.create_and_register_file(file_name, file_size)
                if file_obj is None:
                    print("A file with that name already exists.")
                    continue

                # Add file to the selected folder
                target_folder = folder_manager.get_folder_object(target_folder_name)
                target_folder.add(file_obj)
                print(f"File '{file_name}' added successfully.")

            except KeyError:
                print("Invalid folder selected.")
            except ValueError:
                print("Size must be a number.")

        elif response == '3':
            # Display size of a selected file
            print(f"Available Files: {file_manager.get_all_files()}")
            file_name = input("Choose a File: ")
            try:
                file_obj = file_manager.get_file_object(file_name)
                print(f"The file size is: {file_obj.get_size()}")
            except KeyError:
                print("File not found.")

        elif response == '4':
            # Display size of a selected folder
            print(f"Available Folders: {folder_manager.get_all_folders()}")
            folder_name = input("Choose a Folder: ")
            try:
                folder_obj = folder_manager.get_folder_object(folder_name)
                print(f"The folder size is: {folder_obj.get_size()}")
            except KeyError:
                print("Folder not found.")

        elif response == '5':
            # Display all top-level folders and their nested contents
            for folder in folder_manager.get_all_folders():
                folder_obj = folder_manager.get_folder_object(folder)
                # Only display top-level folders (not nested inside another folder)
                if not any(folder_obj in f._children for f in folder_manager.folders_dict.values()):
                    folder_obj.display()

        elif response == '6':
            print("Goodbye!")
            break


# Entry point of the application
if __name__ == "__main__":
    client()
