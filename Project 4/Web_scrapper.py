import requests
from bs4 import BeautifulSoup as bs

user_name = input("Enter user name: ")
url = "https://www.github.com/"+user_name
print(url)
r = requests.get(url)
soup = bs(r.content, 'html.parser')
# print(soup)
profile_photo = soup.find('img style',  {'class' : 'avatar'})['src']
print(profile_photo)