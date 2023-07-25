# https://canvasapi.readthedocs.io/en/stable/
# https://canvasapi.readthedocs.io/en/stable/examples.html?highlight=courses#list-courses-under-an-account

# Import the Canvas class
from canvasapi import Canvas
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
API_URL = os.getenv('URL')
API_KEY = os.getenv('KEY')

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)
user = canvas.get_user("self")

# active, future, completed
#courses = user.get_courses(enrollment_state='active')

#for course in courses:
#  try:
#    users = course.get_users()
#    print(course)
#  except:
#    pass
#
#for user in users:
#  print(user.name)

course = canvas.get_course(46281)

try:
  users = course.get_users()
  print(users)
except:
  pass


for user in users:
  print(user.name.split()[0])

'''
with open('nameses.txt', 'w') as file:
    for user in users:
      try:
        file.write(user.name + '\n')
      except:
        file.write('failed here')
        '''