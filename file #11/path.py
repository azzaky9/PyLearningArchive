import os

os.chdir('C:/Users/zakii/PycharmProjects/LearningResource/')

full_path = os.path.join('file', 'test_folder', 'inner.txt')
print(f'Full path: {full_path}')

os.remove(full_path)
