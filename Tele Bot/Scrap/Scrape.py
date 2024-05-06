import requests
from bs4 import BeautifulSoup


def scrape_movie_web():
    # URL of the website
    url = 'https://movieweb.com/movies/2024/'

    # Adding headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send a GET request to the URL with headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with the class 'movie-details'
        movie_elements = soup.find_all(class_='movie-details')

        # Extract movie titles, release dates, and images
        movies_info = []
        for element in movie_elements:
            title = element.find('h3').text.strip()
            release_date = element.find(class_='release-date').text.strip()
            image_url = element.find('img')['src']
            movies_info.append({'title': title, 'release_date': release_date, 'image_url': image_url})

        # Print the movie titles, release dates, and image URLs
        for movie in movies_info:
            print("Title:", movie['title'])
            print("Release Date:", movie['release_date'])
            print("Image URL:", movie['image_url'])
            print()

    else:
        print("Failed to retrieve the website.")

if __name__ == "__main__":
    scrape_movie_web()






# movie_titles = []
#     for title in article_titles:
#         # Extract and print the text of each article title
#         titles_with_dates = title.text.strip()
#         # Use regex to split the text based on the pattern of a date
#         titles_list = re.split(r'(\d{1,2}[A-Za-z]{2})', titles_with_dates)
#         # Append only the movie titles to the list
#         movie_titles.extend([titles_list[i] for i in range(len(titles_list)) if i % 2 == 0])
        
#     return "\n".join(movie_titles)