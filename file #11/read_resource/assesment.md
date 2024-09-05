# Assessment: Python File Operations with os Module

## Objective

This assessment aims to evaluate your understanding of file operations using Python's `os` module. You'll be asked to create a script that performs various file and directory operations based on user input.

## Instructions

Create a Python script that does the following:

1. Create a new directory called "assessment_files" in the current working directory.

2. Inside "assessment_files", create three text files: "file1.txt", "file2.txt", and "file3.txt". Write the current date and time to each file.

3. Create a function that lists all files in a given directory and returns them as a list.

4. Create a function that reads the content of a given file and returns it as a string.

5. Create a function that renames a file, given its current name and new name.

6. Create a function that moves a file from one directory to another.

7. Create a menu-driven interface that allows the user to perform the following operations:
   a. List all files in the "assessment_files" directory
   b. Read the content of a specific file
   c. Rename a file
   d. Move a file to a new directory
   e. Delete a file
   f. Exit the program

8. Implement error handling for all operations (e.g., file not found, permission denied, etc.).

## Example Code Structure

```python
import os
from datetime import datetime

def create_initial_files():
    # Your code here

def list_files(directory):
    # Your code here

def read_file(filename):
    # Your code here

def rename_file(old_name, new_name):
    # Your code here

def move_file(filename, new_directory):
    # Your code here

def delete_file(filename):
    # Your code here

def main_menu():
    while True:
        print("\n--- File Operations Menu ---")
        print("1. List all files")
        print("2. Read a file")
        print("3. Rename a file")
        print("4. Move a file")
        print("5. Delete a file")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        # Implement menu options here

if __name__ == "__main__":
    create_initial_files()
    main_menu()
```

## Evaluation Criteria

Your script will be evaluated based on the following criteria:

1. Correct implementation of all required functions
2. Proper use of the `os` module for file operations
3. Effective error handling and user input validation
4. Clear and readable code structure
5. Correct handling of file paths across different operating systems

## Bonus Challenges

For additional practice, try implementing these bonus features:

1. Add a function to calculate and display the total size of all files in the directory.
2. Implement a simple file search function that finds files containing a user-specified string.
3. Add a function to create a backup of a file before modifying or deleting it.

## Submission

Submit your completed Python script along with a brief explanation of how you approached the problem and any challenges you faced.

Good luck!
