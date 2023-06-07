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

# Get the course object
course = canvas.get_course(2803)

# Get the student object
student = course.get_user(94919)

print(student)

# Create a new conversation
conversation = canvas.create_conversation(
    recipients=[94919],
    subject="Group Project",
    body="Hello! This is a message about our group project."
)

# Send the conversation message
print(conversation)