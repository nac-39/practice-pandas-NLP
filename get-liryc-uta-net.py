import requests
from bs4 import BeautifulSoup

def get_lyric(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")
    lyrics = soup.find(id="kashi_area").get_text("\n")
    return lyrics


if __name__ == "__main__":
    hoshino_gen = {
        "喜劇": "https://www.uta-net.com/song/317038/",
        "アイデア": "https://www.uta-net.com/song/254037/",
        "Ain't Nobody Know": "https://www.uta-net.com/song/275639/",
        "時よ": "https://www.uta-net.com/song/198344/",
    }

    for title, url in hoshino_gen.items():
        print(title)
        lyric = get_lyric(url)
        print(lyric[:100])
        print("---------")
        with open(f"./lyrics/{title}.txt", "w", encoding="utf-8") as f:
            f.write(lyric)
