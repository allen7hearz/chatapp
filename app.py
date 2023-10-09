from flask import Flask, render_template, redirect, url_for, request, jsonify
import json
import traceback
from chat import chat_functions
app = Flask(__name__)

messages = []

# Load messages from the messages.json file
def load_messages():
    try:
        with open('messages.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Write messages to the messages.json file
def save_messages(messages):
    with open('messages.json', 'w') as file:
        json.dump(messages, file)

# Route to render the chat page
@app.route('/chat')
def chat():
    messages = load_messages()
    return render_template('chat.html', messages=messages)

# Route to handle the AJAX request for sending a message
@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        message = request.json.get('message')
        if message:
            messages = load_messages()
            if 'data' not in messages:
                messages['data'] = []
            messages['data'].append(message)
            save_messages(messages)
            return '', 200
        return '', 400
    except Exception as e:
        traceback.print_exc()
        app.logger.error('Error sending message: {}'.format(e))
        return 'Error sending message', 500
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
        return redirect(url_for('chat', username=username, password=password))
    else:
        return render_template('login.html', error="Invalid username or password. Please try again.") 
       
if __name__ == '__main__':
    app.run(debug=True)