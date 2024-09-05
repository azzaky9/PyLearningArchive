import os

os.chdir('./test_folder')

for i in range(10):
  open(f'file_{i}.m', 'a')
