class Book:

    def __init__(self, isbn, title, revisions_quantity, publication_year, language_code, rating):
        self.isbn = isbn
        self.title = title
        self.revisions_quantity = int(revisions_quantity)
        self.publication_year = int(publication_year)
        self.language_code = int(language_code)
        self.rating = rating


def to_string(book):
    return "\nDatos del libro: \n\t ISBN: " + book.isbn + \
           "\n\t TÍTULO: " + book.title + \
           "\n\t AÑO DE PUBLICACIÓN: " + str(book.publication_year) + \
           "\n\t CÓDIGO DE IDIOMA: " + str(book.language_code) + \
           "\n\t CANTIDAD DE REVISIONES: " + str(book.revisions_quantity) + \
           "\n\t RATING " + str(book.rating)


def validate_book(book):
    if len(book.isbn) != 10:
        return False
    if not (0 < book.language_code <= 27):
        return False
    return True
