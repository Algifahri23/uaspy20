class MainApp():
    def __init__(self):
        self.books = []


if __name__ == "__main__":
    app = MainApp()
    app.run()
class MainApp(BaseApp):
    def _init_(self):
        self.books = []
        self.InputBook = []
        self.ViewBook = []
        BaseApp._init_(self)


class ViewBook(Book):
    def _init_(self):
        vBook = ViewBook (self, books)
        vBook.list_book()


    if _name_ == "_main_":
        app = MainApp(BaseApp)
        app.run()


    @property
    def list_book(self):
        return self.list_book
    def add_book(self):
        return self.add_book()
    def search_book(self):
        return self.search_book()
