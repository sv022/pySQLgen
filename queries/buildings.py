from random import randint, choice
from userdata import *

def _random_date() -> str: # helper function
    daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = randint(1, 12)
    year = 2000 + randint(10, 24)
    if year % 4 == 0: daysinmonth[1] += 1
    day = randint(1, daysinmonth[month - 1])

    return f'{day // 10}{day % 10}.{month // 10}{month % 10}.{year}'


def buildings_query() -> None:
    with open(f"sql_templates/buildings/building_types.txt") as q:
        query = q.read()

    with open('output.txt', 'w', encoding='utf-8') as f:
        for code, name in zip(data["building_code"], data["building_name"]):
            new_query = query.replace('code', str(code)).replace('name', name)
            f.write(f'{new_query}\n')


def districts_query() -> None:
    with open(f"sql_templates/buildings/districts.txt") as q:
        query = q.read()

    with open('output.txt', 'w', encoding='utf-8') as f:
        for code, name in zip(data["district_code"], data["district_name"]):
            new_query = query.replace('code', str(code)).replace('name', name)
            f.write(f'{new_query}\n')


def criterias_query() -> None:
    with open(f"sql_templates/buildings/criterea.txt") as q:
        query = q.read()

    with open('output.txt', 'w', encoding='utf-8') as f:
        for code, name in zip(data["critera_code"], data["critera_name"]):
            new_query = query.replace('code', str(code)).replace('name', name)
            f.write(f'{new_query}\n')


def materials_query():
    with open(f"sql_templates/buildings/materials.txt") as q:
        query = q.read()

    with open('output.txt', 'w', encoding='utf-8') as f:
        for code, name in data["material"]:
            new_query = query.replace('code', str(code)).replace('name', name)
            f.write(f'{new_query}\n')


def agents_query() -> None:
    with open(f"sql_templates/buildings/agents.txt") as q:
        query = q.read()

    with open('output.txt', 'w', encoding='utf-8') as f:
        for i, (code, phone) in enumerate(zip(data["agent_code"], data["phone"])):
            new_query = query.replace('code', str(code)).replace('phone', phone)
            new_query = new_query.replace('surname', choice(data["surname"]))
            new_query = new_query.replace('lastname', choice(data["lastname"]))
            new_query = new_query.replace('name', choice(data["name"]))
            f.write(f'{new_query}\n')


def random_query(name : str, n : int, start_index = 0) -> None:
    """
    random_query() is used for estate_objects, ratings and deals tables.\n
    Before using it, generate all the predetermined queries\n
    Avaliable query names:\n
    estate_objects\n
    ratings\n
    deals
    To specify the ID to start from, use start_index
    """
    with open(f"sql_templates/buildings/{name}.txt") as q:
        query = q.read()
        q_start, query = query.split("VALUES")

    if name == "estate_objects":
        with open('output.txt', 'w', encoding='utf-8') as f:
            for i in range(n):
                new_query = query
                new_query = new_query.replace("object_code", str(base_id_object + i + start_index)).replace("district_code", str(choice(data["district_code"])))
                new_query = new_query.replace("adress", f'{choice(data["adress"])}, {randint(10, 150)}').replace("floor", str(randint(1, 22)))
                area = choice(data['area'])
                new_query = new_query.replace("room_number", str(area[1])).replace("area", str(area[0]))
                new_query = new_query.replace("building_code", str(choice(data["building_code"]))).replace("current_state", str(randint(1, 10) != 7))
                new_query = new_query.replace("price", str(randint(10000, 40000) * 1000)).replace("descript", f'object description {i}')
                new_query = new_query.replace("material", str(choice(data["material"])[0])).replace("publish_date", _random_date())
                new_query = new_query.replace("object_class", choice(["эконом", "комфорт", "бизнес"]))

                f.write(f'{q_start}VALUES{new_query}\n')

    elif name == "ratings":
        with open('output.txt', 'w') as f:
            for i in range(n):
                new_query = query
                new_query = new_query.replace('rate_code', str(base_id_rating + i + start_index)).replace('object_code', str(base_id_object + randint(0, n - 1)))
                new_query = new_query.replace('rate_date', _random_date()).replace('criteria', str(choice(data["critera_code"])))
                new_query = new_query.replace('rate', str(randint(1, 10)))
                f.write(f'{q_start}VALUES{new_query}\n')
    
    elif name == 'deals':
        with open('output.txt', 'w', encoding='utf-8') as f:
            for i in range(n):
                new_query = query
                new_query = new_query.replace('deal_code', str(base_id_deal + i + start_index)).replace('object_code', str(base_id_object + randint(0, n - 1)))
                new_query = new_query.replace('sell_date', _random_date()).replace('agent_code', str(choice(data['agent_code'])))
                new_query = new_query.replace('price', str(randint(10000, 40000) * 1000))
                f.write(f'{q_start}VALUES{new_query}\n')
    else: 
        raise Exception('No matching query name.')
