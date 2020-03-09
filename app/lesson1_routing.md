# Routing
## What is routing?
It's time to route some things. Routing is what your computer asks for. Say you go to ```mywebsite.com```. That makes the server of ```mywebsite.com``` look for / in it's routing.
## How do I make one?
In order to make a route in Flask you first need to open your ```routes.py``` and type this:
```python
from app import app
@app.route('/')
def home():
  return 'Hello World'
```
So, here's what this code does.
1. It imports the app
2. It tells Flask where this route is going
3. It defines the function 
4. It returns 'Hello World!' to the browser
