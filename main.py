from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    # for us windows users only, perhaps.
    app.run()