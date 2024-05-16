from flask import Flask, jsonify
# get books data

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "CS50",
        "description": "Intro to CS and art of programming!",
        "author": "Havard",
        "borrowed": False
    },
    {
        "id": 2,
        "title": "Python 101",
        "description": "little python code book.",
        "author": "Will",
        "borrowed": False
    }
]

@app.route("/bookapi/books")
def get_books():
    """ function to get all books """
    return jsonify({"Books": books})