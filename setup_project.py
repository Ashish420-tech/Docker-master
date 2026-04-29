import os

def create_folder(path):
    if os.path.exists(path):
        print(f"⚠️ Folder '{path}' already exists")
    else:
        os.makedirs(path)
        print(f"✅ Folder '{path}' created")


def create_file(path):
    if os.path.exists(path):
        print(f"⚠️ File '{path}' already exists")
    else:
        with open(path, 'w') as f:
            pass
        print(f"✅ File '{path}' created")


def main():
    print("🚀 Python Project Setup Tool")

    project_name = input("Enter project/repo name: ").strip()

    if os.path.exists(project_name):
        print(f"⚠️ Project '{project_name}' already exists")
    else:
        os.makedirs(project_name)
        print(f"✅ Created project: {project_name}")

    os.chdir(project_name)

    while True:
        choice = input("\nCreate a folder? (yes/no): ").strip().lower()

        if choice == "yes":
            folder_name = input("Enter folder name: ").strip()

            create_folder(folder_name)

            while True:
                file_choice = input(f"Create file inside '{folder_name}'? (yes/no): ").strip().lower()

                if file_choice == "yes":
                    file_name = input("Enter file name (with extension): ").strip()
                    file_path = os.path.join(folder_name, file_name)
                    create_file(file_path)

                elif file_choice == "no":
                    break
                else:
                    print("❌ Please enter yes or no")

        elif choice == "no":
            print("👋 Exiting setup...")
            break
        else:
            print("❌ Please enter yes or no")

    print("🎯 Project setup completed!")


if __name__ == "__main__":
    main()
