from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample Python logic
def get_random_quote():
    quotes = [
        "Believe in yourself.",
        "Stay curious.",
        "Never give up.",
        "Code every day.",
        "Dream big, build bigger."
    ]
    return random.choice(quotes)

@app.route('/')
def index():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
