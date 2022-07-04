import requests
from bs4 import BeautifulSoup

def get_lyric(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")
    lyrics = soup.find(id="kashi_area").get_text("\n")
    title = soup.find(class_="blur-filter").find("h2").get_text()
    author = soup.find(class_="blur-filter").find("span").get_text()
    return lyrics, title, author


if __name__ == "__main__":
    hoshino_gen = {
        "喜劇": "https://www.uta-net.com/song/317038/",
        "アイデア": "https://www.uta-net.com/song/254037/",
        "Ain't Nobody Know": "https://www.uta-net.com/song/275639/",
        "時よ": "https://www.uta-net.com/song/198344/",
    }

    for title, url in hoshino_gen.items():
        lyric, _title, author = get_lyric(url)
        print(_title, author)
        print("---------")
        with open(f"./lyrics/{title}.txt", "w", encoding="utf-8") as f:
            f.write(lyric)
