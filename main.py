import requests
from bs4 import BeautifulSoup
import smtplib

### Crucial RAM 32GB DDR5 4800MHz CL40 Laptop Memory CT32G48C40S5
CRUCIAL_PRICE_URL = "https://www.amazon.com/Crucial-4800MHz-Laptop-Memory-CT32G48C40S5/dp/B09RVNMGFH/ref=sr_1_1?keywords=ddr5+32gb+sodimm&qid=1658239884&s=pc&sr=1-1"

### Kingston Technology Fury Impact 32GB 4800MT/s DDR5 CL38 SODIMM XMP Ready Laptop Memory Single Module KF548S38IB-32, Black
KINGSTON_PRICE_URL = "https://www.amazon.com/Kingston-Technology-Impact-4800MT-KF548S38IBK2-32/dp/B09T9879D2/ref=sr_1_7?keywords=ddr5%2B32gb%2Bsodimm&qid=1658239884&s=pc&sr=1-7&th=1"

param1 = {
    "Accept-Language" : "en-us",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
}

my_email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"
recipient_email = "YOUR_RECIPIENT_EMAIL"

CRUCIAL_BUYING_PRICE = 150
KINGSTON_BUYING_PRICE = 150

crucial_response = requests.get(url=CRUCIAL_PRICE_URL, headers=param1)
crucial_response = crucial_response.text
soup = BeautifulSoup(crucial_response, "html.parser")
# print(soup)
crucial_price = soup.find_all(name="span", class_="a-offscreen")
crucial_price = float(crucial_price[0].getText().split("$")[1])
print(crucial_price)

kingston_response = requests.get(url=KINGSTON_PRICE_URL, headers=param1)
kingston_response = kingston_response.text
soup = BeautifulSoup(kingston_response, "html.parser")
# print(soup)
kingston_price = soup.find_all(name="span", class_="a-offscreen")
kingston_price = float(kingston_price[0].getText().split("$")[1])
print(kingston_price)

if crucial_price < CRUCIAL_BUYING_PRICE:
    with smtplib.SMTP("smtp.exmail.qq.com") as connection:
        connection.starttls()
        connection.login(user= my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="YOUR_RECIPIENT_EMAIL",
            msg= f"Subject:Crucial DDR5 Low Price Alert!\n\nCrucial DDR5 low price alert! "
                 f"Crucial RAM 32GB DDR5 4800MHz at ${crucial_price}. Click following link to check: {CRUCIAL_PRICE_URL}")

if kingston_price < KINGSTON_BUYING_PRICE:
    with smtplib.SMTP("smtp.exmail.qq.com") as connection:
        connection.starttls()
        connection.login(user= my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="YOUR_RECIPIENT_EMAIL",
            msg= f"Subject:Kingston DDR5 Low Price Alert!\n\nKingston DDR5 low price alert! "
                 f"Kingston Fury 32GB 4800MT/s DDR5 at ${kingston_price}. Click following link to check: {KINGSTON_PRICE_URL}")