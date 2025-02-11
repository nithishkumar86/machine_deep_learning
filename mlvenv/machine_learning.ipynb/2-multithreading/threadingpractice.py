urls=["https://en.wikipedia.org/wiki/Deep_learning",
"https://www.geeksforgeeks.org/deep-learning-tutorial/"]

import requests
import time
import threading
from bs4 import BeautifulSoup

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f" fetched document {len(soup.text)} character from url {url}")

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all the documents are fetced")

