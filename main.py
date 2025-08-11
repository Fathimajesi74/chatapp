import random
import json
import os

def load_data():
    data_path = os.path.join(os.path.dirname(__file__), 'data.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return data


def store_data(user_message, bot_message):
    data_path = os.path.join(os.path.dirname(__file__), 'data.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append({"user": user_message, "bot": bot_message})
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def main():
    loaded_data = load_data()

    while True:
        user_input= input("You:").lower().strip()
        user_array=user_input.split(" ")
        response = ""
        if 'hello' in user_array:
            response="Bot: Hi there!"
            print(response)
        elif 'name' in user_array:
            response="Bot: My name is ChatBot."
            print(response)
        elif 'dice' in user_array:
            response=f"Bot: You rolled a{ random.randint(1, 6)}"
            print(response)
        elif 'exit' in user_array or 'quit' in user_array:  
            response="Bot: Goodbye!"
            print(response)
            break
        store_data(user_input, response)
if __name__=="__main__":
    main()