from flask import *
import pre_processing as pp
import recommendation_functions as rf
import misc_functions as mf

app = Flask(__name__)


knn_table, pearson_table = pp.collaborative_preprocess()
content_based_matrix = pp.content_based_preprocess()
popular_books = pp.get_popular_books()
all_books = pp.get_all_books()

recommended_books = []
book_details = {}


@app.route('/')
def home():
    return render_template('home.html', popular_books_len=len(popular_books), popular_books=popular_books)


@app.route('/all_books')
def allBooks():
    return render_template('all_books.html', all_books_len=len(all_books), all_books=all_books)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/book/<string:book_isbn>')
def book(book_isbn):
    return render_template('book.html', book_details=book_details, recommended_books_len=len(recommended_books), recommended_books=recommended_books)


@app.route('/recommend')
def compute_recommendation():
    global book_details
    global recommended_books
    book_isbn = request.args.get('book_isbn')
    book_details = mf.get_book_details(book_isbn)
    recommended_books = rf.get_recommendations(book_isbn, knn_table, pearson_table, content_based_matrix)
    return 'Nothing'


if __name__ == '__main__':
    app.run(debug=True)