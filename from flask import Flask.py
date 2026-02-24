from flask import Flask
app = Flask(__name__)

@app.root("/")
def hello():
    return "Hello Jenkins! My Flask app is running in Docker!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)