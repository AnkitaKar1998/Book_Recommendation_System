import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

books_data = pd.read_csv(r'datasets/content_dataset.csv')
books_data.drop(books_data.columns[[0]], axis=1, inplace=True)

def get_recommendations(book_isbn, knn_table, pearson_table, content_based_matrix):
    content_based_result = get_content_based_result(book_isbn, content_based_matrix)
    collaborative_result = get_collaborative_result(book_isbn, knn_table, pearson_table)
    if(len(collaborative_result) == 0):
        final_result = [x for x in content_based_result]
    elif(len(content_based_result) == 0):
        final_result = [x for x in collaborative_result]
    else:
        collaborative_isbn = set(d['ISBN'] for d in collaborative_result)
        final_result = [d for d in content_based_result if d["ISBN"] in collaborative_isbn]
        if(len(final_result) == 0):
            final_result = [x for x in collaborative_result]
    return final_result



def get_content_based_result(book_isbn, content_based_matrix):
    book_index = books_data[books_data['ISBN']==book_isbn].index[0]
    scores = list(enumerate(content_based_matrix[book_index]))
    sorted_scores = sorted(scores, key = lambda x:x[1], reverse=True)
    sorted_scores = sorted_scores[1:11]
    content_based_result = []
    for i in sorted_scores:
        book_details = dict(books_data.loc[i[0]])
        content_based_result.append(book_details)
    return content_based_result



def get_collaborative_result(book_isbn, knn_table, pearson_table):
    knn_result = get_knn_result(book_isbn, knn_table)
    pearson_result = get_pearson_result(book_isbn, pearson_table)
    if(len(knn_result) == 0):
        collaborative_result = [x for x in pearson_result]
    elif(len(pearson_result) == 0):
        collaborative_result = [x for x in knn_result]
    else:
        knn_isbn = set(d['ISBN'] for d in knn_result)
        collaborative_result = [d for d in pearson_result if d["ISBN"] in knn_isbn]
        if(len(collaborative_result) == 0):
            collaborative_result = [x for x in knn_result]
    return collaborative_result



def get_knn_result(book_isbn, knn_table):
    matrix = csr_matrix(knn_table.values)
    knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
    knn_model.fit(matrix)
    distance,indices=knn_model.kneighbors(knn_table.loc[book_isbn,:].values.reshape(1,-1),n_neighbors=11)
    knn_result = []
    indices = indices.flatten()
    for i in range(1,len(indices)):
        isbn = knn_table.index[indices[i]]
        book_index = list(books_data[books_data['ISBN']==isbn].index)[0]
        book_details = dict(books_data.loc[book_index])
        knn_result.append(book_details)
    return knn_result



def get_pearson_result(book_isbn, pearson_table):
    book = pearson_table[book_isbn]
    similar = pearson_table.corrwith(book)
    similar_books = pd.DataFrame(similar, columns=['Pearson']).reset_index()
    result = similar_books.sort_values('Pearson', ascending=False).head(11)
    pearson_result = []
    isbn_list = list(result['ISBN'])
    for i in range(1,len(isbn_list)):
        book_index = list(books_data[books_data['ISBN']==isbn_list[i]].index)[0]
        book_details = dict(books_data.loc[book_index])
        pearson_result.append(book_details)
    return pearson_result

