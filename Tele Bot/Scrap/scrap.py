import requests
from bs4 import BeautifulSoup

def movies_list():
    url = 'https://www.gamesradar.com/movie-release-dates/'
    movies_data = []

    # Send a GET request to fetch the HTML content
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all 'h2' tags
    h2_tags = soup.find_all('h2')

    # Iterate over each 'h2' tag
    for h2_tag in h2_tags:
        # Store the text of the 'h2' tag
        movie_category = h2_tag.text.strip()
        movie_category_data = {'category': movie_category, 'movies': []}
        
        # Find the next 'ul' sibling of 'h2' tag
        ul_tag = h2_tag.find_next_sibling('ul')
    
        # Check if ul_tag exists
        if ul_tag:
            # Find all 'li' tags within the 'ul' tag
            li_tags = ul_tag.find_all('li')
        
            # Store the text of each 'li' tag
            for li_tag in li_tags:
                movie_category_data['movies'].append(li_tag.text.strip())
        
        # Append movie category data to the list
        movies_data.append(movie_category_data)

    return movies_data

if __name__ == "__main__":
    movies = movies_list()
    for movie in movies:
        print(movie['category'])
        for m in movie['movies']:
            print('-', m)



# # URL of the webpage to scrape
# url = 'https://www.gamesradar.com/movie-release-dates/'

# # Send a GET request to the URL
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content of the webpage
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Find all the article titles (replace 'h2' with the appropriate tag)
#     article_titles = soup.find_all('ul')[6:16]  # Adjust class if needed
    
#     # Extract and print the text of each article title
#     for title in article_titles:
#         print(title.text.strip())
# else:
#     print("Failed to retrieve the webpage")



# Working splitting is confusing
# def movies():
#     source = requests.get('https://www.gamesradar.com/movie-release-dates/')
#     source.raise_for_status()

#     soup = BeautifulSoup(source.text, 'html.parser')

#     article_titles = soup.find_all('li')  # Adjust class if needed

#     movie_titles = []
#     for title in article_titles:
#         print(title)
#         # Extract and print the text of each article title
#         titles_with_dates = title.text.strip()
#         # Use regex to split the text based on the pattern of a date
#         titles_list = re.split(r' – (\w+ \d{1,2}, \d{4})', titles_with_dates)
#         # Append only the movie titles to the list
#         movie_titles.extend([titles_list[i] + '\n' for i in range(len(titles_list)) if i % 2 == 0])

#     print(movie_titles[0]) 
#     return "".join(movie_titles)

# # Example usage:
# print(movies())



# Working Newest
# URL of the website
# url = 'https://www.gamesradar.com/movie-release-dates/'

# # Send a GET request to fetch the HTML content
# response = requests.get(url)

# # Parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find all 'h2' tags
# h2_tags = soup.find_all('h2')

# # Iterate over each 'h2' tag
# for h2_tag in h2_tags:
#     # Print the text of the 'h2' tag
#     print(h2_tag.text)
    
#     # Find the 'ul' tag following the 'h2' tag
#     ul_tag = h2_tag.find_next_sibling('ul')
    
#     # Print the text of the 'ul' tag
#     print(ul_tag.text)


# Working

# def movies():
#     source = requests.get('https://www.gamesradar.com/movie-release-dates/')
#     source.raise_for_status()

#     soup = BeautifulSoup(source.text, 'html.parser')

#     #movies_table = soup.find("article-body", class_="text-copy bodyCopy auto")
#     #movie_rows = movies_table.find_all('li')

#     # Find all the article titles (replace 'h2' with the appropriate tag)
#     article_titles = soup.find_all('ul')[6:16]  # Adjust class if needed

#     #Extract and print the text of each article title
#     movie_titles = []
#     for title in article_titles:
#         print(title.text.strip())
#     else:
#         print("Failed to retrieve the webpage")
#     return "\n".join(movie_titles)  # Join list items into a single string separated by newlines

# # Example usage:
# print(movies())









# Initialize an empty list to store movie names (Caleb)
    #movie_names = []

    # for movie_row in movie_rows:
    #     name_element = movie_row.find('ul', class_="li")
    #     if name_element:
    #         # Append the stripped movie name to the list
    #         movie_names.append(name_element.text.strip())

    # # Check if the list is empty and return a message or the list of names
    # if not movie_names:
    #     return "No movies currently showing."
    # return "\n".join(movie_names)  # Join list items into a single string separated by newlines





# Scrape news and save to JSON file
# news_data = title.text.strip()
# if news_data:
#     with open('january_movies.json', 'w') as f:
#         json.dump(news_data, f)

