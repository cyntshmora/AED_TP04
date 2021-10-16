import book
import files_manager


def add_in_order_isbn(list_books, book_to_add):
    if book.validate_book(book_to_add):
        n = len(list_books)
        pos = n
        left, right = 0, n - 1
        while left <= right:
            middle = (left + right) // 2
            if list_books[middle].isbn == book_to_add.isbn:
                pos = middle
                break

            if book_to_add.isbn < list_books[middle].isbn:
                right = middle - 1
            else:
                left = middle + 1

        if left > right:
            pos = left
        list_books[pos:pos] = [book_to_add]
    else:
        print("Se encontró un libro con un formato no válido, no ha sido posible añadir el mismo a la lista")


def show_books_list(list_books):
    for book_item in list_books:
        print(book.to_string(book_item))


def generate_mat(fil, col):
    mat = [[None] * col for i in range(fil)]
    return mat


def fill_ratings_matrix(vec, mat):
    for reg in vec:
        if 2000 <= reg.publication_year <= 2020:
            if mat[reg.language_code-1][reg.publication_year-2000] is None or \
                    mat[reg.language_code-1][reg.publication_year-2000].rating <= reg.rating:
                mat[reg.language_code-1][reg.publication_year-2000] = reg
