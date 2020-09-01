# KP tracking 
from multiprocessing import Pool
from bs4 import BeautifulSoup
import requests

# index.html is for testing purposes 


# Function that extracts contents of a page 
def get_content(page_search, urls):
    page = 1
    for url_ in urls:
        scrape(url_, page_search, page)
        page+=1


# Scraping function that does all the hard work on single page URL
def scrape(url_, page_search, page_number):
    page_search.lower()
    r = requests.get(url_)
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

# Getting all urls in one list

def get_urls(src, max_page):
    ls = []    
    for page in range(1, max_page + 1):
        ls.append(src+f'{str(page)}')
    return ls





if __name__=="__main__":

    try:

        # Input for product we want to search
        input_form = input("Search >>> ")

        # Source page for getting number of the last page
        src = 'https://www.kupujemprodajem.com/mobilni-telefoni/apple-iphone/grupa/23/489/'
        max_page = int(page_num())

        # Iterating through every page and extracting content that satisfies the input

        print('\n')
        get_content(input_form, get_urls(src, max_page))
    
    except: 
        
        print("An error occurred, please try again")

