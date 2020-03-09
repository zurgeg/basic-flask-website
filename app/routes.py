# This is where all of the routing goes. We need to import our app from __init__.py but since
# __init__.py is where all the stuff from the modules goes we just need to import app.app
from app import app
# Another alternative is
# from . import app
# because . is the current module. Now let's do some routing
@app.route('/')
def home():
  return 'Hello World!'
  
# Now let's start our server by runnning these commands:
# On Windows and Mac:
# Download the .zip of this repo
# Unzip it
# Open Command Prompt/Terminal
# Go into the folder using cd
# Lastly run ./run.sh (Mac) or run.bat (Windows)
# On Mac (in Terminal):
# Create directory server
# git clone https://github.com/zurgeg/basic-flask-website.git
# git checkout master
# ./run.sh
