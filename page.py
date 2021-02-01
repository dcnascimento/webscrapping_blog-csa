from time import sleep
from selenium import webdriver
from selenium.common import exceptions

class Page:
    def __init__(self):
        self.index = "http://www.csa-ma.com.br/blog-2/"

    def load_page(self, session):
        session.get(self.index)

    def show_all_posts(self, session):
        loadMoreButton = session.find_element_by_class_name('load-more-button')
        while True:        
            try:
                loadMoreButton.click()
                sleep(3)
            except exceptions.StaleElementReferenceException as e:
                break


    

