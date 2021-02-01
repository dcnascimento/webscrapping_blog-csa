import time
from selenium import webdriver
from selenium.common import exceptions
from bs4 import BeautifulSoup
import pandas as pd 
from page import Page
from post import Post
from scrap import Scrap

session = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')

main_page = Page()
post = Post()
scrap = Scrap()

main_page.load_page(session)
main_page.show_all_posts(session)

bs = BeautifulSoup(session.page_source, 'html.parser')

list_posts = post.get_all_posts(session)

post.title, post.date, post.excerpt, post.url = [], [], [], []

for p in list_posts:
    post.title.append(scrap.get_titles(p))
    post.date.append(scrap.get_dates(p))
    post.excerpt.append(scrap.get_excerpts(p))
    post.url.append(scrap.get_url_image(bs))

df = pd.DataFrame({'Titulo': post.title, 'Data de Postagem': post.date, 'Resumo': post.excerpt, 'URL da Imagem': post.url})
df.head()
df.to_csv('blog_content.csv')