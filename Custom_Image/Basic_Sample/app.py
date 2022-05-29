import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "My First Image"

@app.route('/container')
def hello():
    return 'container working successfully' 


if __name__ == "__main__":
    app.run()