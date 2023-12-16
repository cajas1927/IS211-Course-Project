# IS211-Course-Project
Final Project


# Book Catalogue Web Application

This web application allows users to keep track of the books they own. Users can log in and search for books using their ISBN. The application uses the Google Books API to retrieve information about the books and stores relevant details in a SQLite database. Users can view their list of saved books, delete books, and perform other actions.

## Features

- **Search by ISBN:** Users can search for books by entering the ISBN, triggering a search using the Google Books API.

- **View and Delete Books:** After logging in, users can view a list of their saved books, including details such as title, author, page count, average rating, and thumbnail. Users can also delete books from their list.

- **Extra Credit Features:**
  - **Multiple Users:** The application supports multiple users. Each user has their own list of books.
  - **Save Thumbnails:** The application saves and displays the URL of a thumbnail for each book.
  - **Handling Multiple Responses:** If the Google API provides multiple responses for a single ISBN, the application allows users to choose the desired book from the list.
  - **Search by Title:** Users can search for books by title using the Google API.

## How It Works

1. **Database Setup:** The application uses Flask-SQLAlchemy to create a SQLite database with tables for users and books.

2. **Google Books API:** When a user searches for a book by ISBN, the application sends a request to the Google Books API to retrieve information about the book.

3. **Data Storage:** The relevant information (title, author, page count, average rating, thumbnail URL) is stored in the database, linked to the user who added the book.

4. **Web Interface:** Users interact with the application through a web interface built with Flask and Jinja templating. They can view, add, and delete books.

## How to Run the Application

1. Clone the repository: `git clone https://github.com/cajas1927/IS211-Course-Project.git`

2. Install dependencies: pip install flask flask_sqlalchemy requests
3. Run the application: python app.py`

4. Open your web browser and navigate to http://localhost:5000

## Model Details

The application uses the Flask web framework with Flask-SQLAlchemy for database management. The user interface is rendered using HTML templates with Bootstrap for styling.



