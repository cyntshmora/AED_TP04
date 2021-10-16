import books_manager
import os.path
import pickle
import os
from book import *


def get_list_from_file():
    file_name = "libros.csv"
    if os.path.exists(file_name):
        m = open(file_name, mode="rt", encoding="utf8")
        book_list = []
        first_line_read = False
        for line in m:
            if first_line_read:
                data = line.split(",")
                books_manager.add_in_order_isbn(book_list, Book(data[5][0:10], data[0], data[1], data[2], data[3], data[4]))
            else:
                first_line_read = True
        m.close()
        return book_list
    return None


def generate_books_file(matrix_books, file_name):
    saved_books = 0
    m = open(file_name, "wb")
    for j in range(len(matrix_books)):
        for i in range(len(matrix_books[j])):
            if matrix_books[j][i] is not None:
                pickle.dump(matrix_books[j][i], m)
                saved_books += 1
    m.close()
    return saved_books


def show_file(file_name):
    if os.path.exists(file_name):
        tam = os.path.getsize(file_name)
        m = open(file_name, "rb")
        i = 0
        while m.tell() < tam:
            reg = pickle.load(m)
            i += 1
            print(to_string(reg))
        m.close()
