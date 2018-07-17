import bs4, requests
def getRating(url):
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    name = soup.select("#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > h1")
    rating = soup.select('#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > div.imdbRating > div.ratingValue > strong > span')
    return name[0].get_text(), rating[0].get_text()
name, rating = getRating("https://www.imdb.com/title/tt0068646/?ref_=nv_sr_1")
print("The IMDB rating of %s:%s" %(name,rating))
