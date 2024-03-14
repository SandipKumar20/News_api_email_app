import requests
from api_key import api

url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-02-14&sortBy=publishedAt&apiKey={api}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
print(content["articles"])

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])