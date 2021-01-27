import requests
import smtplib


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_STOCKS = "your alphavantage api key"
API_KEY_NEWS = "your news api key"


my_email = "your email"
password = "your password"
receiver = "receiver"


# Stocks api
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCKS
}
response_stock = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response_stock.raise_for_status()
data_stock = response_stock.json()
yesterday_price_close = float(data_stock["Time Series (Daily)"]["2021-01-26"]["4. close"])
day_before_price_close = float(data_stock["Time Series (Daily)"]["2021-01-25"]["4. close"])
percentage = abs(float(yesterday_price_close) - float(day_before_price_close))
differecente_percentage = percentage / float(yesterday_price_close) * 100
result = f"{round(differecente_percentage, 2)}%"
print(result)


# News api
news_params = {
    "q": COMPANY_NAME,
    "apiKey": API_KEY_NEWS
}
response_news = requests.get(url=NEWS_ENDPOINT, params=news_params)
response_news.raise_for_status()
data_news = response_news.json()
articles = data_news["articles"][:4]


if differecente_percentage >= 5:
    for article in articles:
        message = f'\nHeadline:\n{article["title"]}\nBrief:\n{article["description"]}'
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n{}'
            connection.sendmail(
                my_email,
                receiver,
                fmt.format(my_email, receiver, STOCK + " " + result, message).encode('utf-8')
            )
