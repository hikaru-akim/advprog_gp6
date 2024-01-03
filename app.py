from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Sample data (replace with a database in a production environment)
users = {}
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "price": 20.0},
    {"id": 2, "title": "Book 2", "author": "Author 2", "price": 25.0},
    {"id": 3, "title": "Book 3", "author": "Author 3", "price": 30.0},
]

# Routes

@app.route('/')
def index():
    search_query = request.args.get('q', '')
    filtered_books = filter_books(books, search_query)
    return render_template('index.html', books=filtered_books, search_query=search_query)

def filter_books(all_books, search_query):
    """Filter books based on the search query."""
    if search_query:
        return [book for book in all_books if search_query.lower() in book['title'].lower() or search_query.lower() in book['author'].lower()]
    else:
        return all_books