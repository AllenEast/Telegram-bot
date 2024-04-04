CATEGORIES = [
    'ПРЕЗИДЕНТ',
    'ПРОИСШЕСТВИЯ',
    'ПОЛИТИКА',
    'ОБЩЕСТВО',
    'ЭКОНОМИКА',
    'МЫСЛИ ВСЛУ',
    'СПОРТ',
    'КУЛЬТУРА'
]


def get_category(category_name):
    if category_name == 'ПРЕЗИДЕНТ':
        return 'president'
    elif category_name == 'ПРОИСШЕСТВИЯ':
        return 'incidents'
    elif category_name == 'ПОЛИТИКА':
        return 'policy'
    elif category_name == 'ОБЩЕСТВО':
        return 'obshestvo'
    elif category_name == 'ЭКОНОМИКА':
        return 'economy'
    elif category_name == 'МЫСЛИ ВСЛУ':
        return 'misli'
    elif category_name == 'СПОРТ':
        return 'sport'
    elif category_name == 'КУЛЬТУРА':
        return 'culture'
