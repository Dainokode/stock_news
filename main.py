import requests
import smtplib


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_STOCKS = "0AYK50D3V7560AVZ"
API_KEY_NEWS = "d1e7b67977834b279a722c64e699eedf"


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
result = f"{differecente_percentage}%"
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
                fmt.format(my_email, receiver, STOCK + result, message).encode('utf-8')
            )










## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

