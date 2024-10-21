import os
import shutil

# Extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"]
video_extensions = [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv"]
audio_extensions = [".mp3", ".wav", ".aac", ".flac", ".ogg"]
document_extensions = [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"]
compressed_extensions = [".zip", ".rar", ".tar", ".gz"]

print("---> Rohit Pratap Singh <---")
print("---> File Organizer <---")


def copyFiles():
    while True:
        target = input("Enter Target Path (where files will be copied): ")

        if os.path.exists(target):
            print(f"Target path is valid: {target}")
            break
        else:
            print("Enter a valid path.")    

    os.chdir(target)

    Folders = ["Image", "Video", "Documents", "Audio", "Compressed", "Unknown"]
    for Folder in Folders:
        if not os.path.exists(Folder):
            os.mkdir(Folder)

    count = 0

    while True:
        source = input("Enter Source Path (where files will be copied from): ")

        if os.path.exists(source):
            print(f"Source path is valid: {source}")
            break
        else:
            print("Enter a valid path.")          

    for file in os.listdir(source):
        file_path = os.path.join(source, file)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1]
      
            try:
                if file_extension in image_extensions:
                    shutil.copy(file_path, os.path.join(target, "Image")) 
                    print(f"Successfully copied {file} to Image directory.")
                    count += 1
                
                elif file_extension in video_extensions:
                    shutil.copy(file_path, os.path.join(target, "Video")) 
                    print(f"Successfully copied {file} to Video directory.")
                    count += 1
                
                elif file_extension in audio_extensions:
                    shutil.copy(file_path, os.path.join(target, "Audio"))
                    print(f"Successfully copied {file} to Audio directory.")
                    count += 1
                
                elif file_extension in document_extensions:
                    shutil.copy(file_path, os.path.join(target, "Documents"))
                    print(f"Successfully copied {file} to Documents directory.")
                    count += 1

                elif file_extension in compressed_extensions:
                    shutil.copy(file_path, os.path.join(target, "Compressed")) 
                    print(f"Successfully copied {file} to Compressed directory.")
                    count += 1                
                
                else:
                    shutil.copy(file_path, os.path.join(target, "Unknown"))
                    print(f"Successfully copied {file} to Unknown directory.")
                    count += 1
        
            except Exception as e:
                print(f"\033[91mFailed to copy {file}. Reason: {e}\033[0m")

    print(f"{count} : Files copied successfully")
    input("Press Enter to exit...")


def moveFiles():
    while True:
        target = input("Enter Target Path (where files will be moved): ")

        if os.path.exists(target):
            print(f"Target path is valid: {target}")
            break
        else:
            print("Enter a valid path.")    

    os.chdir(target)

    Folders = ["Image", "Video", "Documents", "Audio", "Compressed", "Unknown"]
    for Folder in Folders:
        if not os.path.exists(Folder):
            os.mkdir(Folder)

    count = 0

    while True:
        source = input("Enter Source Path (where files will be moved from): ")

        if os.path.exists(source):
            print(f"Source path is valid: {source}")
            break
        else:
            print("Enter a valid path.")          

    for file in os.listdir(source):
        file_path = os.path.join(source, file)

        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file)
      
            try:
                if file_extension in image_extensions:
                    shutil.move(file_path, os.path.join(target, "Image")) 
                    print(f"Successfully moved {file} to Image directory.")
                    count += 1
                
                elif file_extension in video_extensions:
                    shutil.move(file_path, os.path.join(target, "Video")) 
                    print(f"Successfully moved {file} to Video directory.")
                    count += 1
                
                elif file_extension in audio_extensions:
                    shutil.move(file_path, os.path.join(target, "Audio"))
                    print(f"Successfully moved {file} to Audio directory.")
                    count += 1
                
                elif file_extension in document_extensions:
                    shutil.move(file_path, os.path.join(target, "Documents"))
                    print(f"Successfully moved {file} to Documents directory.")
                    count += 1

                elif file_extension in compressed_extensions:
                    shutil.move(file_path, os.path.join(target, "Compressed")) 
                    print(f"Successfully moved {file} to Compressed directory.")
                    count += 1                
                
                else:
                    shutil.move(file_path, os.path.join(target, "Unknown"))
                    print(f"Successfully moved {file} to Unknown directory.")
                    count += 1
        
            except Exception as e:
                print(f"\033[91mFailed to move {file}. Reason: {e}\033[0m")

    print(f"{count} : Files moved successfully")
    input("Press Enter to exit...")    


def main():
    print("1. Copy")
    print("2. Move")
    print("3. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                copyFiles()
            elif choice == 2:
                moveFiles()
            elif choice == 3:
                exit()
            else:
                print("Invalid Choice")
        except ValueError:
            print("Please enter a valid number.")


main()
