import requests
import random
from bs4 import BeautifulSoup as bs

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table").find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies
proxies = get_free_proxies()
def get_session(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session
for i in range(5):
    s = get_session(proxies)
    print("Request page with IP:", s.get("https://yandex.ru/pogoda/?lat=59.5&lon=30", timeout=1.5).text.strip())