from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!, Iza Ganteng</h1>"
    return "<h1>Hello, World!, muhammad Dava Rahmadhana</h1>"
     return "<h1>Hello, World!, Daffa Irfantoro</h1>"

if __name__ == "__main__":
    app.run(debug=True)
