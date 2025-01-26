import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Displaying the columns without truncation

pd.set_option('display.max_columns', None)

# Set the display option to show more characters per column if necessary
# pd.set_option('display.max_colwidth', None)

# ReadingBook from the csv file
books = pd.read_csv('BX-Books.csv', sep=';', on_bad_lines='skip', encoding="latin-1")
books.columns = ['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher','Image-URL-S','Image-URL-M','Image-URL-L']
print(books.head())
# Logging the books

# Reading the users from the csv file
users = pd.read_csv('BX-Users.csv', sep=';', on_bad_lines='skip', encoding="latin-1")
users.columns = ['User-ID','Location','Age']

print(users.head())
# Logging the users

# Reading the books rating from the csv file
ratings = pd.read_csv('BX-Book-Ratings.csv', sep=';', on_bad_lines='skip', encoding="latin-1")
ratings.columns = ['User-ID','ISBN','Book-Rating']
print(ratings.head())
# Logs the books rating to the console


# Data Analysis USing MatplotLib for


# 1 displaying the age group

users.Age.hist(bins=range(0,100))
plt.title('User Age Group')
plt.xlabel('Age')
plt.ylabel('Number of Users')
plt.show()

# 2 Display the commutative rating of all the books

ratings['Book-Rating'].value_counts().plot(kind='pie')
plt.title('Combined Rating of All Books')
plt.xlabel('Rating')
plt.show()


# Creating Algorithm


# Getting the books that has received the highest ratings
recommender_byRating = pd.DataFrame(ratings.groupby('ISBN')['Book-Rating'].count())
recommender_byRating.sort_values('Book-Rating', ascending=False).head()
print(recommender_byRating.sort_values('Book-Rating', ascending=False).head())

# Popular Books

overall_rating = pd.merge(ratings, books, on='ISBN')
book_rated = (overall_rating.groupby(by = ['Book-Title'])['Book-Rating'].count().reset_index())
book_rated.head()
print(book_rated.head())

# Demographic Based Recommendation

overall_ratingCount = overall_rating.merge(book_rated, left_on =
'Book-Title', right_on = 'Book-Title', how = 'left')
bookUser = overall_ratingCount.merge(users, left_on = 'User-ID', right_on =
'User-ID', how = 'left')


# Filter the results for users residing in Australia

demographic = bookUser[bookUser['Location'].str.contains("australia|spain")]
print(demographic.head())