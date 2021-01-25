from flask import Flask
import secrets
import os

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
	port = os.getenv('PORT', 3000)
	#Start web serviced
	app.run(debug=False, host='0.0.0.0', port = port)