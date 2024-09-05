import os

# open('my_file.txt', 'a')

# file = open('my_file.txt', 'r') # read file
# writeable_file = open('my_file.txt', 'w') # write file

# try:
#   open('my_file.txt', 'x')
# except FileExistsError:
#   print('File already exists')

# write_read_file = open('my_file.txt', '')

# for i in range(20):
#   write_read_file.write(f'Hello, this is line {i}\n')


# print(write_read_file.read())

# file = open('example.txt', 'a')

# file.write('Hello, this is a new line\n')

# for i in range(50):
#   writeable_file.write(f'Hello, this is line {i}\n')




current_dir = os.getcwd() # path

# for i in range(10):
#   os.mkdir(f'folder{i + 1}')

# def make_dir_and_file(path, file_name):
#   # os.mkdir(path)s
#   os.chdir(f'{current_dir}/{path}')
#   open(file_name, 'a')
#   # file.write(f'Hello, this text i
nside {file_name}\n')

# for i in range(10):
#   make_dir_and_file(f'folder{i + 1}', f'file_{i + 1}.txt')

# print(f'current directory: {current_dir}')

for i in range(10):
  try:
    os.chdir(f'folder{i + 1}')
    os.remove(f'file_{i + 1}.txt')
    os.chdir(current_dir)
    os.rmdir(f'folder{i + 1}')
  except FileNotFoundError:
    print('File not exists')

# C:\Users\zakii\PycharmProjects\LearningResource\file\folder2
