class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def info(self):
        print(f"title: {self.title} and pages: {self.pages} .")

book = Book("animals", 567)
book.info()
        