import flask
app = flask.Flask(__name__)

def index():
    return flask.render_template('index.html')
    
    
    
if __name__ == "__main__":
    app.run(host="127.0.0.1": port=5000, debug=True)