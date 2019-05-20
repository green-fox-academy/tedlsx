import re


##  library
class book(object):
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def toString(self):
        return f"{self.author}: {self.title} ({self.year})"

boo = book("Douglas Adams", "The Hitchhiker's Guide to the Galaxy", "1979")

boo.toString()



class bookshelf(book):
    def __init__(self, booklist = []):
        self.booklist = booklist
        
        
    
    def add(self, new_author, new_title, new_year, page_num = 0):
        if page_num == 0:
            book_string = book(new_author, new_title, new_year)
            self.booklist.append(book_string)
        elif page_num > 0:
            book_string = Book(new_author, new_title, new_year, page_num)
            self.booklist.append(book_string)

    def remove(self, new_author, new_title, new_year):
        book_string = book(new_author, new_title, new_year)
        self.booklist.remove(book_string)
        

    def favouriteAuthor(self):
        author_list = []
        popular_list = []
        for book in self.booklist:
            book = book.toString()
            author = re.findall("([0-9a-zA-Z\s.]+)\:", book)[0]
            author_list.append(author)  

        first_popular = max(set(author_list), key = author_list.count)            
        popular_list.append(first_popular)
        for name in author_list:
            if author_list.count(name) == author_list.count(first_popular):
                    popular_list.append(name)
        return set(popular_list)

    def earliestPublished(self):
        first_year = year = re.findall("\((\d+)\)", self.booklist[0].toString())
        for book in self.booklist:
            book = book.toString()
            year = re.findall("\((\d+)\)", book)
            if year <= first_year:
                early_year = year
            first_year = year
        return early_year

    def latestPublished(self):
        first_year = year = re.findall("\((\d+)\)", self.booklist[0].toString())
        for book in self.booklist:
            book = book.toString()
            year = re.findall("\((\d+)\)", book)
            if year >= first_year:
                late_year = year
            first_year = year
        return late_year

    def toString(self):
        return f"number of books is: {len(self.booklist)}, earlist published year is: {self.earliestPublished()}, latest published year is: {self.latestPublished()} and the favourite author is: {self.favouriteAuthor()}. "

    def find_lightest(self):
        weight_list = []
        light_list = []
        for book in self.booklist:
            weight_list.append(book.weight)
        lightest = min(weight_list)
        light_index = weight_list.index(lightest)       
        light_list.append(self.booklist[light_index].author)
        for book in self.booklist:
            if book.weight == lightest:
                    light_list.append(book.author)
        return set(light_list)    

    def find_mostpages(self):
        page_list = []
        most_page_list = []
        for book in self.booklist:
            page_list.append(book.page_num)
        most_page = max(page_list)
        page_index = page_list.index(most_page)       
        most_page_list.append(self.booklist[page_index].author)
        for book in self.booklist:
            if book.page_num == most_page:
                    most_page_list.append(book.author)
        return set(most_page_list)


a = bookshelf()
b = book("Douglas Adams", "The Hitchhiker's Guide to the Galaxy", "1979")
a.add("Douglas Adams", "The Hitchhiker's Guide to the Galaxy", "1979" )
a.add("a", "b", "1666")
a.add("a", "asd", "1444")
a.add("b", "asd", "1444")
a.add("b", "asd", "1444")
a.toString()

a = Hardcover()


### Bookshelf
class Book:
    def __init__(self, title, author, year, page_num, weight):
        self.title = title
        self.author = author
        self.year = year
        self.page_num = page_num
        self.weight = weight
    
    


class hardcover(Book):
    def __init__(self, title = "", author = "", year = "", page_num = 0, weight = 0) :
        Book.__init__(self, title, author, year, page_num, weight)
        self.title = title
        self.author = author
        self.year = year
        self.page_num = page_num
        self.weight = self.page_num * 10 + 100

    def toString(self):
        return f"{self.author}: {self.title} ({self.year})"

class paperback(Book):
    def __init__(self, title = "", author = "", year = "", page_num = 0, weight = 0):
        Book.__init__(self, title, author, year, page_num, weight)
        self.title = title
        self.author = author
        self.year = year
        self.page_num = page_num
        self.weight = self.page_num * 10 +20
    
    def toString(self):
        return f"{self.author}: {self.title} ({self.year})"


a = hardcover("a.title", "a.author", "1234", 24)
a.toString()
b = paperback("b.title", "b.author", "2009", 45)


my_bookshelf = bookshelf([a,b])
my_bookshelf.find_lightest()
my_bookshelf.find_mostpages()

