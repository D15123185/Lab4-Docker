from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return 'Index Page'

@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/user/<username>")
def userpaul(username):
	return 'User %s' % username

@app.route("/post/<port>")
def post80(port):
	return 'Post %s' % port


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)

