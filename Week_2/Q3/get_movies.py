import requests
import bs4

#IMDB URL for top 50 movies
requestURL = "https://www.imdb.com/chart/top"
response = requests.get(requestURL)

#get the required text from response using lxml parser
soup = bs4.BeautifulSoup(response.text, 'lxml')

movieName = soup.select(".titleColumn > a",limit=10)
imdbRating = soup.select(".imdbRating > strong",limit=10)
actors = soup.select(".titleColumn > a",limit=10)

#display top 50 movies from IMDB 
print('\nTop 50 movies are:')
for i in range(10):
    print('\nRank: ', i+1)
    print('Movie Name: ' , movieName[i].text,'\nMovie Rating: ',imdbRating[i].text, '\nMovie Actors: ', actors[i].attrs.get("title"))




