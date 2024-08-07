import os

# Goals

# - Accept input from terminal input()
# - Create new file notes.txt
# - Write message from input terminal to notes.txt

def main():
   message = input("Please write some message: ")

   file = open('notes.txt', 'a')

   with open('notes.txt', 'w') as file:
      file.write(message)

main()
