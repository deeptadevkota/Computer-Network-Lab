import requests
import bs4

#IMDB URL for top 50 movies
requestURL = "https://www.imdb.com/chart/top"
response = requests.get(requestURL)

#get the required text from response using lxml parser
soup = bs4.BeautifulSoup(response.text, 'lxml')

movieName = soup.select(".titleColumn > a",limit=50)
imdbRating = soup.select(".imdbRating > strong",limit=50)
actors = soup.select(".titleColumn > a",limit=50)

#display top 50 movies from IMDB 
print('Top 50 movies are:')
for i in range(50):
    print('\nRank: ', i+1)
    print('Movie Name: ' , movieName[i].text,' -|- Movie Rating: ',imdbRating[i].text, ' -|- Movie Actors: ', actors[i].attrs.get("title"))




