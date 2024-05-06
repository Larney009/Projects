import requests
from bs4 import BeautifulSoup

def movie_titles():
    # URL of the webpage to scrape
    url = 'https://www.gamesradar.com/movie-release-dates/'
    source = requests.get('https://www.moviesite.co.za/showing.html')
    


    # Send a GET request to the URL
    response = requests.get(url)
    url.raise_for_status()
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find all the article titles (replace 'h2' with the appropriate tag)
        article_titles = soup.find_all('ul')[6:16]  # Adjust class if needed
        #article_titles = soup.find_all('ul', class_='content-list row')[1].find_all('li')

        # Extract and print the text of each article title
        for title in article_titles:
            print(title.text.strip())
    else:
        print("Failed to retrieve the webpage")

    #def get_title():
        # Your logic to retrieve January movies here
        #return title.text  # Example return value
    
movie_titles