import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

EMAIL = ""
PASSWORD = ""

url = "https://www.amazon.in/Apple-MacBook-14-inch-10%E2%80%91core-16%E2%80%91core/dp/B09JQWQN6H/ref=sr_1_3?crid=1FIWLVXY35YLE&keywords=macbook+m1+pro&qid=1644212357&sprefix=macbook+m1+pr%2Caps%2C239&sr=8-3"

response = requests.get(url, headers={"User-Agent": "Defined"})
response.raise_for_status()

webpage = response.content

soup = BeautifulSoup(webpage, "html.parser")

price_tag = soup.find(name="span", class_="a-offscreen").getText()
price_tag = price_tag.replace("₹", "").replace(",", "")
price = float(price_tag)

my_price = 200000.0

if price <= my_price:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)

        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:Hooray! Your product is as cheap as you want!\n\n"
                                                                 f"Buy your product right now, it's price now: {price}")
