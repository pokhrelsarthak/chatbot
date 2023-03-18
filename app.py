from flask import Flask, jsonify, request
import Chat as cht

app = Flask(__name__)

# Create a simple API endpoint
@app.route('/')
def chat():
    cht.chat()
    return 'Hello, world!'



if __name__ == '__main__':
    app.run(debug=True)
