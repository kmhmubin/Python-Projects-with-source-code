import requests
from bs4 import BeautifulSoup

# assign the target url
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# requesting the url
response = requests.get(URL)

# get the raw html
website_html = response.text

# crawling the html
soup = BeautifulSoup(website_html, "html.parser")

# printing the whole website html
# print(soup.prettify())

# finding the h3 tags and grab the movies titles
all_movies = soup.findAll(name="h3", class_="title")
# print all movies
# print(all_movies)

# creating a movie list using list comprehension
movie_titles = [movie.getText() for movie in all_movies]
# print all movies
# print(movie_titles)

# reversing the list using splice operator
movies = movie_titles[::-1]

# creating a new file to store the list
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
