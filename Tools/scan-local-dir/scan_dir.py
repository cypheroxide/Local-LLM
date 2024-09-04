import os
from pathlib import Path

def scan_directory(directory_path):
    """
    Scans the given directory recursively and returns a list of all files found.

    :param directory_path: The path to the directory to scan (can be local or network).
    :return: A list of full paths to files found in the directory.
    """
    files_list = []

    # Convert the directory path to a Path object
    dir_path = Path(directory_path)

    # Check if the path exists and is a directory
    if not dir_path.exists():
        return f"Error: The directory '{directory_path}' does not exist."
    
    if not dir_path.is_dir():
        return f"Error: '{directory_path}' is not a directory."

    # Traverse the directory and gather all files
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # Full file path
            full_path = os.path.join(root, file)
            files_list.append(full_path)

    return files_list

# Example Usage
if __name__ == "__main__":
    # Example directory path (could be local or network mounted)
    user_directory = input("Enter the directory path to scan: ")

    # Scan the directory
    result = scan_directory(user_directory)

    if isinstance(result, str):
        # If an error occurred, print it
        print(result)
    else:
        # Print out the list of files found
        print(f"Found {len(result)} files:")
        for file in result:
            print(file)

