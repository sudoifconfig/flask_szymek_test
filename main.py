from flask import Flask, render_template
import os 

PHOTOS_FOLDER = os.path.join('static', 'photos')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PHOTOS_FOLDER

# Testowa strona Hello World
@app.route('/')
def hello_world():
    return 'Hello, World!'

#Stronka z Fotką 
@app.route('/fotka')
def print_fotka():
    image = os.path.join(app.config['UPLOAD_FOLDER'], 'aware_big_logo.png')
    return render_template("index.html", user_image = image)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)