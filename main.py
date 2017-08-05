from flask import Flask
import os
import uuid
from flask import Flask, request, redirect, flash, render_template, Response
from werkzeug.utils import secure_filename
from functools import wraps

app = Flask(__name__)
app.secret_key = "SpaceRocks1!" # for the cookie

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """

    # checking for users
    for uname, pword in (('admin1', 'secret1'),('admin2', 'secret2')):
        if uname == username and pword == password:
            return True

    return False


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/', methods=['GET', 'POST'])
@requires_auth
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