from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Chickens!</title>
        <link rel='stylesheet' type='text/css' href='/static/css/style.css'>
    </head>
    <body>
        <h1>Look at all those chickens!</h1>
        <p style=text-align:center><span id=first>Bok!</span> <span id=second>Bok!</span> <span id=third>Bok!</span></p>
        <img src='/static/images/chicken1.jpg' height='200'>
        <img src='/static/images/chicken2.jpg' height='200'>
        <img src='/static/images/chicken3.jpg' height='200'>
        <img src='/static/images/chicken4.jpg' height='200'>
        <img src='/static/images/chicken5.jpg' height='200'>
        <a href="https://super-duper-xylophone-g4v46vv99xqr3pp5p-5000.app.github.dev/facts"><br>Fun Fact about a chicken!</a>

    </body>
    </html>
    '''

@app.route('/facts')
def facts():
    return '''
    <html>
    <head>
        <title>Chickens!</title>
        <link rel='stylesheet' type='text/css' href='/static/css/style.css'>
    </head>
    <body>
        <h1>Chicken Facts</h1>
        <p>Chickens can recognize and remember over 100 different faces, both human and chicken. They also experience REM sleep, which means they dream like humans. The color of a hen’s earlobes often predicts her egg color: white earlobes usually mean white eggs, while red earlobes mean brown eggs. Chickens can run up to 9 miles per hour when motivated. They are highly social animals and maintain complex hierarchies within their flocks, often called the pecking order. Domestic chickens are descendants of the red junglefowl, native to Southeast Asia, and have been raised by humans for thousands of years.</p>
        <a href="https://super-duper-xylophone-g4v46vv99xqr3pp5p-5000.app.github.dev/">Back to Home</a>
    </body>
    </html>
    '''

app.run(debug=True, reloader_type='stat', port=5000)
