from flask import Flask
import secrets

app = Flask(__name__)

@app.route('/')
def hello_world():
	return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
	#Read app.config file
	app.config.update(dict(
		SECRET_KEY=secrets.token_urlsafe(64),
		WTF_CSRF_SECRET_KEY=secrets.token_urlsafe(64)
	))

	#Start web service
	app.run(debug=False, host='webapp', port = 80)