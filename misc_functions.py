import pandas as pd

books_data = pd.read_csv(r'datasets/content_dataset.csv')
books_data.drop(books_data.columns[[0]], axis=1, inplace=True)


def get_book_details(book_isbn):
    book_index = list(books_data[books_data['ISBN']==book_isbn].index)[0]
    book_details = dict(books_data.loc[book_index])
    return book_details

def get_top_k_popular_books(k):
    books = pd.read_csv(r'datasets/original/books.csv', sep=';', encoding = "ISO-8859-1", error_bad_lines = False)
    ratings = pd.read_csv(r'datasets/original/ratings.csv', sep=';', encoding = "ISO-8859-1")
    df = pd.merge(ratings, books, on="ISBN" )
    df.dropna(inplace=True)
    book_rating_count = pd.DataFrame(df.groupby(by=['ISBN'])['Book-Rating'].count().reset_index())
    popular_books_ratings = book_rating_count.sort_values('Book-Rating', ascending=False).head(k)
    popular_books_isbn = list(popular_books_ratings['ISBN'])
    books_data = pd.read_csv(r'datasets/content_dataset.csv')
    books_data.drop(books_data.columns[[0]], axis=1, inplace=True)
    popular_books = books_data[books_data['ISBN'].isin(popular_books_isbn)].reset_index()
    popular_books.drop(columns=['index'], inplace=True)
    popular_books.rename(columns={'Book-Title': 'Book_Title',
                                  'Book-Author': 'Book_Author',
                                  'Year-Of-Publication': 'Year_Of_Publication',
                                  'Image-URL-S': 'Image_Small',
                                  'Image-URL-M': 'Image_Medium',
                                  'Image-URL-L': 'Image_Large',
                                  'ImportantFeatures': 'Important_Features'
                                 }, inplace=True)
    popular_books.to_csv(r'datasets/popular_books.csv')