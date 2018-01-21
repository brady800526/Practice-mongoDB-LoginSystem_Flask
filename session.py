from flask import Flask, session, render_template, request, url_for, g, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":

		if request.form['password'] == 'password':
			# This password should map to each user's password, not only general 'password' password

			session['user'] = request.form['username'] # Should save Id to prevent replicate user
			return redirect(url_for('protected'))

	return render_template("index.html")

@app.before_request
def before_request():
	if 'user' in session:
		g.user = session['user']

@app.route('/protected')
def protected():
	if g.user:
		return render_template('protected.html')
	else:
		return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(debug=True)
