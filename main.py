import os

# Define the directory to organize
download_directory = "C:/Users/bennyshi/Downloads"

# Function to organize downloaded files
def organize_downloads():
    for filename in os.listdir(download_directory):
        if os.path.isfile(os.path.join(download_directory, filename)):
            # Extract the file extension
            _, file_extension = os.path.splitext(filename)
            # Define the destination directory based on file extension
            destination_directory = os.path.join(download_directory, file_extension[1:].upper() + "s")
            # Check if the destination directory exists, if not, create it
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            # Move the file to the destination directory
            os.rename(
                os.path.join(download_directory, filename),
                os.path.join(destination_directory, filename)
            )
            print(f"Moved {filename} to {destination_directory}")

if __name__ == "__main__":
    organize_downloads()
