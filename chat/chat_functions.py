import json
path = 'C:/Users/allen/Documents/python_code/chatapp/chatapp/messages.json'
# Function to load messages from the JSON file
def load_messages():
    with open(path) as file:
        data = json.load(file)
        return data.get('messages', [])

# Function to add a new message to the JSON file
def add_message(message):
    with open(path, 'r+') as file:
        data = json.load(file)
        messages = data.get('messages', [])
        messages.append(message)
        data['messages'] = messages
        file.seek(0)
        json.dump(data, file)
        file.truncate()