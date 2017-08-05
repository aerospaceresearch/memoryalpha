from flask import Flask
import os
import uuid
from flask import Flask, request, redirect, flash, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "SpaceRocks1!" # for the cookie

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = uuid.uuid4().hex + "-" + secure_filename(file.filename)
            file.save(os.path.join('input', filename))
            flash('uploaded: ' + filename)
            return redirect('/')

    return render_template('index.html')

if __name__ == "__main__":
    # for us windows users only, perhaps.
    app.run(debug=True)