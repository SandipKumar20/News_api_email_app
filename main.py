import requests
from api_key import api
from send_email import send_email

url = f"https://newsapi.org/v2/everything?q=tendulkar&from=2024-02-14&sortBy=publishedAt&apiKey={api}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
print(content["articles"])

message = ""

# Access the article titles and description
for article in content["articles"]:
    if article["title"] is not None:
        message = message + article["title"] + "\n" + article["description"] + 2*"\n"
print(message)
message = message.encode("utf-8")
send_email(message)