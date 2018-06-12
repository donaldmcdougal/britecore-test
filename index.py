from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'test.html',name=name)

if __name__ == "__main__":
    app.run()
