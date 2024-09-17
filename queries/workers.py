from random import randint


template_path = 'sql_templates/workers'
output_file = 'output.txt'


def random_shift_record(n : int):
    with open(f"{template_path}/shift_records.txt") as q:
        query = q.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for _ in range(n):
            emp_id = randint(100, 107)
            hour = randint(10, 22)
            value = 1 if hour < 15 else 2
            timestamp = f'2023-10-19 {hour}:{randint(0, 5)}{randint(0, 9)}:{randint(0, 5)}{randint(0, 9)}'
            new_query = query.replace('employee_id', str(emp_id)).replace('timestamp', timestamp).replace('value', str(value))
            f.write(f'{new_query}\n')
