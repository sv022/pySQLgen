from random import randint, choice, shuffle

data = {
    "building_code": [10000, 10001, 10002, 10003, 10004, 10005],
    "building_name": ["P-44", "I-700", "P-3", "1-553", "P-44T", "P-44T25"],
    "district_code": [523493, 523494, 542340, 546325],
    "district_name": ["Ленинский", "Октябрьский", "Заводской", "Волжский", "Левобережный", "Правобережный"],
    "adress": ['Ленинская', 'Октябрьская', 'Кировская', 'Ульяновская', 'К. Маркса', 'Энгельская', 
               'Московская', 'Волжская', 'Парковый проезд', 'Мирный переулок'],
    "material": [(6001, "Железобетон"), (6002, "Кирпич"), (6003, "Панель"), (6004, 'Вата')],
    "critera_code": [27001, 27002, 27003, 27004, 27005, 27006],
    "critera_name": ["экология", "чистота", "соседи", "условия для детей", "магазины", "безопасность"],
    "agent_code": [50421, 50123, 55424, 50912, 52631, 53734],
    "date": ["11.12.2020", "21.06.2022", "07.12.2022", "5.01.2023", "08.10.2022", "11.12.2023", "04.06.2024", "01.06.2021", "11.11.2021", "06.04.2022", 
            "14.04.2024", "22.10.2024", "23.05.2022", "31.08.2019", "18.02.2024", "12.04.2021", "19.11.2022", "17.04.2022", "12.05.2023", "28.03.2021"],
    "area": [(35.5, 1), (40, 1), (45.5, 1), (60, 2), (67.5, 2), (80, 3), (83.5, 3), (85, 3), (95.5, 4), (105, 4), (120, 5)],
    "current_state": ["pending", "active", "suspended", "sold", "active", "active", "active"],
    "phone": ["+7-(937)-975-54-12", "+7-(937)-983-63-01", "+7-(936)-926-64-46", "+7-(936)-975-12-75", "+7-(927)-901-76-43", "+7-(927)-926-92-16"] 
}

base_id_object = 1000000
base_id_rating = 7000000
base_id_deal = 4000000


def buildings_query():
    with open(f"sql_templates/building_types.txt") as q:
        query = q.read()

    with open('output.txt', 'w', encoding='utf-8') as f:
        for code, name in zip(data["building_code"], data["building_name"]):
            new_query = query.replace('code', str(code)).replace('name', name)
            f.write(f'{new_query}\n')


def criterias_query():
    with open(f"sql_templates/criterea.txt") as q:
        query = q.read()

    with open('output.txt', 'w', encoding='utf-8') as f:
        for code, name in zip(data["critera_code"], data["critera_name"]):
            new_query = query.replace('code', str(code)).replace('name', name)
            f.write(f'{new_query}\n')


def materials_query():
    with open(f"sql_templates/materials.txt") as q:
        query = q.read()

    with open('output.txt', 'w', encoding='utf-8') as f:
        for code, name in data["material"]:
            new_query = query.replace('code', str(code)).replace('name', name)
            f.write(f'{new_query}\n')


def agents_query():
    with open(f"sql_templates/agents.txt") as q:
        query = q.read()

    with open('output.txt', 'w', encoding='utf-8') as f:
        for code, name in zip(data["agent_code"], data["phone"]):
            new_query = query.replace('code', str(code)).replace('phone', name)
            f.write(f'{new_query}\n')


def random_query(name : str, n : int):
    with open(f"sql_templates/{name}.txt") as q:
        query = q.read()
        q_start, query = query.split("VALUES")

    if name == "estate_objects":
        with open('output.txt', 'w', encoding='utf-8') as f:
            for i in range(n):
                new_query = query
                new_query = new_query.replace("object_code", str(base_id_object + i)).replace("district_code", str(choice(data["district_code"])))
                new_query = new_query.replace("adress", f'{choice(data["adress"])}, {randint(10, 150)}').replace("floor", str(randint(1, 22)))
                area = choice(data['area'])
                new_query = new_query.replace("room_number", str(area[1])).replace("area", str(area[0]))
                new_query = new_query.replace("building_code", str(choice(data["building_code"]))).replace("current_state", str(randint(1, 10) != 7))
                new_query = new_query.replace("price", str(randint(10000, 40000) * 1000)).replace("descript", f'object description {i}')
                new_query = new_query.replace("material", str(choice(data["material"])[0])).replace("publish_date", choice(data["date"]))

                f.write(f'{q_start}VALUES{new_query}\n')

    elif name == "ratings":
        with open('output.txt', 'w') as f:
            for i in range(n):
                new_query = query
                new_query = new_query.replace('rate_code', str(base_id_rating + i)).replace('object_code', str(base_id_object + randint(0, n - 1)))
                new_query = new_query.replace('rate_date', choice(data["date"])).replace('criteria', str(choice(data["critera_code"])))
                new_query = new_query.replace('rate', str(randint(1, 10)))
                f.write(f'{q_start}VALUES{new_query}\n')
    
    elif name == 'deals':
        with open('output.txt', 'w', encoding='utf-8') as f:
            for i in range(n):
                new_query = query
                new_query = new_query.replace('deal_code', str(base_id_deal + i)).replace('object_code', str(base_id_object + randint(0, n - 1)))
                new_query = new_query.replace('sell_date', choice(data["date"])).replace('agent_code', str(choice(data['agent_code'])))
                new_query = new_query.replace('price', str(randint(10000, 40000) * 1000))
                f.write(f'{q_start}VALUES{new_query}\n')
