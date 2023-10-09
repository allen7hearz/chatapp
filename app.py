from flask import Flask, render_template, redirect, url_for, request
import json, os
app = Flask(__name__)

def load_users():
        with open('users.json', 'r') as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return {}

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/signup')

def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    # Load existing users from JSON file
    users = load_users()
    # Check if username already exists
    if username in users:
        return render_template('signup.html', error="Username already exists.")
    # Add new user to the dictionary
    users[username] = password
    # Save the updated users back to the JSON file
    save_users(users)
    return redirect(url_for('login', username=username))

@app.route('/login')
def login_page():
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Load existing users from JSON file
    users = load_users()
    # Check if username exists and if password matches
    if username in users and users[username] == password:
        return f"Welcome, {username}!"
    else:
        return render_template('login.html', error="Invalid username or password. Please try again.") 
       
if __name__ == '__main__':
    app.run(debug=True)