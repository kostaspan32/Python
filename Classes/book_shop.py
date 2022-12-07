class Author:
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email


class Book:
    def __init__(self, title, authors, price, copies):
        self.title = title
        self.authors = authors
        self.price = price
        self.copies = copies

    def print_full_title(self):
        print(f'{self.title} by ', end='')
        for i in range(len(self.authors) - 1):
            print(f'{self.authors[i].full_name}, ', end='')
        print(f'{(self.authors[len(self.authors)-1]).full_name}')


    def add_author(self, author):
        self.authors.append(author)


p = Author('Bob Patterson', 'bob@pcookbook.com')
j = Author('James McConan', 'james@pcookbook.com')
b = Book('The Ultimate Python Cookbook', [p, j], 18.25, 43)
b.print_full_title()
t = Author('Tom Rossbow', 'tom@pcookbook.com')
b.add_author(t)
b.print_full_title()
