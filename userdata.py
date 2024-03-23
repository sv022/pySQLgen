data = {
    # buildings
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
    "surname": ["Наумов", "Кабан", "Гофман", "Кунякин", "Зомбанов", "Одеждин", "Голубцов", "Иванов", "Васильев", "Петров", 
                "Белый", "Серый", "Черный", "Шевцов", "Нагиев", "Барецкий", "Авдеев", "Панин", "Андреев", "Львов", "Шилов", 
                "Соловьев", "Новиков", "Колесов", "Троицкий", "Толкач", "Козлов", "Колесников", "Муравьев", "Голубев", "Львов"],
    "name": ["Александр", "Владистас", "Андрей", "Игорь", "Олег", "Макс", "Сергей", "Никита", "Антон", "Леха", "Алексей",
             "Дмитрий", "Стас", "Богдан"],
    "lastname": ["Александров", "Владистасов", "Андреевич", "Игоревич", "Олегович", "Максов", "Алексеевич"],
    "area": [(35.5, 1), (40, 1), (45.5, 1), (60, 2), (67.5, 2), (80, 3), (83.5, 3), (85, 3), (95.5, 4), (105, 4), (120, 5)],
    "current_state": ["pending", "active", "suspended", "sold", "active", "active", "active"],
    "phone": ["+7-(937)-975-54-12", "+7-(937)-983-63-01", "+7-(936)-926-64-46", "+7-(936)-975-12-75", "+7-(927)-901-76-43", "+7-(927)-926-92-16"],
    # university
    "departments": [(4001, 'ИИТ'), (4002, 'ИПТИП'), (4003, 'ИИИ'), (4004, 'ИРИ'), (4005, 'ИТХТ'), (4006, 'ИКБ'), (4007, 'ИТУ')],
    "subjects": [(101, 'Русский язык'), (102, 'Математика профильная'), (122, 'Математика базовая'), (103, 'Физика'), 
                 (104, 'Химия'), (105, 'Информатика и ИКТ'), (106, 'Биология'), (109, 'Английский язык')],
    "achievements": [(90011, 'Международные олимпиады', 10), (90021, 'Всероссийская олимпиада школьников', 7), (90425, 'РТ-Олимпиада', 5), 
                     (90432, 'Аттестат о среднем общем образовании', 2), (90444, 'Федеральная образовательная программа «Код будущего»', 3),
                     (90051, 'Спортивное звание или разряд', 2), (90052, 'Значок ГТО', 5), (90054, 'Волонтерская деятельность', 2)],
    "edu_programs": {
        4001: [(3010304, 'Прикладная математика', 21), (3090301, 'Информатика и вычислительная техника', 50), (3090303, 'Прикладная информатика', 38), 
               (3090304, 'Программная инженерия', 285)],
        4002: [(3090302, 'Информационные системы и технологии', 140), (3110304, 'Электроника и наноэлектроника', 28), (3120305, 'Лазерная техника и лазерные технологии', 40), 
               (3220301, 'Материаловедение и технологии материалов', 32), (3270301, 'Стандартизация и метрология', 25), (3540301, 'Дизайн', 6)],
        4003: [(3010302, 'Прикладная математика и информатика', 45), (3030302, 'Физика', 20), (3100501, 'Компьютерная безопасность', 40), 
               (3150306, 'Мехатроника и робототехника', 25), (3270303, 'Системный анализ и управление', 60)],
        4004: [(3090302, 'Информационные системы и технологии', 45), (3110301, 'Радиотехника', 60), (3110501, 'Радиоэлектронные системы и комплексы', 60)],
        4005: [(3040301, 'Химия', 90), (3180301, 'Химическая технология', 120), (3190301, 'Биотехнология', 125), (3200301, 'Техносферная безопасность', 25)],
        4006: [(3090302, 'Информационные системы и технологии', 110), (3100301, 'Информационная безопасность', 30), (3120301, 'Приборостроение', 50), 
               (3380501, 'Экономическая безопасность', 4), (3400501, 'Правовое обеспечение национальной безопасности', 6)],
        4007: [(3010305, 'Статистика', 25), (3270305, 'Инноватика', 50), (3380301, 'Экономика', 5), (3380302, 'Менеджмент', 5),
               (3380303, 'Управление персоналом', 27), (3380305, 'Бизнес-информатика', 4), (3400301, 'Юриспруденция', 7)]
    },
    "program_subjects": {
        3010304: (101, 102, 105), 
        3090301: (101, 102, 105),
        3090302: (101, 102, 105),
        3090303: (101, 102, 105),
        3090304: (101, 102, 105),
        3110304: (101, 102, 103),
        3120305: (101, 102, 103),
        3220301: (101, 102, 103),
        3270301: (101, 102, 103),
        3540301: (101, 102, 105),
        3010302: (101, 102, 105),
        3030302: (101, 102, 103),
        3100501: (101, 102, 105),
        3150306: (101, 102, 103),
        3270303: (101, 102, 105),
        3110301: (101, 102, 103),
        3110501: (101, 102, 103),
        3040301: (101, 122, 104, 106),
        3180301: (101, 122, 104, 106),
        3190301: (101, 122, 104, 106),
        3200301: (101, 122, 104, 106),
        3100301: (101, 102, 105),
        3120301: (101, 102, 103),
        3380501: (101, 102, 109),
        3380501: (101, 102, 105, 109),
        3010305: (101, 102, 105),
        3270305: (101, 102, 105),
        3270305: (101, 102, 105),
        3380301: (101, 102, 109),
        3380302: (101, 122, 109),
        3380302: (101, 122, 109),
        3380303: (101, 122, 109),
        3380305: (101, 102, 105, 109),
        3400301: (101, 102, 109),
    }
}

# buildings
base_id_object = 1000000
base_id_rating = 7000000
base_id_deal = 4000000
# university
base_id_program_subject = 8000
base_id_enrollee = 2000000
base_id_enrollee_achievement = 6000000
