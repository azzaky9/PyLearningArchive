import os

current_dir = os.getcwd()
print(current_dir)

def create_file(file_name):
   return open(file_name, 'a')

# os.chdir('C:/Users/zakii/PycharmProjects/LearningResource/')

# contents = os.listdir('.')
# print(f"Directory contents: {contents}")

# create_file('outer.py')

# os.remove('outer.py')

# os.mkdir('test_changes')

# os.chdir('C:/Users/zakii/PycharmProjects/LearningResource/file')

# create_file('inner.txt')

# os.rename('inner.txt', 'test_folder/inner.txt')

# create_file('inner.py')
# os.mkdir('test_folder')

# os.makedirs('test_folder/test_children_folder')

# os.rename('my_file.txt', 'notes.txt')

# os.remove('notes.txt')
