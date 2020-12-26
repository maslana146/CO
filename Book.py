class Book:
    def __init__(self, book_id, score):
        self.book_id = book_id  # There are B different books with IDs from 0 to B–1
        self.score = score  # the score that is awarded when the book is scanned.
        self.borrow = False

    def __str__(self):
        return "\nBook ID: %d \n " \
               "Book score: %d \n" % \
               (self.book_id, self.score)

    def borrow_book(self):
        self.borrow = True  # borrows the book

    def return_score(self, key):  # was borrowed or not
        if key == self.book_id:
            return self.score
        else:
            return None