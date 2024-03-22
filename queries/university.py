from random import choice, randint
from userdata import *
template_path = 'sql_templates/university'
output_file = 'output.txt'


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
            new_query = query.replace('code', str(code)).replace('name', name).replace('bonus', bonus)
            f.write(f'{new_query}\n')


def programs_query():
    with open(f"{template_path}/programs.txt") as q:
        query = q.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        for dept_code, programs in data["edu_programs"]:
            for program in programs:
                new_query = query.replace('program_code', str(program[0])).replace('program_name', program[1])
                new_query = new_query.replace('department_code', str(dept_code)).replace('plan', str(program[2]))
                f.write(f'{new_query}\n')


def program_subjects_query():
    with open(f"{template_path}/program_subjects.txt") as q:
        query = q.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        for i, (program_subj_code, subjects) in enumerate(data["program_subjects"].items()):
            new_query = query.replace('code', str(base_id_program_subject + i))
            new_query = new_query.replace('program_id', str(program_subj_code))
            new_query = new_query.replace('min_result', str(randint(4, 7) * 10))
            for subject in subjects:
                new_subject_query = new_query.replace('subject_id', str(subject))
                f.write(f'{new_subject_query}\n')