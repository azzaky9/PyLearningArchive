from datetime import datetime
import pymysql
import os


connection = pymysql.connect(
  host='localhost',
  user='root',
  password='root',
  database='py_study_case'
)

cursor = connection.cursor()


def main():

  now = datetime.now()

  username = input("Input your username: ")
  password = input("Input your password: ")
  # age = int(input("Input your age: "))
  created_at = now
  updated_at = now

  sql = """
    INSERT INTO user (username, password, created_at, updated_at)
    VALUES (%s, %s, %s, %s)
  """
  values = (username, password, created_at, updated_at)

  cursor.execute(sql, values)

  connection.commit()

  cursor.close()
  connection.close()

  print(f"Create new user with {username} at {created_at}")

main()
