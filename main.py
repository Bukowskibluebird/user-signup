from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Signup</h1>
    <form method='POST'>
        <label>Username
            <input name="username" type="text" value='{username}'/>
        </label>
        <p class="error">{username_error}</p>

        <label>Password
            <input name="password" type="password" value='{password}'/>
        </label>
        <p class="error">{password_error}</p>

        <label>Verify Password
            <input name="verify_password" type="password" value='{verify_password}'/>
        </label>
        <p class="error">{verify_password_error}</p>


        <input type="submit" />
    </form>
    """

@app.route('/')
def display_form():
    return form.format(username='', username_error='', password='', password_error='', verify_password='', verify_password_error='')

def validate_username(user):
    if user == "":
        return False
    if " " in user:
        return False
    elif len(user) > 20:
        return False
    elif len(user) < 3:
        return False
    else:
        return True

def validate_password(pword):
    if pword == "":
        return False
    if " " in pword:
        return False
    elif len(pword) > 20:
        return False
    elif len(pword) < 3:
        return False
    else:
        return True

def verify_password(pword, verify_pword):
    if pword != verify_pword:
        return False
    else:
        return True

@app.route('/', methods=['POST'])
def validate():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']

    username_error = ''
    password_error = ''
    verify_password_error = ''

    if not validate_username(username):
        username_error = "Not a valid username"
        username = ''

    if not validate_password(password):
        password_error = "Not a valid password"

    if not verify_password(password, verify_password):
        verify_password_error = "Password and password-confirmation do not match"
        password = ''
        verify_password = ''


    if not username_error and not password_error and not verify_password_error:
        return "Success, ya dink!"
    else:
       return form.format(username_error=username_error, password_error=password_error, verify_password_error=verify_password_error,
       username=username, password=password, verify_password=verify_password)


app.run()