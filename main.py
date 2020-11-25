# Znalazłem jakies linki do githuba z tym problemem:
# https://github.com/rgab1508/hashcode
# https://github.com/Brinfer/HashCode-2020/blob/main/src/QualificationRound/Class/Library.py
# https://github.com/pgimalac/hashcode-evaluator/tree/master/2020-qualification-round

# TEST INPUT DATA:
# 6 2 7
# 1 2 3 6 5 4
# 5 2 2
# 0 1 2 3 4
# 4 3 1
# 3 2 5 0



class Book:
    def __init__(self, type, points):
        self.book_id = type         # There are B different books with IDs from 0 to B–1
        self.score = points         # the score that is awarded when the book is scanned.
        self.borrow = False

    def __str__(self):
        return "\nBook ID: %d \n " \
               "Book score: %d \n"  % \
               (self.book_id, self.score)

    def boroowBook(self):
        self.borrow = True   # borrows the book

    def isAvailable(self):   # was borrowed or not
        return not self.borrow





class Library:
    def __init__(self, type, books, time, number):
        self.library_id = type                  # There are L different libraries with IDs from 0 to L–1.
        self.set_of_books = books               # the set of books in the library,
        self.sign_up_time = time                # the time in days that it takes to sign the library up for scanning,
        self.books_per_day = number             # the number of books that can be scanned each day from the library once the library is signed up

        self.posibleScore()                     # maximum possible score

    def __str__(self):
        return "Library ID: %d\n " \
               "List of books: %s\n " \
               "Time to sign up: %d\n " \
               "Books per day: %d" % \
               (self.library_id,
                ''.join(str(i) for i in self.set_of_books),
                self.sign_up_time,
                self.books_per_day)

    def posibleScore(self):         # returns the maximum possible score
        pos_score = 0
        for book in self.set_of_books:

            pos_score += book.score
        return pos_score


class Program:                  # tak sobie mysle że będzie to na pewno działało na jakiejś rekurencji daltego zrobilem
    def __init__(self):         # tą klase program by trzymała wyniki
        self.max_score = 0
        self.visited_libraries = []
        self.borrowed_books = []




LIBRARIES = []

num_of_books, number_of_libraries, time = map(int, input().split())         #
                                                                            #
scores_of_books = list(map(int, input().split()))                           #
                                                                            #
for library in range(number_of_libraries):                                  #
    b, time, per_day = map(int, input().split())                            #   Kod wczytujący dane, przebia je na ksiązki i biblioteki
    books_in_library = list(map(int, input().split()))                      #
    books = [Book(book, scores_of_books[book]) for book in books_in_library]    #
    LIBRARIES.append(Library(library, books, time, per_day))                    #
