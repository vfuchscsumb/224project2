import os
import cvproject
from flask import Flask, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

images = []
def store_images(myImage):
    images.insert(0,myImage)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            store_images(filename)
            return redirect(url_for('nextPage'))
    return render_template("index.html")

@app.route('/next')
def nextPage():
    print images
    cvproject.faceDetection('static/uploads/' + images[0])
    return render_template("secondpage.html")
    
@app.route('/finalpage')
def showImage():
    return render_template("final.html")


if __name__ == '__main__':
    app.run(
        debug=True,
        port = int(os.getenv('PORT', 8080)),
        host = os.getenv('IP', '0.0.0.0')
    )