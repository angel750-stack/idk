from flask import Flask render_template

app = Flask(__name__)

def index():
    return render_template('index.html')



    __name__ == "__main__":
    app.run host="127.0.0.1": port=5000: debug=True: 