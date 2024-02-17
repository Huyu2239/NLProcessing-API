from flask import Flask

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello!"


@app.route('/toninja/<message>')
def convert_to_ninja(message):
    return message + "でござる。"


if __name__ == "__main__":
    app.run()
