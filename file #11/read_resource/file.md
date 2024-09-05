# Python File Operations with os Module: A Practical Guide

## 1. Introduction to the os Module

The `os` module in Python provides a way to interact with the operating system. We'll focus on file and directory operations.

```python
import os
```

## 2. Working with Directories

### 2.1 Getting the Current Working Directory

```python
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")
```

### 2.2 Changing the Current Directory

```python
os.chdir('/path/to/new/directory')
```

### 2.3 Creating a New Directory

```python
os.mkdir('new_directory')
```

### 2.4 Creating Nested Directories

```python
os.makedirs('parent/child/grandchild')
```

### 2.5 Listing Directory Contents

```python
contents = os.listdir('.')
print(f"Directory contents: {contents}")
```

## 3. File Operations

### 3.1 Checking if a File Exists

```python
file_exists = os.path.exists('example.txt')
print(f"File exists: {file_exists}")
```

### 3.2 Getting File Information

```python
file_size = os.path.getsize('example.txt')
print(f"File size: {file_size} bytes")

file_mtime = os.path.getmtime('example.txt')
print(f"Last modified time: {file_mtime}")
```

### 3.3 Renaming a File

```python
os.rename('old_name.txt', 'new_name.txt')
```

### 3.4 Moving a File

```python
os.rename('file.txt', 'new_directory/file.txt')
```

### 3.5 Deleting a File

```python
os.remove('file_to_delete.txt')
```

## 4. Path Operations

### 4.1 Joining Paths

```python
full_path = os.path.join('directory', 'subdirectory', 'file.txt')
print(f"Full path: {full_path}")
```

### 4.2 Getting the Absolute Path

```python
abs_path = os.path.abspath('relative/path/file.txt')
print(f"Absolute path: {abs_path}")
```

### 4.3 Splitting a Path

```python
directory, filename = os.path.split('/path/to/file.txt')
print(f"Directory: {directory}")
print(f"Filename: {filename}")
```

## 5. Practical Examples

### 5.1 Recursively List All Files in a Directory

```python
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{sub_indent}{f}")

list_files('.')
```

### 5.2 Find and Delete All Files with a Specific Extension

```python
def delete_files_by_extension(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

delete_files_by_extension('.', '.tmp')
```

## 6. Error Handling

Always use try-except blocks when working with file operations to handle potential errors gracefully.

```python
try:
    os.remove('non_existent_file.txt')
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
```

## Conclusion

This guide covers the essential file operations using Python's `os` module. Practice these operations in a safe environment to gain hands-on experience. Remember to handle errors appropriately in your code to make it more robust.
