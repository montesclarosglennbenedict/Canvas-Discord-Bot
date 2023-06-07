# https://canvasapi.readthedocs.io/en/stable/

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
courses = user.get_courses(enrollment_state='active')

for course in courses:
  try:
    users = course.get_users()
    print(course.name)
  except:
    pass

for user in users:
  print(user.name)
  print(user.email)