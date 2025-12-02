from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    html = '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Home page</title>
        </head>
        <body>
            <h1 style= "text-align: center;">Welcome to the home page</h1>
            <p>You can go and read about us on our  <a href="https://super-duper-xylophone-g4v46vv99xqr3pp5p-5000.app.github.dev/about">About Page!</a></p>
        </body>
    </html>
    '''
    return html

@app.route("/about")
def about():
    html = '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>About</title>
        </head>
        <body>
            <h1>Welcome to the about page</h1>
            <p>This is the about page. To return to home <a href="https://super-duper-xylophone-g4v46vv99xqr3pp5p-5000.app.github.dev">click here!</a>Go to contacts <a href="https://super-duper-xylophone-g4v46vv99xqr3pp5p-5000.app.github.dev">here.</a></p>
        </body>
    </html>
    '''
    return html

@app.route("/contacts")

def contacts():
    html = '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Contacts</title>
        </head>
        <body>
            <h1>Welcome to the Contacts page.</h1>
            <p>This is the contacts page. To return to home <a href="https://super-duper-xylophone-g4v46vv99xqr3pp5p-5000.app.github.dev">click here!</a><br> To navigate to about us, <a href="https://super-duper-xylophone-g4v46vv99xqr3pp5p-5000.app.github.dev">click here!</a></p>
        </body>
    </html>
    '''
    return html


app.run(debug = True, reloader_type="stat", host="0.0.0.0", port=5000)