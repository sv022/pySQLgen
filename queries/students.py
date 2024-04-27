from random import choice, randint
from userdata import *
template_path = 'sql_templates/students'
output_file = 'output.txt'


def random_student(n : int):
    """
    n : number of queries
    """
    with open(f"{template_path}/students.txt") as q:
        query = q.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i in range(n):
            name = f'{choice(data["surname"])} {choice(data["name"])} {choice(data["lastname"])}'
            group = f'{choice(data["student_groups"])}-{randint(1, 9):02}-{20 + randint(2, 4)}'
            new_query = query.replace('name', name)
            new_query = new_query.replace('group', group)
            new_query = new_query.replace('subject', choice(data["student_subjects"]))
            new_query = new_query.replace('score', str(randint(3, 5)))
            
            f.write(f'{new_query}\n')