import requests
from api_key import api
from send_email import send_email

topic = "tendulkar"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-02-15&" \
      "sortBy=publishedAt&" \
      f"apiKey={api}&" \
       "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
print(content["articles"])

message = ""
message = message + "Subject: Today's news" + "\n"

# Access the article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        message = message + article["title"] + "\n" + article["description"]  \
                  + "\n" + article["url"] + 2*"\n"
print(message)
message = message.encode("utf-8")
send_email(message)