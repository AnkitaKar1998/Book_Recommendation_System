# Book Recommendation System

<ul>
<li> This project is implemented as a website which shows recommended books when the user selects a particular book.
<li> Website link: <i>https://ml-book-recommendation-system.herokuapp.com/</i>
<li> This is a hybrid recommendation system in which three different algorithm is used: Collaborative Filtering using Pearson Corelation, Vollaborative Filtering using KNN and Content Based algorithm.
<li> Book Crossing Dataset is used for this project which can be found here <i>http://www2.informatik.uni-freiburg.de/~cziegler/BX/</i>
</ul>

## How to run the project on localhost

<ol>
<li> Clone the repository.
<li> Install Flask module, if not installed in your machine, using command

        pip install Flask

<li> Open the project dolder. Open command prompt/terminal.
<li> Run app.py file.
</ol>

## Note

<ul>
<li> The recommendation of each book viewed is based only on the ratings of users and other features of that book in the dataset. Current user view actions are not saved and hence not considered for recommendation.
<li> The project can be further extended by creating a register/login system and a rating system where the logged in users can give rating to each book. The recommendations can then be evaluated based user history and new ratings.
</ul>