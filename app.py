from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv()

from nlp import *
from flask_cors import CORS  # CORSをインポート
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "hello!"

@app.route('/similarwords', methods=["POST"])  # URLパラメータを削除
def _get_similar_words():
    data = request.get_json()  # リクエストボディからJSONデータを取得
    word = data.get('word')  # 'text'キーでテキストデータを取得
    if not word:
        return jsonify({"error": "No text provided"}), 400
    return jsonify({"results": get_similar_words(word)})

@app.route('/toninja', methods=["POST"])  # URLパラメータを削除
def _convert_to_ninja():
    data = request.get_json()  # リクエストボディからJSONデータを取得
    text = data.get('text')  # 'text'キーでテキストデータを取得
    if not text:
        return jsonify({"error": "No text provided"}), 400
    return jsonify({"content": convert_to_ninja(text)})

if __name__ == "__main__":
    app.run()
