class Post:
    def __init__(self):
        self.title = ''
        self.date = ''
        self.excerpt = ''
        self.url = ''
    
    def get_all_posts(self, session):
        return session.find_elements_by_class_name('post-content')