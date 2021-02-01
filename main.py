import time
from selenium import webdriver
from selenium.common import exceptions
from bs4 import BeautifulSoup
import pandas as pd 

session = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
session.get("http://www.csa-ma.com.br/blog-2/")

loadMoreButton = session.find_element_by_class_name('load-more-button')

while True:
    try:
        loadMoreButton.click()
        time.sleep(3)
    except exceptions.StaleElementReferenceException as e:
        break

soup = BeautifulSoup(session.page_source, 'html.parser')
posts = session.find_elements_by_class_name('post-content')

postTitles, postDates, postExcerpts, urls = [], [], [], []

for post in posts:
    postTitles.append(post.find_element_by_class_name('post-title').text)
    postDates.append(post.find_element_by_class_name('post-date').text)
    postExcerpts.append(post.find_element_by_class_name('post-excerpt').text)
    urls.append(soup.find('img', class_='attachment-post-thumbnail').get('src'))

df = pd.DataFrame({'Titulo': postTitles, 'Data de Postagem': postDates, 'Resumo': postExcerpts, 'URL da Imagem': urls})
df.head()
df.to_csv('Scrap_Blog.csv')