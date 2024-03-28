from random import choice, randint
from userdata import *
template_path = 'sql_templates/university'
output_file = 'output.txt'


"""
Generate queries in the following order:
(departments_query, subjects_query, achievements_query, programs_query) --> program_subjects_query --> 
random_enrollee --> (random_enrollee_achievement, random_enrolee_subjects, random_program_enrollees)
"""


def departments_query():
    with open(f"{template_path}/departments.txt") as q:
        query = q.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        for code, name in data["departments"]:
            new_query = query.replace('code', str(code)).replace('name', name)
            f.write(f'{new_query}\n')


def subjects_query():
    with open(f"{template_path}/subjects.txt") as q:
        query = q.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        for code, name in data["subjects"]:
            new_query = query.replace('code', str(code)).replace('name', name)
            f.write(f'{new_query}\n')
            

def achievements_query():
    with open(f"{template_path}/achievements.txt") as q:
        query = q.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        for code, name, bonus in data["achievements"]:
            new_query = query.replace('code', str(code)).replace('name', name).replace('bonus', str(bonus))
            f.write(f'{new_query}\n')


def programs_query():
    with open(f"{template_path}/programs.txt") as q:
        query = q.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        for dept_code, programs in data["edu_programs"].items():
            for program in programs:
                new_query = query.replace('program_code', str(program[0])).replace('program_name', program[1])
                new_query = new_query.replace('department_code', str(dept_code)).replace('plan', str(program[2]))
                f.write(f'{new_query}\n')


def program_subjects_query():
    with open(f"{template_path}/program_subjects.txt") as q:
        query = q.read()
    i = 0
    with open(output_file, 'w', encoding='utf-8') as f:
        for program_subj_code, subjects in data["program_subjects"].items():
            new_query = query.replace('program_id', str(program_subj_code))
            for subject in subjects:
                new_subject_query = new_query.replace('subject_id', str(subject)).replace('code', str(base_id_program_subject + i)).replace('min_result', str(randint(4, 7) * 10))
                i += 1
                f.write(f'{new_subject_query}\n')
                

def random_enrollee(n : int, start_index = 0):
    """
    n : number of queries
    start_index : ID of enrollee to start generating from
    """
    with open(f"{template_path}/enrollees.txt") as q:
        query = q.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i in range(start_index, n + start_index):
            new_query = query.replace('code', str(base_id_enrollee + i))
            new_query = new_query.replace('name', f'{choice(data["surname"])} {choice(data["name"])} {choice(data["lastname"])}')
            f.write(f'{new_query}\n')


def random_enrollee_achievement(n : int, max_index : int, start_index = 0):
    """
    n : number of queries
    max_index : biggest enrollee_id allowed
    start_index : ID of enrollee_achievement to start generating from
    """
    with open(f"{template_path}/enrollee_achievements.txt") as q:
        query = q.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i in range(start_index, n + start_index):
            new_query = query.replace('code', str(base_id_enrollee_achievement + i))
            new_query = new_query.replace('enrollee_id', str(randint(base_id_enrollee, base_id_enrollee + max_index - 1)))
            new_query = new_query.replace('achievement_id', str(choice(data["achievements"])[0]))
            f.write(f'{new_query}\n')


def random_enrolee_subjects(n : int, max_index : int, start_index = 0):
    """
    n : number of queries
    max_index : biggest enrollee_id allowed
    start_index : ID of enrolee_subject to start generating from
    """
    with open(f"{template_path}/enrollee_subjects.txt") as q:
        query = q.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i in range(start_index, n + start_index):
            new_query = query.replace('code', str(base_id_enrolee_subject + i))
            new_query = new_query.replace('enrollee_id', str(randint(base_id_enrollee, base_id_enrollee + max_index - 1)))
            new_query = new_query.replace('subject_id', str(choice(data["subjects"])[0]))
            new_query = new_query.replace('result', str(randint(40, 100)))
            f.write(f'{new_query}\n')


def random_program_enrollees(n : int, max_index : int, start_index = 0):
    """
    n : number of queries
    max_index : biggest enrollee_id allowed
    start_index : ID of program_enrollee to start generating from
    """
    with open(f"{template_path}/program_enrollees.txt") as q:
        query = q.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i in range(start_index, n + start_index):
            new_query = query.replace('code', str(base_id_program_enrollee + i))
            new_query = new_query.replace('program_id', str(choice(list(data["program_subjects"]))))
            new_query = new_query.replace('enrollee_id', str(randint(base_id_enrollee, base_id_enrollee + max_index - 1)))
            new_query = new_query.replace('result', str(randint(40, 100)))
            f.write(f'{new_query}\n')
