import requests

from bs4 import BeautifulSoup


content = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(content.text, "html.parser")
movie_names = soup.find_all(name="h3", class_ = "jsx-4245974604")

with open("output.text", mode="w") as file:
    file.write(soup.prettify())

print(movie_names)
