class Scrap:
    def __init__(self):
        pass

    def get_titles(self, p):
        return p.find_element_by_class_name('post-title').text
    
    def get_dates(self, p):
        return p.find_element_by_class_name('post-date').text

    def get_excerpts(self, p):
        return p.find_element_by_class_name('post-excerpt').text
    
    def get_url_image(self, bs):
        return bs.find('img', class_='attachment-post-thumbnail').get('src')