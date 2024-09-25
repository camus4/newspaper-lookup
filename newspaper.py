import requests
from bs4 import BeautifulSoup
import sys
import webbrowser

url = 'https://t3n.de/'
open_url = "https://t3n.de/news"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# show headline 
latest_article = soup.find('article', class_='c-pin -hero tg-')
title = latest_article.find('a', class_='u-link-newstitle u-text-extralarge')
title = title.text

# show short description
content = soup.find_all('div', class_ = 'o-grid__item c-pin__body -hero u-gap-top-reset')[0]
content = content.text

print(f'headline: \n{title}\n')

while True:
    try: 
        want_to_read = input("Do you want to read a short extract from the article? (yes/no)\n")
        if want_to_read == "yes":
            print(f'\ncontent:\n\n{content}\n')

            open_page_url= input("do you want to open the url to see the whole article? (yes/no)? ")

            if open_page_url == "yes":
                open_url = None
                webbrowser.open("https://t3n.de/news")
            else:
                sys.exit()
            
            while True:
                exit = input('enter a key to exit')
                sys.exit()
                    
        else:
            sys.exit()
    except ValueError:
        print('Value Error')
        break

# add previous article , look for HTML adjustments 



