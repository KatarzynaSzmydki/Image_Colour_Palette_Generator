'A website that finds the most common colours in an uploaded image.'


from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import UploadForm
import os
from werkzeug.utils import secure_filename
from os.path import exists
from colorthief import ColorThief


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


@app.route('/', methods=['POST','GET'])
def home():
    form = UploadForm()
    img_path ='static/img/img_start.jpg'

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        if exists('static/img/' + filename):
            os.remove('static/img/' + filename)
        form.file.data.save('static/img/' + filename)

        img_path = 'static/img/' + filename

    color_thief = ColorThief(img_path)
    dominant_color = color_thief.get_color(quality=1)
    palette = color_thief.get_palette(color_count=5)
    palette = [rgb_to_hex(rgb) for rgb in palette]


    # return render_template("index.html", form=form, file_path=img_path, file_example=False)

    return render_template("index.html",
                           form=form,
                           file_path=img_path,
                           file_example=True,
                           palette=palette)


@app.route('/history')
def history():
    return render_template("history.html")



if __name__ == "__main__":
    app.run(debug=True)




