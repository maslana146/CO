# Znalazłem jakies linki do githuba z tym problemem:
# https://github.com/rgab1508/hashcode
# https://github.com/Brinfer/HashCode-2020/blob/main/src/QualificationRound/Class/Library.py
# https://github.com/pgimalac/hashcode-evaluator/tree/master/2020-qualification-round

class Book:
    def __init__(self, type, points):
        self.book_id = type         # There are B different books with IDs from 0 to B–1
        self.score = points         # the score that is awarded when the book is scanned.
    def __str__(self):
        return "Book ID: %d \n Book score: %d \n"  % (self.book_id, self.score)

class Library:
    def __init__(self, type, books, time, number):
        self.library_id = type                  # There are L different libraries with IDs from 0 to L–1.
        self.set_of_books = books               # the set of books in the library,
        self.sign_up_time = time                # the time in days that it takes to sign the library up for scanning,
        self.books_per_day = number              # the number of books that can be scanned each day from the library once the library is signed up

    def __str__(self):
        return "Library ID: %d\n List Of books: %s\n Time to sign up: %d\n Books per day: %d" % (self.library_id,
                                                                                                 ','.join(str(i) for i in self.set_of_books),
                                                                                                 self.sign_up_time,
                                                                                                 self.books_per_day)


LIBRARIES = []

num_of_books, number_of_libraries, time = map(int, input().split())     #
                                                                        #
scores_of_books = list(map(int, input().split()))                       #
                                                                        #
for library in range(number_of_libraries):                              #
    b, time, per_day = map(int, input().split())                        #   Kod wczytujący dane, przebia je na ksiązki i biblioteki
    books_in_library = list(map(int, input().split()))                  #
    books = []                                                          #
    for book in books_in_library:                                       #
        books.append(Book(book, scores_of_books[book]))                 #
    LIBRARIES.append(Library(library, books, time, per_day))            #


