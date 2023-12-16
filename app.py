from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    books = db.relationship('Book', backref='user', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    page_count = db.Column(db.Integer)
    average_rating = db.Column(db.Float)
    thumbnail_url = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create tables within the application context
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    books = Book.query.filter_by(user_id=1).all()
    return render_template('index.html', books=books)

@app.route('/search', methods=['POST'])
def search():
    isbn = request.form['isbn']
    google_books_api_url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'

    try:
        response = requests.get(google_books_api_url)
        data = json.loads(response.text)

        book_info = data['items'][0]['volumeInfo']
        title = book_info['title']
        author = book_info['authors'][0]
        page_count = book_info.get('pageCount', None)
        average_rating = book_info.get('averageRating', None)
        thumbnail_url = book_info['imageLinks']['thumbnail'] if 'imageLinks' in book_info else None

        new_book = Book(title=title, author=author, page_count=page_count,
                        average_rating=average_rating, thumbnail_url=thumbnail_url, user_id=1)
        db.session.add(new_book)
        db.session.commit()

        flash('Book added successfully', 'success')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')

    return redirect(url_for('index'))

@app.route('/delete/<int:book_id>')
def delete(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
