from random import randint, choice
from userdata import *
from string import ascii_uppercase, digits


template_path = 'sql_templates/books'
output_file = 'output.txt'


def random_book(n : int):
    with open(f"{template_path}/books.txt") as q:
        query = q.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for _ in range(n):
            book_name = russian_words[randint(0, len(russian_words))].capitalize() + ' ' + russian_words[randint(0, len(russian_words))].capitalize()
            
            genre = choice(data["genres"])
            
            new_query = query.replace('NAME', book_name).replace('GENRE', genre)
            f.write(f'{new_query}\n')


def random_author(n : int):
    with open(f"{template_path}/authors.txt") as q:
        query = q.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for _ in range(n):
            name = choice(data["name"])
            surname = choice(data["surname"])
            lastname = choice(data["lastname"])
            
            new_query = query.replace('LASTNAME', lastname).replace('SURNAME', surname).replace('NAME', name)
            f.write(f'{new_query}\n')


def random_book_author(n : int, max_author_index: int, max_book_index : int):
    with open(f"{template_path}/book_authors.txt") as q:
        query = q.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for _ in range(n):
            author_id = randint(0, max_author_index)
            book_id = randint(0, max_book_index)
            
            new_query = query.replace('AUTHORID', author_id).replace('BOOKID', book_id)
            f.write(f'{new_query}\n')


def random_catalog_entry(n : int):
    with open(f"{template_path}/catalog.txt") as q:
        query = q.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for _ in range(n):
            code_symbolds = [*ascii_uppercase, *digits]
            code = ''.join([choice(code_symbolds) for _ in range(10)])
            
            name = russian_words[randint(0, len(russian_words))] + russian_words[randint(0, len(russian_words))]

            publisher = "Издательство" + russian_words[randint(0, len(russian_words))]
            publish_year = randint(1990, 2024)

            pages = randint(40, 500)
            
            new_query = query.replace('CODE', code).replace('NAME', name).replace('PUBLISHER', publisher)
            new_query = new_query.replace('PUBLISHYEAR', publish_year).replace('PAGES', pages)
            f.write(f'{new_query}\n')