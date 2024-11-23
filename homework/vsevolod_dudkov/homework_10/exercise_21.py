PRICE_LIST = '''тетрадь 50р
 книга 200р
 ручка 100р
 карандаш 70р
 альбом 120р
 пенал 300р
 рюкзак 500р'''

PRICE_LIST = PRICE_LIST.replace("р\n", '')
PRICE_LIST = PRICE_LIST.rstrip('р')
NEW_LIST = PRICE_LIST.split()
PRICE_DICT = dict(zip(itr := iter(NEW_LIST), itr))
PRICE_DICT = {key: int(value) for key, value in PRICE_DICT.items()}

print(PRICE_DICT)
