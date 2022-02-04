import cloudscraper
from bs4 import BeautifulSoup
import requests
import re
import os
import sys

path = r"your_path"

def getOsea(url):
    global name
    global nft_hyperlink
    try:
        scraper = cloudscraper.create_scraper()
        html = scraper.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        name = soup.find("a", attrs={'class': 'styles__StyledLink-sc-l6elh8-0 ekTmzq CollectionLink--link'}).string
        link = soup.find('meta', content=re.compile("https://lh3.googleusercontent.com/"))
        nft_hyperlink = link.get("content")
    except Exception:
        getOsea(url)

if __name__ == "__main__":
    collection = input("Contract address of the NFT: ")
    start = int(input("From NFT Number (starting from 1): "))
    end = int(input("Until NFT Number (If you want all NFTs of the collection insert the total amount here): "))
    print("Wait until it finishes downloading ! :)")
    try:
        while start <= end:
            url = f"https://opensea.io/assets/{collection}/{start}"
            getOsea(url)
            if not os.path.exists(f"{path}/{name}"):
                os.makedirs(f"{path}/{name}")
            r = requests.get(nft_hyperlink)
            nft_img = open(f"{path}/{name}/{name}_{start}.png", "wb")
            nft_img.write(r.content)
            nft_img.close()
            start += 1
    except Exception:
        print("err")
        sys.exit(1)



