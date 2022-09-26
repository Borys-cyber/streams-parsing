import time
from threading import Thread
import requests
from lxml import html

start = time.perf_counter()
names = ["krosivki-nike-md-runner-2-749794-010", "krosivki-zhinochi-nike-air-force-1-pixel-dh3860-100", "shkarpetki-nike-3ppk-value-cotton-sx4508-101"]
for name in names:
    url = f"https://idealsport.com.ua/{name}"
    response = requests.get(url)
    tree = html.fromstring(response.text)
    xPath = '//*[@id="main"]/div[1]/section/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div/div/text()'
    price = tree.xpath(xPath)
    print(f'Ціна:{name}{price[2]}')
end = time.perf_counter()
print(f'time without threads = {end - start:0.2f}')




