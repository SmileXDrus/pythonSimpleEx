import traceback

# Несколько способов импорта
# 1. весь модуль
# import exceptions

# 2. весь модуль с псевдонимом
# import aexceptions as an
# import numpy as np

# 3. конкретно то что нужно
# from exceptions import Bear, PositiveValueError

# 4. всё - не рекомендуется
# from exceptions import *

# Импорт из модуля которые еще в папке (или в нескольких)
from oop_examples.exceptions import Bear, PositiveValueError

# Модули и пакеты
# from corepackage.exceptions import Bear, PositiveValueError
# from corepackage import Bear, PositiveValueError

print('Start moduls.py')
name = 'Фауст'
age = int(input('Введите возраст: '))

# 2. Обработка исключений
try:
    bear = Bear(name, age)
    # 5/0
except PositiveValueError as e:
    # Была ошибка
    print('Была ошибка', e)
    # print('Была ошибка', traceback.format_exc())
except ValueError:
    print('Ошибка в числе')
except Exception:
    print('Что то пошло не так?')
else:
    # Ошибки не было
    print('Медведь создан')
    print(bear)
finally:
    # Выпонить в любом случае была или не была
    print('end')
