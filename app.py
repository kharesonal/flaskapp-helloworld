#Import the Flask class from the Flask library.
from flask import Flask

#Create the App
app = Flask(__name__)

#@app.route('/') sets up the home route ("/") for our app. When someone visits this route, the hello function will run.
@app.route('/')
def hello():
    return "Hello World"

# About route
@app.route('/about')
def about():
    return 'This is the About page.'

# Contact route
@app.route('/contact')
def contact():
    return 'Contact us at contact@example.com.'

#In Python, every file (or module) has a built-in variable called __name__.
#When you run a Python file directly (for example, by executing python app.py), Python sets __name__ to '__main__'
#Python to only execute the code inside this if block if the file is being run directly.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


            
