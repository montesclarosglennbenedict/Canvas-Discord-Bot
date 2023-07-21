# https://canvasapi.readthedocs.io/en/stable/
# https://canvasapi.readthedocs.io/en/stable/examples.html?highlight=courses#list-courses-under-an-account

# Import the Canvas class
from canvasapi import Canvas
import os

# Canvas API URL
API_URL = os.environ['URL']
# Canvas API key
API_KEY = os.environ['KEY']

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
  print(course)
except:
  pass

with open('nameses.txt', 'w') as file:
    for user in users:
      try:
        file.write(user.name + '\n')
      except:
        file.write('failed here')