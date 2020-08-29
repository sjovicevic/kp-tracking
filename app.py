# KP tracking 
from bs4 import BeautifulSoup
import requests

def page_num():
    r = requests.get('https://www.kupujemprodajem.com/mobilni-telefoni/apple-iphone/grupa/23/489/1')
    ls = []
    soup = BeautifulSoup(r.text, 'lxml')
    param = {'name':'data[page]'}
    for li in soup.find_all('input', param):
        li.get('value')
    return ls


string = 'https://www.kupujemprodajem.com/mobilni-telefoni/apple-iphone/grupa/23/489/'
print(page_num())
input_form = input("Search >>> ")
input_form.lower()
for page in range(1,3):
    r = requests.get(string+f'{page}')
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'lxml')
    for match in soup.find_all('a', class_='adName', href=True):
        heading = match.text
        if input_form in heading.lower():
            print(f'{heading} - {match["href"]}')
