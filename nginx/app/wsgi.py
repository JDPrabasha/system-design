import flask
import socket

app = flask.Flask(__name__)


@app.route('/')
def home():
    return f'Hello from {socket.gethostname()}!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
