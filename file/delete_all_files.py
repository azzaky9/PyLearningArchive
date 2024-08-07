import os

def delete_files_recursive(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f'Deleted: {file_path}')

delete_files_recursive('.', '.txt')
