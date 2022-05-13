'''
This is an example plugin for fetching and parsing blog at hamatti.org/blog
'''

from bs4 import BeautifulSoup
import requests


URL = 'https://hamatti.org/blog'

def _parse(soup):
    blog_list = soup.find('div', { 'id': 'blog-post-list' })
    blog_posts = blog_list.find_all('li')

    posts = []
    for post in blog_posts:
        href = post.a.attrs['href']
        title = post.a.text
        posts.append({
            'href': href,
            'title': title
        })
    
    return posts

def call():
    print(f'Running plugin {__name__} from {URL}')
    soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
    
    return _parse(soup)

