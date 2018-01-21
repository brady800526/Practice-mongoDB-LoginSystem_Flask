## Summary

This repo is a practice of using Session in Python Flask Framework to build a one user Login System.

*All the step is followed by [youtube channel](https://www.youtube.com/watch?v=eBwhBrNbrNI&list=PLXmMXHVSvS-CMpHUeyIeqzs3kl-tIG-8R&index=3) and [github](https://github.com/PrettyPrinted/flask-sessions) created by Pretty Printed.*

## Session

Session is a server-side dictionary stored key-value pair, in this case, we user session to store username. Once the username is not empty, we allow user to login our protected.html page.

## Usage

Download the repo, under the directory run:

    python session.py

You will see the landing page.

<figure style="text-align: center;">
    <img src="http://i66.tinypic.com/15s62v7.png" alt="Landing Page" style="width: 60%; height: 60%"/>
    <figcaption style="display: block;">Landing Page</figcaption>
</figure>

By entering name "Brady" and password "password", then press the Send button. User will be send to the protected page.

<figure style="text-align: center;">
    <img src="http://i66.tinypic.com/hrhbwl.png" alt="Landing Page" style="width: 60%; height: 60%"/>
    <figcaption style="display: block;">Protected Page</figcaption>
</figure>

As we enter the protected page meaning you successfully pass the Login System.

## Architecture

All the logic are placed in the session.py, so we will majorly discuss the session.py.

In the landing page (index.html), we send the username and password. Since we assume there is only one user(possibily because we don't have database), we only check if the password is equal to 'password'. If yes, we save the username to session, otherwise we will get back to landing page.

<figure style="text-align: center;">
    <img src="http://i65.tinypic.com/mayt0l.jpg" alt="The architecture of this app" style="width: 80%; height: 80%"/>
    <figcaption style="display: block;">The architecture of this app</figcaption>
</figure>

## Code

#### Setting
------------------------------------------------------------------------

session.py

```
app = Flask(__name__)
app.secret_key = os.urandom(24)
```

First we start an app initialized by Flask Framework `app = Flask(__name__)`

When you use session, you need to specify a secret_key for [encoded the value](https://www.youtube.com/watch?v=mhcnBTDLxCI﻿).

#### index route - Show the Landing Page
------------------------------------------------------------------------

session.py - GET
```
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ...
        ...
        ...
    else:
        return render_template("index.html")
```

If it is GET request, this route will enter the else condition and send the index.html template back to user.

The index.html will show a simple form for user to log in.

session.py - POST
```
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":

        if request.form['password'] == 'password':
            # This password should map to each user's password, not only general 'password' password

            session['user'] = request.form['username'] 
            # Should save Id to prevent replicate user
            return redirect(url_for('protected'))
```

After fill the form and submit, we will send back to the index route again. By examing the password is "password", we will save the username to session['user'].

#### before_request - Examine before every request
------------------------------------------------------------------------

session.py
```
@app.before_request
def before_request():
    if 'user' in session:
        g.user = session['user']
```

In the same time, we also user flask.g class to save the username in the session. Actually it's not a neccessary move since we can conctroll access only by session. Anyway, we save the username to the g.user.


#### protected route - Process the comment and save to db
------------------------------------------------------------------------

session.py
```
@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html')
    else:
        return redirect(url_for('index'))
```

if g.user exists, we send user to protected page, otherwise we send the user to landing page.

## Conclusion

In this project, we use session to save user value and save the username to g.user. Once the g.user has username value, it will allowed user to login to protected page.

Followed on, we should use database to save user data, and validate the user by data saved in database.
