# KP tracking 
from bs4 import BeautifulSoup
import requests

# index.html is for testing purposes 


# Function that extracts contents of a page 
def get_content(page_source, page_search, page_number):
    page_search.lower()
    r = requests.get(page_source)
    soup = BeautifulSoup(r.text, 'lxml')
    for match in soup.find_all('a', class_='adName', href=True):
        heading = match.text
        if input_form in heading.lower():
            print(f'{heading.lower()} - {match["href"]}')
    print(f'''
    
    Page {page_number}
    
    ''')

# Function for defining last page
def page_num():
    r = requests.get('https://www.kupujemprodajem.com/mobilni-telefoni/apple-iphone/grupa/23/489/1')
    soup = BeautifulSoup(r.text, 'lxml')
    return soup.find('input', {'name':'data[page]'}).get('value')
    


# Input for product we want to search
input_form = input("Search >>> ")

# Source page for getting number of the last page
src = 'https://www.kupujemprodajem.com/mobilni-telefoni/apple-iphone/grupa/23/489/'
max_page = int(page_num())

# Iterating through every page and extracting content that satisfies the input
for page in range(1, max_page + 1):
   get_content(src+f'{str(page)}', input_form, page)

