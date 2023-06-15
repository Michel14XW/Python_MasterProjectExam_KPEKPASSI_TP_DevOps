from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get('name', '')
    firstname = request.args.get('firstname', '')
    return f"<h1 style='color:blue'>Hello {firstname} {name}!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
